from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import database
import universities
import re

app = Flask(__name__, template_folder='../templates', static_folder='../static')
CORS(app)

# Initialize database on startup
database.init_database()

def parse_chat_message(message):
    """Parse chat message to extract intent and data"""
    message = message.lower().strip()
    
    # Add new result: "add result: name=John, result=95%, college=MIT, board=CBSE"
    if message.startswith('add result'):
        match = re.search(r'name=([^,]+),\s*result=([^,]+),\s*college=([^,]+),\s*board=(.+)', message, re.IGNORECASE)
        if match:
            return {
                'action': 'add',
                'data': {
                    'name': match.group(1).strip(),
                    'result': match.group(2).strip(),
                    'college': match.group(3).strip(),
                    'board': match.group(4).strip()
                }
            }
    
    # Search by name or ID: "search John" or "find John" or "search 2102002"
    elif message.startswith('search') or message.startswith('find'):
        query = message.split(maxsplit=1)[1] if len(message.split()) > 1 else None
        if query:
            return {'action': 'search', 'data': {'query': query}}
    
    # Get by ID: "get 5" or "show 5"
    elif message.startswith('get') or message.startswith('show'):
        parts = message.split()
        if len(parts) > 1 and parts[1].isdigit():
            return {'action': 'get_id', 'data': {'id': int(parts[1])}}
    
    # University search: "university DU" or "uni BUET" or "university list"
    elif message.startswith('university') or message.startswith('uni'):
        parts = message.split(maxsplit=1)
        if len(parts) > 1:
            query = parts[1].strip()
            if query.lower() in ['list', 'all', 'list all', 'show all']:
                return {'action': 'uni_list_all', 'data': {}}
            else:
                return {'action': 'uni_search', 'data': {'query': query}}
        else:
            return {'action': 'uni_list_all', 'data': {}}
    
    # List all: "list all" or "show all"
    elif 'list all' in message or 'show all' in message:
        return {'action': 'list_all', 'data': {}}
    
    # Delete: "delete 5"
    elif message.startswith('delete'):
        parts = message.split()
        if len(parts) > 1 and parts[1].isdigit():
            return {'action': 'delete', 'data': {'id': int(parts[1])}}
    
    # Help
    elif 'help' in message or message == '?':
        return {'action': 'help', 'data': {}}
    
    return {'action': 'unknown', 'data': {}}

@app.route('/')
def index():
    """Serve the main chat interface"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages and process commands"""
    data = request.get_json()
    message = data.get('message', '')
    
    if not message:
        return jsonify({'response': 'Please enter a message!'})
    
    parsed = parse_chat_message(message)
    action = parsed['action']
    action_data = parsed['data']
    
    try:
        if action == 'add':
            result_id = database.insert_result(
                action_data['name'],
                action_data['result'],
                action_data['college'],
                action_data['board']
            )
            response = f"✅ Result added successfully! ID: {result_id}\n"
            response += f"Name: {action_data['name']}\n"
            response += f"Result: {action_data['result']}\n"
            response += f"College: {action_data['college']}\n"
            response += f"Board: {action_data['board']}"
            
        elif action == 'search':
            results = database.get_result_by_name(action_data['query'])
            if results:
                response = f"Found {len(results)} result(s) for '{action_data['query']}':\n\n"
                for row in results:
                    response += f"ID: {row['id']}\n"
                    response += f"Name: {row['name']}\n"
                    response += f"Result: {row['result']}\n"
                    response += f"College: {row['college']}\n"
                    response += f"Board: {row['board']}\n"
                    response += f"Added: {row['created_at']}\n\n"
            else:
                response = f"❌ No results found for '{action_data['query']}'"
        
        elif action == 'get_id':
            result = database.get_result_by_id(action_data['id'])
            if result:
                response = f"Result Details (ID: {result['id']}):\n\n"
                response += f"Name: {result['name']}\n"
                response += f"Result: {result['result']}\n"
                response += f"College: {result['college']}\n"
                response += f"Board: {result['board']}\n"
                response += f"Added: {result['created_at']}"
            else:
                response = f"❌ No result found with ID {action_data['id']}"
        
        elif action == 'list_all':
            results = database.get_all_results()
            if results:
                response = f"📋 All Results ({len(results)} total):\n\n"
                for row in results:
                    response += f"ID: {row['id']} | {row['name']} | {row['result']} | {row['college']} | {row['board']}\n"
            else:
                response = "No results in database yet."
        
        elif action == 'delete':
            success = database.delete_result(action_data['id'])
            if success:
                response = f"✅ Result with ID {action_data['id']} deleted successfully!"
            else:
                response = f"❌ No result found with ID {action_data['id']}"
        
        elif action == 'uni_search':
            unis = universities.search_university(action_data['query'])
            if unis:
                response = f"🎓 Found {len(unis)} university(ies) for '{action_data['query']}':\n\n"
                for uni in unis:
                    response += universities.format_university_info(uni)
                    response += "\n" + "="*50 + "\n\n"
            else:
                response = f"❌ No university found for '{action_data['query']}'\nTry: university list (to see all universities)"
        
        elif action == 'uni_list_all':
            unis = universities.list_all_universities()
            response = f"🎓 All Public Universities in Bangladesh ({len(unis)} total):\n\n"
            for uni in unis:
                response += f"• {uni['short']} - {uni['name']} ({uni['district']})\n"
            response += f"\n💡 Type 'university <short form>' to see details\n"
            response += f"Example: university DU, uni BUET, university Chittagong"
        
        elif action == 'help':
            response = """📚 Available Commands:
            
• Add Result:
  add result: name=John Doe, result=95%, college=MIT, board=CBSE
  
• Search by Name or Student ID:
  search John
  search 2102002
  find MEHEDI
  
• Get by Database ID:
  get 5
  show 5
  
• List All Results:
  list all
  show all
  
• Search University:
  university DU
  uni BUET
  university Chittagong
  
• List All Universities:
  university list
  uni all
  
• Delete Result:
  delete 5
  
• Help:
  help
  ?"""
        
        else:
            response = "❓ I didn't understand that command. Type 'help' for available commands."
    
    except Exception as e:
        response = f"❌ Error: {str(e)}"
    
    return jsonify({'response': response})

if __name__ == '__main__':
    print("🚀 Server starting on http://localhost:5000")
    print("📝 Type 'help' in the chat for available commands")
    app.run(debug=True, host='0.0.0.0', port=5000)

# 💬 Client-Server Chat Application

A web-based client-server chat application where clients can interact with the server to manage student results and search for university information. The application features a real-time chat interface and a SQLite database to store and retrieve result records.

## 🌐 Live Demo

**🚀 Try it now:** [https://socket-programming-client-server-chatting.onrender.com/](https://socket-programming-client-server-chatting.onrender.com/)

> **Note:** The free tier may take 30-60 seconds to wake up after inactivity.

## 📋 Features

- **Chat-based Interface**: Natural language commands to interact with the database
- **Student Result Management**: Store and search 84+ student results with ID, name, CGPA, college, and board
- **University Information System**: Search 24 public universities in Bangladesh by name or short form
- **Real-time Communication**: Instant responses from the server
- **Responsive Design**: Beautiful gradient UI that works on all devices
- **CRUD Operations**: Add, search, view, list, and delete results
- **Comprehensive University Data**: Location, contact info, establishment date, and more

## 🗄️ Database Schema

The application uses SQLite with the following table structure:

```sql
CREATE TABLE results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    result TEXT NOT NULL,
    college TEXT NOT NULL,
    board TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

## 🚀 Setup Instructions

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Navigate to the project directory**:
   ```bash
   cd "/run/media/sofi/Study/Client Server"
   ```

2. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server**:
   ```bash
   python app/server.py
   ```

4. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

## 📚 Available Commands

### Student Result Commands

#### Add a New Result
```
add result: name=John Doe, result=95%, college=MIT, board=CBSE
```

#### Search by Name or Student ID
```
search John
search 2102002
find MEHEDI
```

#### Get Result by ID
```
get 5
show 5
```

#### List All Results
```
list all
show all
```

#### Delete a Result
```
delete 5
```

### University Search Commands

#### Search University by Short Form
```
university DU
uni BUET
university PSTU
```

#### Search University by Name
```
university Dhaka
university Chittagong
uni Rajshahi
```

#### List All Universities
```
university list
uni all
university
```

### Get Help
```
help
?
```
show all
```

### Delete a Result
```
delete 5
```

### Get Help
```
help
?
```

## 📁 Project Structure

```
Client Server/
├── app/
│   ├── server.py          # Flask server with chat logic
│   ├── database.py        # Database operations
│   └── universities.py    # University data and search functions
├── templates/
│   └── index.html         # Frontend HTML
├── static/
│   ├── style.css          # Styling
│   └── script.js          # Client-side JavaScript
├── requirements.txt       # Python dependencies
├── populate_data.py       # Script to populate student data
├── README.md             # This file
├── USAGE_GUIDE.md        # Quick usage guide
├── UNIVERSITY_FEATURE.md # University feature documentation
└── results.db            # SQLite database (created automatically)
```

## 🎯 Usage Examples

### Example 1: Adding a Student Result
```
Client: add result: name=Alice Smith, result=92%, college=Stanford, board=ICSE
Server: ✅ Result added successfully! ID: 1
        Name: Alice Smith
        Result: 92%
        College: Stanford
        Board: ICSE
```

### Example 2: Searching for Results
```
Client: search Alice
Server: Found 1 result(s) for 'Alice':
        
        ID: 1
        Name: Alice Smith
        Result: 92%
        College: Stanford
        Board: ICSE
        Added: 2025-11-22 10:30:45
```

### Example 3: Listing All Results
```
Client: list all
Server: 📋 All Results (3 total):
        
        ID: 3 | Bob Wilson | 88% | Harvard | CBSE
        ID: 2 | Carol Davis | 95% | MIT | State Board
        ID: 1 | Alice Smith | 92% | Stanford | ICSE
```

## 🛠️ Technical Details

### Backend
- **Framework**: Flask (Python web framework)
- **Database**: SQLite (lightweight, file-based database)
- **CORS**: Enabled for cross-origin requests
- **API**: RESTful endpoint at `/chat` for message processing

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern gradient design with animations
- **JavaScript**: Vanilla JS for chat functionality
- **Responsive**: Mobile-friendly design

### Message Parsing
The server uses regex pattern matching to parse natural language commands and extract relevant data for database operations.

## 🔧 Troubleshooting

### Server won't start
- Ensure Python 3.7+ is installed: `python --version`
- Install dependencies: `pip install -r requirements.txt`
- Check if port 5000 is available

### Database errors
- The database file `results.db` is created automatically
- If corrupted, delete `results.db` and restart the server

### Can't connect from browser
- Ensure the server is running
- Check the console for the correct URL
- Try `http://127.0.0.1:5000` if localhost doesn't work

## 🎨 Customization

### Change Server Port
Edit `app/server.py`, line 133:
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Change port here
```

### Modify Color Scheme
Edit `static/style.css` gradient colors:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

## 🌐 Deployment

This application is deployed on Render.com and automatically deploys from the `main` branch.

**Live URL:** [https://socket-programming-client-server-chatting.onrender.com/](https://socket-programming-client-server-chatting.onrender.com/)

### Deploy Your Own
1. Fork this repository
2. Sign up at [Render.com](https://render.com)
3. Create a new Web Service
4. Connect your GitHub repository
5. Render will auto-detect the configuration from `render.yaml`

## 📝 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

Created as a client-server chat application for result management.

**GitHub Repository:** [Socket_Programming_Client_Server_Chatting](https://github.com/safiullah-foragy/Socket_Programming_Client_Server_Chatting)

---

**Enjoy managing your results! 🎓**

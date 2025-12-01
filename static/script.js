const chatBox = document.getElementById('chatBox');
const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');

// Focus on input when page loads
messageInput.focus();

// Get current time formatted
function getCurrentTime() {
    const now = new Date();
    return now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });
}

// Add message to chat box
function addMessage(content, isClient = false) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isClient ? 'client-message' : 'server-message'}`;
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    
    if (isClient) {
        contentDiv.textContent = content;
    } else {
        // Format server messages
        const lines = content.split('\n');
        contentDiv.innerHTML = lines.map(line => {
            // Highlight certain patterns
            line = line.replace(/✅/g, '<span style="color: #28a745;">✅</span>');
            line = line.replace(/❌/g, '<span style="color: #dc3545;">❌</span>');
            line = line.replace(/📋/g, '<span style="color: #17a2b8;">📋</span>');
            line = line.replace(/📚/g, '<span style="color: #ffc107;">📚</span>');
            line = line.replace(/❓/g, '<span style="color: #6c757d;">❓</span>');
            
            // Make keywords bold
            line = line.replace(/\b(ID|Name|Result|College|Board|Added):/g, '<strong>$1:</strong>');
            
            return line;
        }).join('<br>');
    }
    
    const timeDiv = document.createElement('div');
    timeDiv.className = 'message-time';
    timeDiv.textContent = getCurrentTime();
    
    messageDiv.appendChild(contentDiv);
    messageDiv.appendChild(timeDiv);
    chatBox.appendChild(messageDiv);
    
    // Scroll to bottom
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Send message to server
async function sendMessage() {
    const message = messageInput.value.trim();
    
    if (!message) {
        return;
    }
    
    // Add client message to chat
    addMessage(message, true);
    messageInput.value = '';
    
    // Show loading indicator with typing animation
    const loadingDiv = document.createElement('div');
    loadingDiv.className = 'message server-message';
    loadingDiv.innerHTML = `
        <div class="message-content">
            <strong>Server:</strong> 
            <div class="typing-indicator">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    `;
    loadingDiv.id = 'loading';
    chatBox.appendChild(loadingDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
    
    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        });
        
        const data = await response.json();
        
        // Remove loading indicator
        const loading = document.getElementById('loading');
        if (loading) {
            loading.remove();
        }
        
        // Add server response
        addMessage(data.response, false);
        
    } catch (error) {
        // Remove loading indicator
        const loading = document.getElementById('loading');
        if (loading) {
            loading.remove();
        }
        
        addMessage('❌ Error: Could not connect to server. Please make sure the server is running.', false);
        console.error('Error:', error);
    }
    
    // Focus back on input
    messageInput.focus();
}

// Event listeners
sendButton.addEventListener('click', sendMessage);

messageInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// Quick command function
function setCommand(command) {
    messageInput.value = command;
    messageInput.focus();
    
    // Move cursor to appropriate position for add command
    if (command.includes('name=')) {
        const pos = command.indexOf('name=') + 5;
        messageInput.setSelectionRange(pos, pos);
    }
}

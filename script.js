// Function to update the chat log
function updateChatLog() {
    // Fetch the chat log from the text file using AJAX
    $.ajax({
      url: 'chat.txt', // Path to the text file
      dataType: 'text',
      success: function(data) {
        // Split the text file content into lines
        var lines = data.split('\n');
        
        // Get the chat log element by ID
        var chatLog = document.getElementById('chat-log');
  
        // Clear the previous content of the chat log
        chatLog.innerHTML = '';
  
        // Loop through each line of the text file
        lines.forEach(function(line) {
          // Create a new div element for each line
          var div = document.createElement('div');
  
          // Set the class of the div based on the content of the line
          if (line.startsWith('User:')) {
            // User input
            div.className = 'user-message';
          } else if (line.startsWith('AI response to find this:')) {
            // AI response to find this
            div.className = 'ai-find-message';
          } else if (line.startsWith('User input to find this')) {
            // AI response to find this
            div.className = 'user-message';
          }
            else {
            // Other messages
            div.className = 'other-message';
          }
  
          // Set the text content of the div
          div.textContent = line;
  
          // Append the div to the chat log
          chatLog.appendChild(div);
        });
      }
    });
  }
  
  // Call the updateChatLog function every 1 second
  setInterval(updateChatLog, 1);
  
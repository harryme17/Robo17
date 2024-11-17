# robo17 - Your Personal AI-Powered Voice Assistant

## Overview
**robo17** is an advanced, Python-driven voice assistant designed to make your life easier. Combining speech recognition, generative AI, and automation tools, it performs tasks such as web browsing, answering questions, and solving complex mathematical queries. The project includes a complete web interface for enhanced user interaction and multimedia support.

## Features
- **Voice Recognition**: Uses `speech_recognition` and `pyttsx3` for seamless interaction.
- **Generative AI Integration**: Powered by Google’s generative AI for intelligent query responses.
- **Web Automation**: Open and navigate web pages, play multimedia, and control applications.
- **Timed Reminders**: Set timers with spoken notifications.
- **File Management**: Interacts with local files for tasks like creating logs or reports.

## Project Structure
```
.
├── chat.txt          # Log file for conversation history
├── favicon.ico       # Favicon for web interface
├── index.html        # Main HTML page for web integration
├── robo17.py         # Core Python script for voice assistant functionality
├── script.js         # JavaScript for client-side interactions
├── styles.css        # Stylesheet for UI design
└── video25.mp4       # Example video for multimedia support
```

## Getting Started
### Prerequisites
- Python 3.x
- Required Python libraries:
  ```bash
  pip install pyttsx3 pyautogui SpeechRecognition wikipedia
  ```
- API key for Google Generative AI (replace in `robo17.py`)

### Running the Assistant
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/robo17.git
   ```
2. Navigate to the project directory:
   ```bash
   cd robo17
   ```
3. Run the Python script:
   ```bash
   python robo17.py
   ```

## Usage
- Start the assistant and use the hot word **"harry"** to trigger commands.
- Available commands include:
  - Wikipedia searches
  - Opening applications or websites
  - Playing music and videos
  - Setting timers
  - Performing web searches and mathematical queries

## License
This project is licensed under the MIT License. See `LICENSE` for more information.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss your ideas.

## Contact
For questions or suggestions, reach out at [your-email@example.com].

---
Bring the power of voice and AI to your daily tasks with **robo17**. Let's make technology more interactive!

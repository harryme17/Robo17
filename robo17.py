import pyautogui
import threading
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import google.generativeai as genai

genai.configure(api_key="Your_api_key_here")

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
    {
    "role": "user",
    "parts": ["Ask for a mathematical query or any question on the internet"]
  },
  {
    "role": "model",
    "parts": ["## Searching the answer for the mathematical query on the internet.\n\nPlease provide the mathematical query you want me to use for generating the solutions.\n\nOnce I have the query, I can help you by providing detailed explanations, examples, or step-by-step solutions to aid in understanding the mathematical concept.\n\nHere are some tips for formulating a good mathematical query:\n\n* Specify the mathematical concept: Clearly state the topic or type of problem you want to explore, such as algebra, calculus, geometry, etc.\n* Include relevant details: Provide equations, formulas, or specific parameters to ensure the solutions provided are tailored to your query.\n* Use precise language: Ensure the query is phrased in a way that can be understood by someone familiar with the mathematical topic.\n\nFeel free to provide your mathematical query, and I'll do my best to assist you in finding the solution!**"]
  },
])

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    open("chat.txt", "w").close()
    if hour < 12:
        with open("chat.txt", "a") as file:
                file.write("Good Morning\n")
        speak("Good Morning!")
    elif 12 <= hour < 18:
        with open("chat.txt", "a") as file:
                file.write("Good Afternoon\n")   
        speak("Good Afternoon!")
    elif 18 <= hour < 20:
        with open("chat.txt", "a") as file:
                file.write("Good Evening\n")
        speak("Good Evening!") 
    else:
        with open("chat.txt", "a") as file:
                file.write("Good Night\n")
        speak("Good Night!")  
    speak("I am robo17, whats you problem kiddo")       

hot_word = "harry"  # Define the hot word as a global variable

def takeCommand():
    global hot_word  
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        while True:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

            try:
                print("Recognizing...")    
                query = r.recognize_google(audio, language='en-in')
                print(f"User said: {query}\n")
                if 'exit' in query.lower():
                    speak("Emergency Exit!")
                    break
                elif hot_word in query.lower():
                    query = query.replace(hot_word, "")
                    return query

            except Exception as e:
                print("Say that again please...")

def setTimer(minutes):
    speak(f"Timer set for {minutes} minutes.")
    threading.Timer(minutes * 60, timerComplete).start()

def timerComplete():
    speak("Time's up!")

def listCommands():
    speak("Here are the commands you can use:")
    speak("1. Wikipedia search")
    speak("2. Open YouTube and search for something")
    speak("3. Open Google")
    speak("4. Open Stack Overflow")
    speak("5. Play music")
    speak("6. Check the time")
    speak("7. Open VS Code")
    speak("8. Send an email")
    speak("9. Open the camera")
    speak("10. Close the camera")
    speak("11. Show recent apps")
    speak("12. Switch tabs")
    speak("13. Operate the mouse")
    speak("14. Hit enter")
    speak("15. Press the right arrow key")
    speak("16. Press the left arrow key")
    speak("17. Find this")
    speak("18. Set a timer for a specific duration")
    speak("19. Exit the program")

def openDesktopItem(name):
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    for file in os.listdir(desktop_path):
        if name.lower() in file.lower():
            os.startfile(os.path.join(desktop_path, file))

if __name__ == "__main__":
    wishMe()
    
    with open("chat.txt", "a") as file:
        file.write("Chat started at: " + str(datetime.datetime.now()) + "\n")
    while True:
        query = takeCommand().lower()
        with open("chat.txt", "a") as file:
            file.write("User: " + query + "\n")
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            with open("chat.txt", "a") as file:
                file.write("Opening Wikipedia and searching for " + query + "\n")

        elif 'open youtube' in query:
              search_query = query.replace('open youtube and search for ', '').replace("open youtube for", "")
              speak(f"Opening YouTube and searching for {search_query}")
              url = f"https://www.youtube.com/results?search_query={search_query}"
              webbrowser.open(url)
              with open("chat.txt", "a") as file:
                # Remove 'open youtube' from the query before writing to the file
                file.write(f"Searching for {search_query} on YouTube\n")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
            speak("Opening Google")
            with open("chat.txt", "a") as file:
                file.write("Opening Google\n")

        elif 'play music' in query:
            search_query = query.replace(hot_word, "").replace("play music", "").strip()
            speak(f"Searching Spotify for {search_query}")
            webbrowser.open("https://open.spotify.com/search/{}".format(search_query.replace(" ", "%20")))
            with open("chat.txt", "a") as file:
                file.write(f"Searching Spotify for {search_query}\n")

        elif any(word in query for word in ['time', 'clock']):
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            with open("chat.txt", "a") as file:
                file.write(f"The time is {strTime}\n")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

    
        elif any(word in query for word in ['pl', 'camera']):
            os.system("start microsoft.windows.camera:")
            speak("Opening the camera")
            with open("chat.txt", "a") as file:
                file.write("Opening the camera\n")

        elif any(word in query for word in ['close', 'close the camera', 'close camera']):
            os.system("taskkill /f /im WindowsCamera.exe")
            speak("Camera application closed.")
            with open("chat.txt", "a") as file:
                file.write("Closing the camera application\n")
            
        elif any(word in query for word in ['show', 'recent', 'apps']):
            # Simulate pressing Win + Tab
            pyautogui.hotkey('win', 'tab')
            speak("Showing recent apps.")
            with open("chat.txt", "a") as file:
                file.write("Showing recent apps.\n")

        elif any(word in query for word in ['switch', 'tabs']):
            # Simulate pressing Alt + Tab
            pyautogui.hotkey('Alt', 'tab')
            speak("Switched.")
            with open("chat.txt", "a") as file:
                file.write("Switched tabs\n")

        elif 'operate the mouse' in query:
            # Simulate a mouse click at the current position
            pyautogui.click()
            speak("Mouse click performed.")
            with open("chat.txt", "a") as file:
                file.write("Mouse click performed\n")

        elif 'hit enter' in query:
            # Simulate pressing the Enter key
            pyautogui.press('enter')
            speak("Enter key pressed.")
            with open("chat.txt", "a") as file:
                file.write("Enter key pressed\n")

        elif 'full screen' in query:
            # Simulate pressing the Enter key
            pyautogui.press('f11')
            speak("Fullscreen")
            with open("chat.txt", "a") as file:
                file.write("Fullscreen\n")

        elif any(word in query for word in ['right']):
            # Simulate pressing the right arrow key
            pyautogui.press('right')
            speak("Right arrow key pressed.")
            with open("chat.txt", "a") as file:
                file.write("Right arrow key pressed\n")

        elif any(word in query for word in ['left', 'key']):
            # Simulate pressing the left arrow key
            pyautogui.press('left')
            speak("Left arrow key pressed.")
            with open("chat.txt", "a") as file:
                file.write("Left arrow key pressed\n")

        elif 'set a timer for' in query:
            try:
                minutes = int(query.split('set a timer for')[1].split('minutes')[0].strip())
                setTimer(minutes)
            except Exception as e:
                print(e)
                speak("Sorry, I couldn't set the timer. Please try again.")

        elif any(word in query for word in ['list', 'commands', 'command']):
            with open("chat.txt", "a") as file:
                file.write("Open YouTube and search for something\n Open Google\n Open Stack Overflow\n Play music\n Check the time\n Open VS Code\n Send an email\n Open the camera\n Close the camera\n Show recent apps\n Switch tabs\n Operate the mouse\n Hit enter\n Press the right arrow key\n Press the left arrow key\n Find this\n Set a timer for a specific duration\n Exit the program\n")
            listCommands()

        elif any(word in query for word in ['file', 'folder', 'shortcut']):
            words = query.split()
            # Get the name of the desktop item
            name = ' '.join(words[words.index('open') + 1:])
            with open("chat.txt", "a") as file:
                file.write("Opening \n")
            if not openDesktopItem(name):
                speak(f"{name}")

        elif 'find this' in query:
            query_text = query.split('find this', 1)[1].strip()
            with open("chat.txt", "a") as file:
                file.write("Please provide the input to send. \n")
            speak("Please provide the input to send.")
            input_text = takeCommand()
            with open("chat.txt", "a") as file:
                file.write("User input to find this: " + input_text + "\n")
            convo.send_message(input_text)
            response = convo.last.text
            print(response)
            with open("chat.txt", "a") as file:
                file.write("AI response to find this: " + response + "\n")
            speak(response)

        elif 'exit' in query:
            with open("chat.txt", "a") as file:
                file.write("Exiting the program... see you soonishh")
            speak("Exiting the program")
            break
    
        else:
            speak("Sorry,please repeat! For AI use keyword FIND THIS")

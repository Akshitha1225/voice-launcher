import speech_recognition as sr
import subprocess
import webbrowser

# Mapping voice commands to apps
app_commands = {
    "whatsapp": "C:\\Users\\pottu\\Desktop\\WhatsApp - Shortcut.lnk",
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "youtube": "https://www.youtube.com",
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "chat gpt"or "chatgpt": "https://chat.openai.com",
    "gmail": "https://mail.google.com",
    "file explorer": "explorer.exe",
    "camera": "start microsoft.windows.camera:"
}

# Function to open applications
def open_application(command):
    for app in app_commands:
        if any(trigger in command for trigger in [f"hello {app}", f"hai {app}"]):
            action = app_commands[app]
            if action.startswith("http"):
                webbrowser.open(action)  # Opens web URLs
            else:
                subprocess.Popen(action, shell=True)  # Opens desktop applications
            print(f"Opening {app}...")
            return
    print("Command not recognized!")

# Function to recognize voice
def recognize_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Recognized: {command}")  # Debugging output
        open_application(command)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError:
        print("Speech recognition service unavailable")

# Run voice recognition
recognize_voice()

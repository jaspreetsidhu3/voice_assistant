import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import logging

# Initialize logging
logging.basicConfig(filename='amigo.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize pyttsx3
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice

def speak(audio):
    """Convert text to speech."""
    engine.say(audio)
    engine.runAndWait()

def take_command():
    """Listen for voice commands and recognize them."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: " + query + "\n")
        logging.info(f"User said: {query}")
    except sr.UnknownValueError:
        speak("Sorry, I did not understand the audio.")
        return "None"
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return "None"
    except Exception as e:
        speak("An error occurred.")
        logging.error(f"Error: {e}")
        return "None"
    return query

def open_application(url, name):
    """Open an application or website."""
    try:
        speak(f"Opening {name}")
        webbrowser.open(url)
    except Exception as e:
        speak(f"Could not open {name}.")
        logging.error(f"Error opening {name}: {e}")

if __name__ == '__main__':
    speak("Amigo assistant activated")
    speak("How can I help you?")
    
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except wikipedia.exceptions.PageError:
                speak("No results found on Wikipedia.")
            except Exception as e:
                speak("An error occurred while searching Wikipedia.")
                logging.error(f"Wikipedia search error: {e}")
        elif 'are you' in query:
            speak("I am Amigo, developed by Jaspreet Singh.")
        elif 'open youtube' in query:
            open_application("https://youtube.com", "YouTube")
        elif 'open google' in query:
            open_application("https://google.com", "Google")
        elif 'open github' in query:
            open_application("https://github.com", "GitHub")
        elif 'open stackoverflow' in query:
            open_application("https://stackoverflow.com", "Stack Overflow")
        elif 'open spotify' in query:
            open_application("https://spotify.com", "Spotify")
        elif 'open whatsapp' in query:
            loc = "C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            if os.path.exists(loc):
                try:
                    speak("Opening WhatsApp")
                    os.startfile(loc)
                except Exception as e:
                    speak("Could not open WhatsApp.")
                    logging.error(f"Error opening WhatsApp: {e}")
            else:
                speak("WhatsApp is not installed.")
        elif 'play music' in query:
            open_application("https://spotify.com", "Spotify")
        elif 'local disk d' in query:
            open_application("file:///D://", "Local Disk D")
        elif 'local disk c' in query:
            open_application("file:///C://", "Local Disk C")
        elif 'local disk e' in query:
            open_application("file:///E://", "Local Disk E")
        elif 'sleep' in query:
            speak("Goodbye!")
            logging.info("Assistant terminated by user.")
            exit(0)
        else:
            speak("Sorry, I didn't understand that command.")

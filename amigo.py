import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# Set voice property to female
engine.setProperty('voice', voices[1].id)

def speak(audio):
    """Function to speak the given audio"""
    engine.say(audio)
    engine.runAndWait()

def take_command():
    """Function to take command from the microphone"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        speak("I didn't understand")
        return "None"
    return query

def main():
    """Main function to run the assistant"""
    speak("Amigo assistance activated")
    speak("How can I help you?")
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif 'are you' in query:
            speak("I am Amigo, developed by Jaspreet Singh")
        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("youtube.com")
        # ... [rest of the commands]
        elif 'sleep' in query:
            speak("Goodbye!")
            break

if __name__ == '__main__':
    main()

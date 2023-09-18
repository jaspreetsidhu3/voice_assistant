import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# Init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice


def speak(audio):
    print("speaking: ", audio)
    engine.say(audio)
    engine.runAndWait()

def choose_microphone():
    # Get a list of available microphones and print their names/indexes
    mic_list = sr.Microphone.list_microphone_names()
    print("Available Microphones:")
    for i, mic_name in enumerate(mic_list):
        print(f"{i}: {mic_name}")

    # Ask the user to select a microphone by index
    while True:
        try:
            selected_index = int(input("Enter the index of the microphone you want to use: "))
            if 0 <= selected_index < len(mic_list):
                return selected_index
            else:
                print("Invalid index. Please select a valid index.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")

def take_command(selected_microphone_index):
    r = sr.Recognizer()
    with sr.Microphone(device_index=selected_microphone_index) as source:
        try:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
            print("Audio captured")

            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language='en-US')
                print("User said: " + query + "\n")
                return query
            except Exception as e:
                print("Error recognizing speech: " + str(e))
                speak("I didn't understand")
                return "None"
        except Exception as ex:
            print("Error capturing audio: " + str(ex))
            speak("There was an error capturing audio.")
            return "None"

if __name__ == '__main__':
    speak("Amigo assistance activated ")
    speak("How can I help you")

    # Allow the user to choose a microphone
    selected_microphone_index = choose_microphone()
    print(f"Using microphone {selected_microphone_index}: {sr.Microphone.list_microphone_names()[selected_microphone_index]}")

    while True:
        query = take_command(selected_microphone_index).lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'are you' in query:
            speak("I am amigo developed by Jaspreet Singh")
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")
        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            loc = "C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(loc)
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")
        elif 'sleep' in query:
            exit(0)

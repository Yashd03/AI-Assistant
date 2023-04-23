import random
import datetime
import webbrowser
import wikipedia
import pyttsx3
import speech_recognition as sr

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize recognizer
r = sr.Recognizer()

# Set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Define a function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to listen for voice input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except:
        print("Sorry, I did not hear that.")
        return ""

# Define a function to get the current time
def get_time():
    now = datetime.datetime.now()
    return "The time is " + now.strftime("%I:%M %p")

# Define a function to search Wikipedia
def search_wikipedia(query):
    try:
        results = wikipedia.summary(query, sentences=2)
        return results
    except:
        return "Sorry, I could not find any results for that query."

# Define a function to open a webpage
def open_webpage(url):
    webbrowser.open(url)

# Define the main function
def main():
    speak("Hello, how can I assist you?")

    while True:
        text = listen().lower()

        if "hello" in text:
            speak("Hi, how are you?")
        elif "how are you" in text:
            speak("I am fine, thank you.")
        elif "what is your name" in text:
            speak("My name is AI Assistant.")
        elif "what time is it" in text:
            speak(get_time())
        elif "search" in text:
            query = text.replace("search", "").strip()
            results = search_wikipedia(query)
            speak(results)
        elif "open" in text:
            url = text.replace("open", "").strip()
            open_webpage(url)
        elif "stop" in text:
            speak("ok have a nice day bye.")
            break
        elif "bye" in text:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I did not understand that.")

if __name__ == "__main__":
    main()

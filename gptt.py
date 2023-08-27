import speech_recognition as sr
import pyttsx3
import wikipedia

# Initialize the speech recognition engine and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    if "wikipedia" in command:
        search_query = command.replace("wikipedia", "")
        try:
            result = wikipedia.summary(search_query, sentences=1)
            print(result)
            speak("According to Wikipedia, " + result)
        except wikipedia.exceptions.DisambiguationError:
            print("Multiple results found. Please be more specific.")
            speak("Multiple results found. Please be more specific.")
        except wikipedia.exceptions.PageError:
            print("No information found. Please try a different query.")
            speak("No information found. Please try a different query.")
    else:
        print("Sorry, I didn't understand that command.")
        speak("Sorry, I didn't understand that command.")

def main():
    with sr.Microphone() as source:
        print("Listening...")
        speak("How can I assist you?")
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
            process_command(command)
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand your speech.")
        except sr.RequestError:
            print("Sorry, I couldn't request results. Please check your internet connection.")

if __name__ == "__main__":
    main()

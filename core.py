import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# to convert voices into text
def takecommand():
    while True:
        r = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                print("listening...")
                r.pause_threshold = 2
                audio = r.listen(source, timeout=1.95, phrase_time_limit=5)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except Exception as e:
            return "none"
        return query

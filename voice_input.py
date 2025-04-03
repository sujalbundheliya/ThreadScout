import speech_recognition as sr

def get_voice_input():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            audio = r.listen(source, timeout=5)
            text = r.recognize_google(audio)
            print("📝 Recognized:", text)
            return text
    except Exception as e:
        print("⚠️ Voice input failed:", e)
        return None

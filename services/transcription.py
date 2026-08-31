import speech_recognition as sr
import tempfile
import os

def transcribe_audio(audio_file):
    try:
        temp_dir = tempfile.gettempdir()
        temp_path = os.path.join(temp_dir, "temp_audio.wav")
        
        with open(temp_path, "wb") as f:
            f.write(audio_file.getbuffer())
        
        recognizer = sr.Recognizer()
        
        try:
            with sr.AudioFile(temp_path) as source:
                audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio. Please try again with clearer audio."
        except sr.RequestError as e:
            return f"Error accessing Google Speech Recognition: {str(e)}"
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)
    except Exception as e:
        raise Exception(f"Error: {str(e)}")
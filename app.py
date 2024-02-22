import speech_recognition as sr
from google_trans_new import google_translator
import translators as ts
from gtts import gTTS 
from playsound import playsound 
import os

r = sr.Recognizer()
#translator = google_translator()    

while True:
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            speech_text = r.recognize_google(audio)
            print(speech_text)
            if speech_text == "stop":
                break
        except sr.UnknownValueError:
            print("Sorry could not recognize what you said")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        except Exception as e:
            print(e)       
        #txt_translated = translator.detect(speech_text)    
        #translated_text = translator.translate(speech_text, lang_tgt='it')
        translated_text = ts.translate_text(speech_text, translator='google', to_language='it')
        print(translated_text)         
        voice = gTTS(translated_text, lang='it', slow=False)
        #indirizzo file corrente
        file_path = os.path.dirname(os.path.abspath(__file__))
        file_path = file_path.replace("\\", "//") + "//"
        voice.save(os.path.join(file_path, "output.mp3")) 
        #apro il file audio, lo riproduco e poi lo elimino
        playsound(os.path.join(file_path, "output.mp3"))
        os.remove(os.path.join(file_path, "output.mp3"))

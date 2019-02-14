
#Snow boy https://snowboy.kitt.ai
#CMU Sphinkx
import speech_recognition as sr

#Audio del microfono
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Diga algo")
    audio = r.listen(source)

#Llamar al reconocedor de google
GOOGLE_CLOUD_CREDENTIALS = r"""{
  
}"""

try:
    print(
        r.recognize_google_cloud(
            audio,
            credentials_json=GOOGLE_CLOUD_CREDENTIALS
        )
    )
except sr.UnknownValueError:
        print("Google Cloud Speech no reconoce audio")
import pyttsx3
import fitz

with fitz.open("Origin_ A Novel ( PDFDrive ).pdf") as doc:
    text = ""
    for page in doc:
        text += page.get_text()

engine = pyttsx3.init()

engine.say(text='Good morning Mr T! Lovely evening?')
engine.save_to_file(text, "audiobook.mp3")
engine.runAndWait()



import pyttsx3, pikepdf
from PyPDF2 import PdfFileReader
from gtts import gTTS

def decr(path):
    """Decrypts the pdf file"""

    with pikepdf.open(path) as pdf:

        pdf.save(f"decrypted_{path}")

    print("Decryption complete!")

#decr('sample_pdf.pdf')

def pdfToTxt(path):
    """Converts PDF to Text"""

    pdf = PdfFileReader(path)
    num_pages = pdf.getNumPages()
    text = ""

    for i in range(num_pages):
        
        txt = pdf.getPage(i).extractText()
        text += txt
    return text

path = "decrypted_sample_pdf.pdf"

#print(pdfToTxt(path))

def txtToAud(txt):
    """Converts text to audio"""

    engine = pyttsx3.init()
    engine.setProperty('rate', 135)
    engine.say(txt)

    engine.runAndWait()

txt = pdfToTxt(path)

#txtToAud(txt)

def saveAud(txt):
    """Saves the audio to a file"""

    tts = gTTS(text=txt, lang='en')
    tts.save("aud.mp3")
    print('Audio file saved!')

saveAud(txt)



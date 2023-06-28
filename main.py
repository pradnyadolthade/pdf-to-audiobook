import pyttsx3
import PyPDF2
from tkinter import *

speaker = pyttsx3.init()


def start_reading():
    with open('pandp12p.pdf', 'rb') as book:
        pdf_reader = PyPDF2.PdfReader(book)
        pages = len(pdf_reader.pages)
        print(pages)
        for num in range(7, pages):
            page = pdf_reader.pages[num]
            text = page.extract_text()
            speaker.say(text)
            speaker.runAndWait()

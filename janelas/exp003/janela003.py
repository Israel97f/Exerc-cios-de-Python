from tkinter import Tk, ttk
from googletrans import Translator

tradutor = Translator()
resutado = tradutor.translate(
    'Ola mundo',
    src='pt',
    dest='en'
)

print(resutado.text)

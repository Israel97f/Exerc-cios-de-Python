from tkinter import Tk, Label, Button

janela = Tk()

butao = Button(
    text = 'Click-me'
)
butao.pack()

texto = Label(
    text = 'Ola mundo',
    font = ('Arial', 20)
)

texto.pack()

janela.mainloop()
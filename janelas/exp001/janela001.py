from tkinter import Tk, Label, Button
i = 1
def muda_label(evento):
    global i
    texto.config(text=f'apetou {i}')
    i += 1

def muda_botao():
    print('fui clicado')
    butao.config(text='fui clicado')

janela = Tk()

butao = Button(
    text = 'Click-me',
    font=('Arial', 12),
    command=muda_botao
)
butao.pack()

texto = Label(
    text = 'Ola mundo',
    font = ('Arial', 20)
)

texto.pack()
janela.bind('1', muda_label)
janela.mainloop()

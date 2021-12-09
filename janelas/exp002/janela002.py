from tkinter import Tk, font, ttk, Button

janela = Tk()

#estilo = ttk.Style()
#estilo.configure('TButton', font=('Havenica', 12))

b1 = Button(
    text='butão 1'
)

b2 = ttk.Button(
    text='butão 2'
)

b1.pack()
b2.pack(
    padx=10,
    pady=10
)

janela.mainloop()

from tkinter import Tk, ttk, Text
from googletrans import Translator
from ttkthemes import ThemedTk
from ttkbootstrap import Style


def traduzir(evento=None):
    text= entrada_texto.get('1.0', 'end')
    dest= saida.get()
    src= entrada.get()
    translator = Translator()
    resultado = translator.translate(text=text, dest=f'{dest}', src=f'{src}')

    saida_texto.configure(state='normal')
    saida_texto.delete('1.0', 'end')
    saida_texto.insert('1.0', resultado.text)
    saida_texto.configure(state='disabled')


janela = ThemedTk(theme='black')
janela.title('Boogle Translator')
Frame_geral = ttk.Frame() 

# ------ Entradas ---------
entrada_frame = ttk.Frame(Frame_geral)
entrada_label = ttk.Label(entrada_frame, text='entrada', font=('Roboto', 16))
entrada = ttk.Combobox(entrada_frame, values=('en', 'es', 'pt', 'ja'), font=('Roboto',16))
entrada.set('pt')
entrada_label.grid(row=0, column=0, padx=10, pady=10)
entrada.grid(row=0, column=1)
entrada_frame.pack()
entrada_texto = Text(Frame_geral, height=10, width=50, font=('Roboto', 16))
entrada_texto.pack(padx=10, fill='both', expand='yes')

# ------- Saidas ----------
saida_frame = ttk.Frame(Frame_geral)
saida_label = ttk.Label(saida_frame, text='Saida', font=('Roboto', 16))
saida = ttk.Combobox(saida_frame, values=('en', 'es', 'pt', 'ja'), font=('Roboto',16))
saida.set('en')
saida_label.grid(row=0, column=0, padx=10, pady=10)
saida.grid(row=0, column=1)
saida_frame.pack()
saida_texto = Text(Frame_geral, height=10, width=50, font=('Roboto', 16), state='disabled')
saida_texto.pack(padx=10, fill='both', expand='yes')

botao = ttk.Button(Frame_geral, text='Traduzir', command=traduzir)
botao.pack(fill='both', padx=10, pady=10)
janela.bind('<Return>', traduzir)

Frame_geral.pack()
janela.mainloop()

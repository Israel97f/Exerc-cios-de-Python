from sys import platform
from cx_Freeze import setup, Executable 

base=None
if platform == 'win32':
    base = 'win32GUI'

setup(
    name='Boogle Translator',
    version='1.0',
    description='tradutor feito na live de python',
    options={'build_exe':{'includes': ['tkinter', 'ttkbootstrap']}},
    executables = [
        Executable('janela003.py', base=base)
    ]
)
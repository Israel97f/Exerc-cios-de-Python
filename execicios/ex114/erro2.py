import requests

try:
    re = requests.get('http://pudim.com.br/')
except:
    print('\033[31mNão comsegui conectar com o site pudim\033[m')
else:
    print('\033[32mConexão com site pudim feita com sucesso')

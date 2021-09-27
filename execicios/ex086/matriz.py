lista = [[[], [], []], [[], [], []], [[], [], []]]
n = 0
for c in range(0, 3):
    for v in range(0, 3):
        lista[c][v].append(int(input(f'Digite um valor para posição {[c, v]} ')))
print('-=' * 30)
print(f"""
{lista[0][0]}  {lista[0][1]}  {lista[0][2]}
{lista[1][0]}  {lista[1][1]}  {lista[1][2]}
{lista[2][0]}  {lista[2][1]}  {lista[2][2]}
""")

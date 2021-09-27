lista = [[[], [], []], [[], [], []], [[], [], []]]
s = m = 0
for c in range(0, 3):
    for v in range(0, 3):
        lista[c][v].append(int(input(f'Digite um valor para posição {[c, v]} ')))
        if lista[c][v][0] % 2 == 0:
            s += lista[c][v][0]
        if c == 1 and (v == 0 or lista[1][v][0] > m):
            m = lista[1][v][0]
print('-=' * 30)
print(f"""
{lista[0][0]}  {lista[0][1]}  {lista[0][2]}
{lista[1][0]}  {lista[1][1]}  {lista[1][2]}
{lista[2][0]}  {lista[2][1]}  {lista[2][2]}
""")
print('-=' * 30)
print(f'A soma de valores é {s}')
print(f'A soma dos valores da tecera coluna é {lista[0][2][0] + lista[1][2][0] + lista[2][2][0]}')
print(f'O maior valor da segunda linha é {m}')

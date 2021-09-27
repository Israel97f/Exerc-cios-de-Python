import math

n = float(input('Diga o angulo '))

o = math.pi/180 * n

print('=' * 20)
print('Para o angulo {} temos \ntangente  = {:.3f} \ncoseno    = {:.3f} \nseno      = {:.3f}'.format(n, math.tan(o), math.cos(o), math.sin(o)))
print('=' * 20)

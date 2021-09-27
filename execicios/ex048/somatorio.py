s = 0
i = 0
for c in range(3, 500, 3):
    if c % 2 != 0:
        s += c
        i += 1
print('\033[35mO somatorio é {} e exitem {} números'.format(s, i))

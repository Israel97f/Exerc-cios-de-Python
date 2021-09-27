from time import sleep
for c in range(10, -1, -1):
    print('\033[33m{}'.format(c))
    sleep(1)
print('\U0001f386' * 20)

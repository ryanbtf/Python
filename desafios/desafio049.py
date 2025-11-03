n = int(input('Escolha um número e veja a tabuada dele: '))
print('\n TABUADA DO {}'.format(n))
for c in range (1, 11):
    print('{} x {} = {}'.format(n, c, n*c))
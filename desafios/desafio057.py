'''sexo = 0
while sexo != 'F':
    sexo = str(input('Digite o seu sexo (M/F):  ')).strip().upper()[0]
    if sexo != 'F':
        print('Digite um valor correto! (M/F)')
print('FIM')'''

sexo = str(input('Digite o seu sexo (M/F):  ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, por favor digite um sexo válido: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
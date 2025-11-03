print('Escreva 3 comprimentos de retas para saber se você pode formar um triângulo!')
cateto1 = int(input('Cateto 1: '))
cateto2 = int(input('Cateto 2: '))
hipotenusa = int(input('Hipotenusa: '))

if cateto1 + cateto2 > hipotenusa:
    print('Você pode formar um triângulo!')
else:
    print('Você não pode formar um triângulo :/')
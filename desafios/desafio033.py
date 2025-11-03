num1 = int(input('Escolha um número: '))
num2 = int(input('Escolha outro número: '))
num3 = int(input('Escolha outro número: '))

if num1 > num2 > num3:
    print('Maior número: {}'.format(num1))
    print('Menor número: {}'.format(num3))
elif num1 > num3 > num2:
    print('Maior número: {}'.format(num1))
    print('Menor número: {}'.format(num2))
elif num2 > num1 > num3:
    print('Maior número: {}'.format(num2))
    print('Menor número: {}'.format(num3))
elif num2 > num3 > num1:
    print('Maior número: {}'.format(num2))
    print('Menor número: {}'.format(num1))
elif num3 > num1 > num2:
    print('Maior número: {}'.format(num3))
    print('Menor número: {}'.format(num2))
elif num3 > num2 > num1:
    print('Maior número: {}'.format(num3))
    print('Menor número: {}'.format(num1))
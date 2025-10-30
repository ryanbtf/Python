print('\nPREFIRA QUE PRIMEIRO NÚMERO SEJA MAIOR QUE O SEGUNDO PARA RESULTADOS AGRADÁVEIS.\n')

num1 = int(input('Insira um número: '))
num2 = int(input('Insira mais um número: '))

print('\nCálculos com os números escolhidos:')

print('O número {} subtraído pelo número {} é igual a: {}'.format(num1, num2, num1 - num2))
print('O número {} multiplicado pelo número {} retorna: {}'.format(num1, num2, num1 * num2))
print('O número {} divido pelo número {} é igual a: {:.2f}'.format(num1, num2, num1 / num2))
print('A soma dos números {} e {} é igual a: {}'.format(num1, num2, num1 + num2))
print('A raiz quadrada do número {} é: {}'.format(num1, num1 ** 2))
print('Já a raiz quadrada do número {} é: {}'.format(num2, num2 ** 2))
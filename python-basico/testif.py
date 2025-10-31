num1 = 10
num2 = int(input('Tente adivinhar o número que estou pensando de 0 a 100: '))

if num2 == num1:
    print('Parabéns, você acertou!')
else:
    print('Número errado!')

def nums(x):
    if x == 10:
        return 'Número correto!'
    else:
        return 'Número errado!'
    
resultado = nums(num2)
print(resultado)
salario = int(input('Qual é o seu salário mensal?: '))
if salario >= 1250:
    psalario = salario + (salario*0.10)
    print('Você recebeu um aumento de 10%!')
else:
    psalario = salario + (salario*0.15)
    print('Você recebeu um aumento de 15%!')

print('\nSeu novo salário será R${}!'.format(psalario))
valorcasa = int(input('Qual o valor da casa que deseja comprar?: '))
salario = int(input('Qual é o seu salário mensalmente?: '))
anos = int(input('Em quantos anos pretende pagar esta casa?: '))
prestacao = valorcasa / (anos*12)

if prestacao > (salario*0.3):
    print('Você não pode financiar esta casa pois a prestação excede 30% do seu salário! :/')
else:
    print('A prestação mensal a ser paga será de R${:.2f}!'.format(prestacao))
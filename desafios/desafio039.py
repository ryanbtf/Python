anonascimento = int(input('Qual ano você nasceu?: '))
idade = 2025 - anonascimento

if idade < 18:
    tempof = 18 - idade
    print('Você ainda não precisa se alistar, faltam {} anos.'.format(tempof))
elif idade == 18:
    print('Você já pode se alistar!')
else:
    tempof = idade - 18
    print('Você ja deveria ter se alistado! já se passou {} ano(s) que você completou 18!'.format(tempof))
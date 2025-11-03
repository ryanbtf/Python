dtnascimento = int(input('Qual ano você nasceu?: '))
idade = 2025 - dtnascimento

if idade <= 9:
    print('Você é um atleta MIRIM!')
elif 9 < idade <= 14:
    print('Você é um atleta de categoria INFANTIL!')
elif 14 < idade <= 19:
    print('Você é um atleta de categoria JUNIOR!')
elif idade == 20:
    print('Você é um atleta SÊNIOR!')
elif idade > 20:
    print('Você é um atleta de categoria MASTER!')
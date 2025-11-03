nota1 = int(input('Qual a primeira nota?: '))
nota2 = int(input('Qual a segunda nota?: '))
media = (nota1 + nota2) / 2

print(media)

if media < 5:
    print('REPROVADO')
elif 5 <= media <= 6.9:
    print('RECUPERAÇÃO')
elif media >= 7:
    print('APROVADO')
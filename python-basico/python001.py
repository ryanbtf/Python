#print('\n ***Somos a maior empresa de comércio da América Latina! Seja muito bem-vindo!*** \n')

bemvindo = '***Somos a maior empresa de comércio da América Latina! Seja muito bem-vindo!***'

bemvindom = bemvindo.upper()

print(bemvindom)

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')

print('Olá {} {}, tudo bem com o(a) senhor(a)?'.format(nome, sobrenome))

idade = int(input('Esperamos que sim, digite aqui sua idade: '))

cidadecliente = input('Onde o(a) senhor(a) mora?: ')

print('Ok, tudo certo então senhor(a) {}, tens {} anos e mora em {}!'.format(nome, idade, cidadecliente))
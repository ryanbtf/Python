'''dados = dict()
dados = {'nome':'Pedro','idade':25}
dados['sexo'] = 'M'

print(dados)'''

filme = {'titulo':'Star Wars', 'ano':1997, 'diretor':'George Lucas'}

print(filme)
print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}')
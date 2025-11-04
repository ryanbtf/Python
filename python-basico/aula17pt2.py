dados = list()
pessoas = list()

dados.append('Pedro')
dados.append(25)
print(dados)
#dados.insert(0, 'Ryan')
#dados.insert(1, 18)
#print(dados)

pessoas.append(dados[:])

print(pessoas[0][1])
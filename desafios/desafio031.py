distancia = int(input('Quantos KM sua viagem terá?: '))
if distancia <= 200:
    preco1 = distancia * 0.5
    print ('Sua viagem custará R${}!'.format(preco1))
else:
    preco2 = distancia * 0.45
    print ('Sua viagem custará R${}!'.format(preco2))

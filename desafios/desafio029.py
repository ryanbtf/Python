vc = int(input('Você estava a quantos km/h com seu carro?: '))
multa = vc - 80
multacarro = multa * 7

if vc > 80:
    print('Você está sendo multado no valor de R${} por ultrapassar a velocidade!'.format(multacarro))
else:
    print('Você estava nos limites, siga sua viagem.')
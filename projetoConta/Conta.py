# Código da classe
class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True
    
    def gerarExtrato(self):
        print(f'numero: {self.numero}\ncpf: {self.cpf}\nnome: {self.nomeTitular}\nsaldo: R${self.saldo}')

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return ('Não existe saldo suficiente!')
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return ('Transferência realizada')

# Código do exemplos
'''c1 = Conta(numero= 1, cpf= 12344321, nomeTitular= 'Ryan', saldo= 9000)
c1.depositar(500)

valor_saque = 300
resultado_saque = c1.sacar(valor_saque)

if resultado_saque:
    print(f'Saque de R${valor_saque} realizado com sucesso!')
else:
    print('Saldo insuficiente para realizar o saque.')

print(f'Nome do titular da conta: {c1.nomeTitular}')
print(f'Número da conta: {c1.numero}')
print(f'CPF do titular da conta: {c1.cpf}')
print(f'Saldo da conta: R${c1.saldo}')

c1.gerarExtrato()'''

conta1 = Conta(123, 88888888, 'Maria', 0)
conta2 = Conta(124, 99999999, 'Pedro', 500)

print(conta2.transfereValor(conta1, 300))

conta1.gerarExtrato()
conta2.gerarExtrato()
from classes.Cliente import Cliente
from classes.Conta import Conta
from classes.ContaEspecial import ContaEspecial

# Testando código

cliente1 = Cliente(123, 'João', 'Rua X')
cliente2 = Cliente(224, 'Maria', 'Rua Y')
cliente3 = Cliente(456, 'Zezinho', 'Rua Z')

conta1 = Conta(cliente1, 1, 2000)
conta2 = Conta(cliente2, 2, 2000)
conta3 = ContaEspecial(cliente3, 3, 2000, 1000)

conta1.depositar(1000)
conta1.sacar(200)

conta1.extrato.gerar_extrato(conta1.numero)
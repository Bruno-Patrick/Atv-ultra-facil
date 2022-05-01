from cliente import Cliente
from conta import Conta
from banco import Banco

# cli1 = Cliente("123", "Rua lala", "03631929219", "19")
# cli1.verifica_cpf()
banco = Banco()
conta1 = Conta('Bruno', 2, 3)
# conta1.mostrar_conta()
conta2 = Conta('Marcelo', 15, 300)
conta3 = Conta('Eduardo', 2000, 3)
conta4 = Conta('Bruna', 9, 3)
conta3.sacar(1000)


banco.criar_conta('Banco do Brasil','Bruno', 10, 100)
print(Banco.bancos)
# print(Conta.todas_as_contas)
banco.imprimir_todas_as_contas()
# print(conta1._Conta.__num_conta)
# conta2 = Conta('123', 'Bruno', 2, 3)
# print(conta2._Conta.__num_conta)

# print(conta1._Conta__numero)
# conta1.sacar(2)
# conta1.criar_conta('Bruno',)
# print(conta1._Conta__saldo)
# conta1.delete()
# print(conta1._Conta__saldo)
# conta1.depositar(10)
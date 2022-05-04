from cliente import Cliente
from conta import Conta
from emprestimo import Emprestimo
from banco import Banco

cli1 = Cliente("Rua lala", "03631929219", "19")
cli1.verifica_cpf()
# banco = Banco()
# conta1 = Conta('Bruno', 2, 3)
# # conta1.mostrar_conta()
# conta2 = Conta('Marcelo', 15, 300)
conta2 = Conta("Maria",200,300)
conta3 = Conta('Eduardo', 20000, 3)
# conta3.get_numero()
# conta4 = Conta('Bruna', 9, 3)
# conta3.sacar(1000)
# banco_conta = Banco()

emp_conta3 = Emprestimo(conta3,2000,10,20)
# print(emp_conta3.valor_parcela())
# emp_conta3.emprestimo()
# print(emp_conta3.valor_parcela())
emp_conta3.paga_emprestimo_avista()
emp_conta3.pagar_emprestimo_parcela()

SANTANDER = Banco("SANTANDER",2)
SANTANDER.vincular_conta(conta2)
SANTANDER.vincular_conta(conta3)
BB = Banco("Banco do Brasil",1)
BB.vincular_conta(conta2)
BB.vincular_conta(conta3)
BB.extrato()
SANTANDER.extrato()
# 
# banco.criar_conta('Banco do Brasil','Bruno', 10, 100)
# print(Banco.bancos)
# print(Conta.todas_as_contas)
# banco.imprimir_todas_as_contas()
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
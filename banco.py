from conta import Conta
class Banco(Conta):
  
  bancos = []

  def __init__(self):
    pass

  @classmethod
  def criar_conta(cls, banco, titular, saldo, limite):
    nova_conta = [Conta(titular, saldo, limite)]
    nova_conta.insert(0, banco)
    cls.bancos.append(nova_conta)
    return nova_conta

  def imprimir_todas_as_contas(cls):
        print("Relação de Todas as Contas do Banco")
        for tr in cls.todas_as_contas:
            print("-----------")
            print(tr)
        print("\n--- Total de dinheiro do Banco: R${} ---\n"
        .format(Conta.total_dinheiro))
class Banco:

  _slots_ = ('__contas_do_banco', '__nome', '__numero')
  def __init__(self, nome, numero):
      self.__contas_do_banco = []
      self.__nome = nome
      self.__numero = numero

  def vincular_conta(self, conta):
      self.__contas_do_banco.append(conta)

  def linha(self):
    print("====================")

  def extrato(self):
      saldo = 0
      print(f"{self.__nome}")
      for i in self.__contas_do_banco:
          print(f"Conta {i.get_numero()}:\n{i.get_extrato().imprime()}\n Saldo da conta: {i.get_saldo()}")
          print()
          saldo += i.get_saldo()
      self.linha()
      return print(f"Total do banco {saldo}\n <><><><><><> \n")
    
  def remover_contas(self, conta):
      return self.__contas_do_banco.remove(conta)

from conta import Conta
class Banco(Conta):
  def __init__(self, nome):
      self.nome = nome

  def imprimir_todas_as_contas(cls):
        print("Relação de Todas as Contas do Banco")
        for tr in cls.todas_as_contas:
            print("-----------")
            print(tr)
        print("---Total de dinheiro do Banco: R${} ---"
        .format(Conta.total_dinheiro))
    
  def armazenar_dados_da_conta(self):
        dados_da_conta = [self.__numero, self.__titular,
        self.__saldo,self.__limite]
        return dados_da_conta
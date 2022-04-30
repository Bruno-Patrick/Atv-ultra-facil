class Conta:
    def __init__(self,cli,sal,lim):
        self.__numero += 1
        self.__titular = cli
        self.__saldo = sal
        self.__limite = lim

    def delete(self):
        if self.__saldo == 0:
            del self.__numero
            del self.__titular
            del self.__saldo
            del self.__limite
        else:
            return print("A CONTA DEVE ESTAR ZERADA!!")
    
    def depositar(self, valor):
        self.__saldo += valor
        return print(self.__saldo)

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo = self.__saldo - valor
            # self.extrato.transacoes.append('Saque de {}'.format(valor))
        else:
            print("Saldo insuficiente!!!")
    
    def criar_conta(self):
        self.Conta(self.__numero,self.__titular, self.__saldo, self.__limite)
        return print(self.Conta)
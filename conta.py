class Conta:
    #Numero da conta:
    _num_conta = 1
    todas_as_contas = []
    total_dinheiro = 0
    def __init__(self,cli,sal,lim):
        self.__numero = Conta._num_conta
        self.__titular = cli
        self.__saldo = sal
        self.__limite = lim
        Conta.total_dinheiro += self.__saldo
        Conta.todas_as_contas.append(self.armazenar_dados_da_conta())
        Conta._num_conta += 1

    def encerrar_conta(self):
        try:
            if self.__saldo == 0:
                del self.__numero
                del self.__titular
                del self.__saldo
                del self.__limite
                Conta._num_conta -= 1
            else:
                print("O SALDO DA CONTA DEVERÁ ESTAR ZERADO!!")
        except AttributeError:
            print("A CONTA FOI ENCERRADA!!")
    
    def depositar(self, valor):
        self.__saldo += valor
        Conta.total_dinheiro += valor
        return print(self.__saldo)

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            Conta.total_dinheiro -= valor

            # self.extrato.transacoes.append('Saque de {}'.format(valor))
        else:
            print("Saldo insuficiente!!!")
    

    
    

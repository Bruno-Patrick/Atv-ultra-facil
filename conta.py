from historico import Historico

class Conta:
    #Numero da conta:
    _num_conta = 1
    todas_as_contas = []
    total_dinheiro = 0
    __slots__ = ['__numero', '__titular', '__saldo', '__limite','__extrato']
    def __init__(self,cli,sal,lim):
        self.__numero = Conta._num_conta
        self.__titular = cli
        self.__saldo = sal
        self.__limite = lim
        self.__extrato = Historico()
        Conta.total_dinheiro += self.__saldo
        Conta.todas_as_contas.append(self.armazenar_dados_da_conta())
        Conta._num_conta += 1

    
    def get_numero(self):
        return self.__numero

    def get_saldo(self):
        return self.__saldo

    def get_extrato(self):
        return self.__extrato

    def armazenar_dados_da_conta(self):
        dados_da_conta = [self.__numero, self.__titular,
        self.__saldo,self.__limite]
        return dados_da_conta

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
        self.__extrato.transacoes.append('Saque de {}'.format(valor))
        return print(self.__saldo)

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            Conta.total_dinheiro -= valor
            self.__extrato.transacoes.append('Saque de {}'.format(valor))
        else:
            print("Saldo insuficiente!!!")
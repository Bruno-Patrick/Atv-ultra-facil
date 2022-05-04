class Emprestimo():
    
    __total_emprestimo = 0

    @classmethod
    def get__total_emprestimo(cls):
        return cls.__total_emprestimo

    @classmethod
    def total_emprestimos(cls):
        if cls.__total_emprestimo != 0:
            print("Total de emprestimos feitos pela conta: ",cls.__total_emprestimo)
        else:
            print("Não há empréstimos ativos para essa conta!")

    __slots__ = ['__juros', '__valor', '__periodo','__conta', '__total', '__periodo','__parcela']
    def __init__(self, conta,valor, juros, periodo):
        self.__juros = juros/100
        self.__valor = valor
        self.__periodo = periodo
        # self._extrato = Historico()
        self.__conta = conta
        self.__total = int(self.__valor*(1+self.__juros)**self.__periodo)
        self.__periodo = periodo
        self.__parcela = int(self.__valor*((self.__juros*(1+self.__juros)*self.__periodo)/(((1+self.__juros)*self.__periodo)-1)))
        return self.emprestimo()
   
    @property
    def get_emprestimo(self):
        return print(self.__valor)

    def emprestimo(self):
        valor_emp = self.__valor
        self.__conta.depositar(valor_emp)
        print("Emprestimo realizado para a conta",self.__conta.get_numero)
        Emprestimo.__total_emprestimo += 1
        # self.extrato.transacoes.append('Emprestimo de {}'.format(valor_emp))

    def paga_emprestimo_avista(self):
        valor = self.__total
        if self.__conta.get_saldo() < valor:
            print("\nNão é possivel pagar o emprestimo a vista\n")
        else:
            self.__conta.sacar(valor)
            print("Emprestimo quitado!!\n")
            self.__periodo = 0
            self.__total = 0

        
    def pagar_emprestimo_parcela(self):
        valor = self.__parcela
        if self.__conta.get_saldo() < valor or self.__total == 0:
            print("\nNão é possivel pagar a parcela!\n")
        else:
            self.__conta.sacar(valor)
            self.__total -= valor
            self.__periodo -= 1
            print("\nParcela paga com sucesso!\n")
        if valor < self.__total:
            print("Você ainda possui parcelas a pagar: ",self.__periodo,"\n") 
        else:
            print("Emprestimo quitado\n")
            self.__total = 0
            Emprestimo.__total_emprestimo -= 1
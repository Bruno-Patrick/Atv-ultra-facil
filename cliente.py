class Cliente:
    def __init__(self, n, e, cpf, i):
        self.__nome = n
        self.__endereco = e
        self.__CPF = cpf
        self.__idade = i
    
    def converter_cpf(self):
        CPF = []
        CPF = list(self.__CPF)
        for i in range(0,11):
            CPF[i] = int(CPF[i])
        return CPF

    def primeiro_digito(self):
        CPF = self.converter_cpf()
        KEY = 10
        SOMA = 0
        for i in range(0,9):
            SOMA += CPF[i]*KEY
            KEY -= 1
        MOD = SOMA%11
        if MOD < 2:
            primeiroDigito = 0
            return primeiroDigito
        else:
            primeiroDigito = 11-MOD
            return primeiroDigito

    def segundo_digito(self):
        CPF = self.converter_cpf()
        KEY = 11
        SOMA = 0
        for i in range(0,10):
            SOMA += CPF[i]*KEY
            KEY -= 1
        MOD = SOMA%11
        if MOD < 2:
            segundoDigito = 0
            return segundoDigito
        else:
            segundoDigito = 11-MOD
            return segundoDigito
    
    def verifica_cpf(self):
        PD = self.primeiro_digito()
        SD = self.segundo_digito()
        CPF = self.converter_cpf()

        if PD == CPF[9] and SD == CPF[10]:
            print("CPF VÁLIDO")
        else:
            print("CPF INVÁLIDO")
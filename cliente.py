class Cliente:
    def __init__(self, n, e, cpf, i):
        self.__nome = n
        self.__endereco = e
        self.__CPF = cpf
        self.__idade = i
    
    def valida_cpf(self):
        listaCpf = []
        listaCpf = list(self.__CPF)
        key = 10
        mult = 0
        soma = 0
        mod = 0
        while key > 2:
            for i in range(0,9):
                listaCpf[i] = int(listaCpf[i])
                mult = listaCpf[i]*key
                key -= 1
                soma += mult
            mod = soma%11
            if mod < 2:
                PD = 0
            else:
                PD = 11-mod
            print(PD)
            key = 11
            mult = 0
            soma = 0
            mod = 0
            for i in range(0,10):
                listaCpf[i] = int(listaCpf[i])
                mult = listaCpf[i]*key
                key -= 1
                soma += mult
            mod = soma%11
            if mod < 2:
                SD = 0
            else:
                SD = 11-mod
            print(SD)
        if PD == int(listaCpf[9]) and SD == int(listaCpf[10]):
            print("CPF VÁLIDO")
        else:
            print("CPF NO SERASA")

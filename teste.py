from banco import Banco
from cliente import Cliente
from conta import Conta
from emprestimo import Emprestimo
from historico import Historico

class Teste(Banco, Cliente, Conta, Emprestimo, Historico):
    
    def __init__(self, nome, numero, e, cpf, i, cli,sal,lim):
        super().__init__(nome, numero)
        super().__init__(e, cpf, i)
        super().__init__(cli, sal, lim)
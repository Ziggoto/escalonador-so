import random

__author__ = 'fabio'

class Bloco:
    _PID = 0

    def __init__(self):
        self.set_pid()
        self.tamanho = 1024

    def set_pid(self):
        self.pid = Bloco._PID
        Bloco._PID += 1

class SuperBloco(Bloco):

    def __init__(self):
        Bloco.__init__(self)
        self.bitvector = []

class BlocoHeader(Bloco):

    def __init__(self, nome_arquivo):
        Bloco.__init__(self)
        self.nome_arquivo = nome_arquivo
        self.tamanho_arquivo = self.tamanho
        self.qtde_blocos = 1
        self.primeiro_bloco = None

    def add_primeiro_bloco(self, novo_bloco):
        novo_bloco.dados_id = 0
        self.primeiro_bloco = novo_bloco
        self.tamanho_arquivo += novo_bloco.tamanho
        self.qtde_blocos += 1

class BlocoDados(Bloco):

    def __init__(self, dados_id=0):
        Bloco.__init__(self)
        self.dados_id = dados_id
        self.espaco_usado = 0
        self.prox_bloco = None

    def add_prox_bloco(self, prox_bloco):
        self.prox_bloco = prox_bloco

class BlocoRAM(Bloco):

    def __init__(self, tamanho=None):
        Bloco.__init__(self)
        if tamanho == None:
            self.tamanho = 2 ** random.randint(9, 11)
        self.conteudo = None

    def add_conteudo(self, processo):
        self.conteudo = processo

    def is_vazio(self):
        if self.conteudo == None:
            return True
        return False

    def __str__(self):
        conteudo = ""
        if self.conteudo != None:
            conteudo = self.conteudo
        return str(conteudo)

    def __repr__(self):
        return self.__str__()
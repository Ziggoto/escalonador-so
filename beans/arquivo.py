# -*- coding: utf-8 -*-

__author__ = 'fabio'

class Arquivo:
    """
    Implementação de um arquivo de blocos encadeados
    """

    def __init__(self):
        self.bloco_inicial = None
        self.nome = "Arquivo X"

    def get_tamanho(self):
        tamanho = 0
        aux = self.bloco_inicial
        while aux.prox_bloco != None:
            tamanho += aux.tamanho
            aux = aux.prox_bloco
        return aux

    def _gera_metadados(self):
        pass

    def save(self):
        """
        Método para salvar o arquivo em disco
        """
        self._gera_metadados()

        file = open(self.nome, 'wb')
        #TODO salvar baseado no objeto Bloco
        file.close()

class Bloco:
    """
    Implementação do bloco de um arquivo
    """

    def __init__(self, endereco):
        self.endereco = endereco
        self.prox_bloco = None
        self.tamanho = 32

    def set_prox_bloco(self, bloco):
        self.prox_bloco = bloco


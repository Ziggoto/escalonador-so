__author__ = 'fabio'

import os
import beans.bloco as bloco

class Disco:

    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.blocos = [bloco.SuperBloco()]
        self.super_bloco = self.blocos[0]

    def malloc(self, processo):
        pass

    def get_processo(self, processo):
        pass

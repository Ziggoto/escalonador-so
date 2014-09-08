# -*- coding: utf-8 -*-

''' 
### Algoritimos para implementar:

    1.FIFO (Não preemptivo)
    2.Filas de Prioridade Híbrido (com Round Robin)
    3.Round Robin
    4.Shortest Job First (Não preemptivo)
    5.Shortest Remaining Time
'''

from cores import Cores

class Escalonador():
    
    def __init__(self, cores=4):
        self.cores = Cores(cores)
        self.aptos = []
        self.executando = self.cores.cores
        self.quantum = 0
        
    
    def add_processo(self, processo):
        pass
    
    def draw_img(self):
        pass
    
    def executa(self):
        p = None
        while not self.cores.is_full():
            p = self.get_prox()
            if p == None:
                break
            self.cores.add_process(p)
            del self.aptos[0]
        self.quantum += 1
    
    def get_prox(self):
        if len(self.aptos) > 0:
            p = self.aptos[0]
            return p
        return None
    
    #Somente testes
    def exibe(self):
        for i in range(self.cores):
            print self.executando[i]
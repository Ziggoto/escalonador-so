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
from processo import Processo
from desenha import Desenho

class Escalonador():
    
    def __init__(self, cores=4, processos_aptos=10):
        self.cores = Cores(cores)
        self.aptos = []
        self.executando = self.cores.cores
        self.quantum = 0
        self.algoritimo = ""
        
        for i in range(processos_aptos):
            self.aptos.append(Processo(i))
        
    
    def add_processo(self, processo):
        self.aptos.append(processo)
    
    def draw_img(self):
        fila = self.aptos if self.algoritimo != "Fila de Prioridade com RoundRobin" else self.filas
        desenho = Desenho(cores=self.cores, algoritimo=self.algoritimo, fila_aptos=fila)
        desenho.draw()
    
    def executa(self):
        p = None
        while not self.cores.is_full():
            p = self.get_prox()
            if p == None:
                break
            self.cores.add_process(p)
            del self.aptos[0]
        self.quantum += 1
        self.cores.processa()
    
    def get_prox(self):
        if len(self.aptos) > 0:
            p = self.aptos[0]
            return p
        return None
    
    #Somente testes
    def exibe(self):
        for i in range(self.cores):
            print self.executando[i]
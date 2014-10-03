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
            try:
                self.add_processo(Processo(i))
            except AttributeError:
                pass
    
    def add_processo(self, processo):
        self.aptos.append(processo)
    
    def draw_img(self):
        #fila = self.aptos if self.algoritimo != "Fila de Prioridade com RoundRobin" else self.filas
        #desenho = Desenho(cores=self.cores, algoritimo=self.algoritimo, fila_aptos=fila)
        desenho = Desenho(self)
        return desenho.draw()
    
    def executa(self):
        p = None
        if self.cores.is_empty() and len(self.aptos) == 0:
            return False
        
        while not self.cores.is_full(): #Tem espaco em branco
            p = self.get_prox()
            if p == None:
                break
            self.cores.add_process(p) #Adiciona o processo no espaco em branco
            del self.aptos[0]
        self.quantum += 1
        return self.cores.processa()
    
    def get_prox(self):
        if len(self.aptos) > 0:
            p = self.aptos[0]
            return p
        return None
    
    def is_finished(self):
        if self.cores.is_empty() and len(self.aptos) == 0:
            return True
        return False
    
    #Somente testes
    def exibe(self):
        for i in range(self.cores):
            print self.executando[i]
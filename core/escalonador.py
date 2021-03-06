# -*- coding: utf-8 -*-

from cores import Cores
from processo import Processo
from desenha import Desenho
from memoria import MemoriaVirtual

class Escalonador():
    
    def __init__(self, cores=4, processos_aptos=10, tamanho_ram=4):
        self.memoria = MemoriaVirtual(self, tamanho_ram)
        self.cores = Cores(self.memoria, cores)

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
            return False #Encerra o programa...
        
        while not self.cores.is_full(): #Enquanto tiver espaco em branco nos cores
            p = self.get_prox()
            if p == None:
                break

            if not self.memoria.is_in_memory(p):
                if not self.memoria.has_memory_for(p):
                    #Tenta o Swap:
                    self.memoria.swap()
                    break #Se não tiver memória alocavel(mesmo fazendo merge), sai do looping
                self.alloc_process(p) #Aloca na memória, podendo fazer o Merge ou não

            self.cores.add_process(p) #Adiciona o processo nos cores
            del self.aptos[0]
        self.quantum += 1
        return self.cores.processa()
    
    def get_prox(self):
        if len(self.aptos) > 0:
            p = self.aptos[0]
            return p
        return None

    def alloc_process(self, processo):
        if self.memoria.malloc(processo):
            return True
        return False

    def is_finished(self):
        if self.cores.is_empty() and len(self.aptos) == 0:
            return True
        return False

    def fill_memory(self):
        '''
        Aloca todos os processos dos cores na memória, fazendo swap se necessário.
        :return:
        '''
        def get_old_process():
            for i in self.cores.cores:
                pass

        return None

    #Somente testes
    def exibe(self):
        for i in range(self.cores):
            print self.executando[i]

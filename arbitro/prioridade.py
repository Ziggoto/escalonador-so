from core.desenha import Desenho
from core.processo import Processo
import arbitro.round_robin
import core.escalonador

class FilaPrioridade(arbitro.round_robin.RoundRobin):
    
    def __init__(self, tempo_quantum=4, cores=4, processos_aptos=10):
        arbitro.round_robin.RoundRobin.__init__(self, tempo_quantum, cores, processos_aptos)
        self.algoritimo = "Fila de Prioridade com RoundRobin"
        
        self.f1 = [] # Fila de alta prioridade
        self.f2 = [] # Fila de media prioridade
        self.f3 = [] # Fila de baixa prioridade
        self.f4 = [] # Fila de baixissima prioridade
        
        self.filas = [self.f1, self.f2, self.f3, self.f4]
        self.pos = 0
        self.tempos = [4, 3, 2 , 1]
        
        self.fila_da_vez = 0
        self.ordena()
        
    def ordena(self):
        for i in self.aptos:
            if i.prioridade == 0:
                self.f1.append(i)
            elif i.prioridade == 1:
                self.f2.append(i)
            elif i.prioridade == 2:
                self.f3.append(i)
            else:
                self.f4.append(i)
                
    def add_processo(self, processo):
            if processo.prioridade == 0:
                self.f1.append(processo)
            elif processo.prioridade == 1:
                self.f2.append(processo)
            elif processo.prioridade == 2:
                self.f3.append(processo)
            else:
                self.f4.append(processo)
    
    #O tempo do quantum nao ta sendo considerado                
    def executa(self):
        if not self.is_finished():
            for i in self.cores.cores:
                if i is not None and i.tempo_processando == self.tempo_quantum:
                    i.tempo_processando = 1
                    if i.quantum_necessario == 0:
                        self.add_processo(i) #Recoloca em alguma fila
                        self.cores.rm_process(i) #Tira do escalonador
                    else:
                        i.quantum_necessario -= 1
                        
            #Insere nos cores
            processos = None
            while not self.cores.is_full():
                processos = self.get_prox(len(self.cores.get_empty_cores()))
                for p in processos:
                    self.cores.add_process(p)
                    #del self.filas[self.pos][0]
                    self.retira_processo(p)
            self.quantum += 1
            return self.cores.processa()
        
    def retira_processo(self, processo):
        index_i = 0
        for i in self.filas:
            index_j = 0
            for j in i:
                if j == processo:
                    del self.filas[index_i][index_j]
            index_j += 1
        index_i += 1
        
    def get_prox(self, qtde=1):
        lista = []
        pos_atual = self.pos
        fila = self.filas[pos_atual]
        
        if len(fila) > qtde:
            for i in range(qtde):
                lista.append(fila[i])
            #Incrementa
            if pos_atual < 3:
                self.pos += 1
            else:
                self.pos = 0
        else:
            aux = qtde - len(fila) #pega os que sobraram
            for i in range(len(fila)):
                lista.append(fila[i])
            #Incrementa
            if pos_atual < 3:
                self.pos += 1
            else:
                self.pos = 0
            for i in range(aux):
                lista.append(fila[i])    
        
        return lista
    
    def is_finished(self):
        t1 = len(self.f1)
        t2 = len(self.f2)
        t3 = len(self.f3)
        t4 = len(self.f4)
        t = [t1, t2, t3, t4]
        if len(set(t)) == 1 and t1 == 0 and self.cores.is_empty():
            return True
        return False
    
    #Soh testes
    def exibe(self):
        print "Cores:",
        print self.cores.cores
        print "Fila de Alta Prioridade: ",
        print self.f1
        print "Fila de Media Prioridade: ",
        print self.f2
        print "Fila de Baixa Prioridade: ",
        print self.f3
        print "Fila de Baixissima Prioridade: ",
        print self.f4
        #print self.filas
        print "====================="
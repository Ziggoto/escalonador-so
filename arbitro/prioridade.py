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
        
        for i in range(processos_aptos):
            self.add_processo(Processo(i))
        
        #self.fila_da_vez = 0
        #self.ordena()
        
    def ordena(self):
        pass
                
    def add_processo(self, processo):
        return self.filas[processo.prioridade].append(processo)
    
    def executa(self):
        def escalona():
            #Equivalente ao executa() do Escalonador
            #Adiciona processo aos cores
            if self.is_finished():
                return False
            
            processos = None
            while not self.cores.is_full(): #Tem espaco em branco
                processos = self.get_prox(len(self.cores.get_empty_cores()))
                if len(processos) == 0:
                    break
                for p in processos:
                    self.cores.add_process(p) #Adiciona o processo no espaco em branco
                    self.retira_processo(p)
            self.quantum += 1
            return self.cores.processa()
        
        if not self.is_finished():
            #Equivalente ao executa() do RoundRobin:
            #Retira dos cores processos "vencidos"
            for i in self.cores.cores:
                if i is not None and i.tempo_processando == self.tempo_quantum:
                    i.tempo_processando = 0
                    if i.quantum_necessario == 0:
                        self.add_processo(i) #Recoloca em alguma fila
                        self.cores.rm_process(i) #Tira do escalonador
                    else:
                        i.quantum_necessario -= 1
            return escalona()
        return False #Pra nao repetir mais

    
    def retira_processo(self, processo):
        try:
            for l in self.filas:
                try:
                    l.remove(processo)
                    return True
                except ValueError:
                    continue
            return False
        except AttributeError:
            return False
        
    def get_prox(self, qtde=1):
        lista = []
        fila = self.filas[self.pos]
        
        cont = 0
        max = len(fila) if len(fila) < qtde else qtde
        while max >= 1 or cont <= 4:
            for i in range(max):
                lista.append(fila[i])
                qtde -= 1 
            self.muda_fila()
            fila = self.filas[self.pos]
            max = len(fila) if len(fila) < qtde else qtde
            cont += 1
        
        return lista
    
    def muda_fila(self):
        if self.pos < 3:
            self.pos += 1
        else:
            self.pos = 0
    
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
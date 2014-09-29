from core.processo import Processo
import arbitro.round_robin
import core.escalonador

class FilaPrioridade(arbitro.round_robin.RoundRobin):
    
    def __init__(self, cores=4, processos_aptos=10):
        arbitro.round_robin.RoundRobin.__init__(self, cores, processos_aptos)
        self.algoritimo = "Fila de Prioridade com RoundRobin"
        
        self.f1 = [] # Fila de alta prioridade
        self.f2 = [] # Fila de media prioridade
        self.f3 = [] # Fila de baixa prioridade
        self.f4 = [] # Fila de baixissima prioridade
        
        self.filas = [self.f1, self.f2, self.f3, self.f4]
        self.pos = 0
        self.tempos = [4, 3, 2 , 1]
        
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
                    
    def executa(self):
        for i in self.cores.cores:
            if i is not None:
                if i.quantum_necessario == 0:
                    self.add_processo(i) #Recoloca em alguma fila
                    self.cores.rm_process(i) #Tira do escalonador
                else:
                    i.quantum_necessario -= 1
            
                    
        #Insere nos cores
        p = None
        while not self.cores.is_full():
            p = self.get_prox()
            if p == None:
                break
            self.cores.add_process(p)
            del self.filas[self.pos][0]
        self.quantum += 1
        self.cores.processa()
        
    def get_prox(self):
        pos_atual = self.pos
        fila = self.filas[pos_atual]
        if(len(fila) > 0):
            return fila[0]
        elif pos_atual < 3:
            self.pos += 1
            return self.get_prox() #Recursao
        else:
            self.pos = 0
        return None

#Teste parado:
'''
print "Fila de Alta Prioridade: ",
print f.f1
print "Fila de Media Prioridade: ",
print f.f2
print "Fila de Baixa Prioridade: ",
print f.f3
print "Fila de Baixissima Prioridade: ",
print f.f4
print f.filas

print "=== Cores ===="
print f.cores.cores
f.executa()
print f.cores.cores

for i in range(10):
    f.executa()

    print f.cores.cores
    print f.filas
'''
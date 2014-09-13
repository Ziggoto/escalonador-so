from core.processo import Processo
import arbitro.round_robin

class FilaPrioridade(arbitro.round_robin.RoundRobin):
    
    def __init__(self, cores=4):
        arbitro.round_robin.RoundRobin.__init__(self, cores)
        
    def ordena(self):
        f1 = [] # Fila de alta prioridade
        f2 = [] # Fila de media prioridade
        f3 = [] # Fila de baixa prioridade
        f4 = [] # Fila de baixissima prioridade
        
        for i in range(self.aptos):
            if i.prioridade == 0:
                f1.append(i)
            elif i.prioridade == 1:
                f2.append(i)
            elif i.prioridade == 2:
                f3.append(i)
            else:
                f4.append(i)
            
        fila_final = f1 + f2 + f3 + f4
        self.aptos = fila_final


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
        p = None
        
        for i in range(len(self.aptos)):
            p = self.aptos[i]
            
            if p.prioridade == 0:
                f1.append(p)
            elif p.prioridade == 1:
                f2.append(p)
            elif p.prioridade == 2:
                f3.append(p)
            else:
                f4.append(p)
            
        fila_final = f1 + f2 + f3 + f4
        self.aptos = fila_final


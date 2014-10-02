import arbitro
import core.escalonador

class ShortestRemainingTime(arbitro.round_robin.RoundRobin):
    
    def __init__(self, tempo_quantum=4, cores=4, processos_aptos=10):
        arbitro.round_robin.RoundRobin.__init__(self, tempo_quantum, cores, processos_aptos)
        self.algoritimo = "Shortest Remaining Time"
        
    def add_processo(self, processo):
        if len(self.aptos) == 0:
            arbitro.round_robin.RoundRobin.add_processo(self, processo)
        else:
            for i in self.aptos:
                if processo.tempo_restante <= i.tempo_restante:
                    self.aptos.insert(self.aptos.index(i), processo)
                    return True #Gambiarra mas ta valendo
            arbitro.round_robin.RoundRobin.add_processo(self, processo)


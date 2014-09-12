import core.escalonador

class ShortestJobFirst(core.escalonador.Escalonador):
    
    def __init__(self, cores=4):
        core.escalonador.Escalonador.__init__(self, cores)
     
    def add_processo(self, processo):
        if len(self.aptos) == 0:
            core.escalonador.Escalonador.add_processo(self, processo)
        else:
            for i in self.aptos:
                if processo.tempo_necessario <= i.tempo_necessario :
                    self.aptos.insert(self.aptos.index(i), processo)
                    return True #Gambiarra mas ta valendo
            core.escalonador.Escalonador.add_processo(self, processo)
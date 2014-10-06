import arbitro
import core.escalonador

class ShortestRemainingTime(core.escalonador.Escalonador):
    
    def __init__(self, tempo_quantum=4, cores=4, processos_aptos=10):
        core.escalonador.Escalonador.__init__(self, cores, processos_aptos)
        self.algoritimo = "Shortest Remaining Time"
        
    def add_processo(self, processo):
        if len(self.aptos) == 0:
            core.escalonador.Escalonador.add_processo(self, processo)
        else:
            for i in self.aptos:
                if processo.tempo_restante <= i.tempo_restante:
                    self.aptos.insert(self.aptos.index(i), processo)
                    return True #Gambiarra mas ta valendo
            core.escalonador.Escalonador.add_processo(self, processo)
    
    def executa(self):
        if len(self.aptos) > 0:
            for i in self.aptos:
                for core in self.cores.cores:
                    if core == None:
                        self.cores.add_process(self.aptos[0])
                        del self.aptos[0]
                        break
                    elif i.tempo_restante < core.tempo_restante:
                        maior_processo = self.get_maior_processo()
                        self.add_processo(maior_processo)
                        self.cores.rm_process(maior_processo)
                        self.cores.add_process(i)
                        del self.aptos[0]
                        break
                        
        if self.cores.is_empty():
            return False
        
        self.quantum += 1
        return self.cores.processa()
    
   
    def get_maior_processo(self):
        maior = self.cores.cores[0]
        for i in self.cores.cores:
            if maior == None:
                maior = i
                continue
            else:
                if i != None and i.tempo_restante > maior.tempo_restante:
                    maior = i
        return maior

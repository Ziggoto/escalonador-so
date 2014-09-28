import core.escalonador

class RoundRobin(core.escalonador.Escalonador):
    
    def __init__(self, cores=4, processos_aptos=10):
        core.escalonador.Escalonador.__init__(self, cores, processos_aptos)
        self.algoritimo = "Round Robin"
        
    def executa(self):
        for i in self.cores.cores:
            if i is not None:
                self.add_processo(i)
                self.cores.rm_process(i)
        
        core.escalonador.Escalonador.executa(self)
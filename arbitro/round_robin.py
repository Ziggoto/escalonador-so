import core.escalonador

class RoundRobin(core.escalonador.Escalonador):
    
    def __init__(self, cores=4):
        core.escalonador.Escalonador.__init__(self, cores)
        
    def executa(self):
        for i in self.cores.cores:
            if i is not None:
                self.add_processo(i)
                self.cores.rm_process(i)
        
        core.escalonador.Escalonador.executa(self)
     
    
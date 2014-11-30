from core.processo import Processo
import core.escalonador

class FIFO(core.escalonador.Escalonador):
    
    def __init__(self, cores=4, processos_aptos=10):
        core.escalonador.Escalonador.__init__(self, cores, processos_aptos)
        self.algoritimo = "FIFO"
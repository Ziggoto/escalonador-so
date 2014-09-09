import core.escalonador
from core.processo import Processo

class FIFO(core.escalonador.Escalonador):
    
    def __init__(self, cores=4):
        core.escalonador.Escalonador.__init__(self, cores)

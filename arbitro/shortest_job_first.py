import core.escalonador

class ShortestJobFirst(core.escalonador.Escalonador):
    
    def __init__(self, cores=4):
        core.escalonador.Escalonador.__init__(self, cores)
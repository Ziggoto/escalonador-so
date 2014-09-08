import core.escalonador
from core.processo import Processo

class FIFO(core.escalonador.Escalonador):
    
    def __init__(self, cores=4):
        core.escalonador.Escalonador.__init__(self, cores)
        
    def add_processo(self, processo):
        self.aptos.append(processo)


f = FIFO()
f.add_processo(Processo(1))
f.add_processo(Processo(2))
f.add_processo(Processo(3))
f.add_processo(Processo(4))
f.add_processo(Processo(5))
f.add_processo(Processo(6))

print f.aptos

print "Executando..."

f.executa()

print "Executando: ",
print f.executando
print "Aptos: ",
print f.aptos

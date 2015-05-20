import core.escalonador

class RoundRobin(core.escalonador.Escalonador):
    
    def __init__(self, tempo_quantum=4, cores=4, processos_aptos=10, tamanho_ram=4):
        core.escalonador.Escalonador.__init__(self, cores, processos_aptos, tamanho_ram)
        self.algoritimo = "Round Robin"
        self.tempo_quantum = tempo_quantum
        self.tentativa = 1

    def executa(self):
        for i in self.cores.cores:
            if i is not None and i.tempo_processando == self.tempo_quantum:
                i.tempo_processando = 1
                self.add_processo(i)
                self.cores.rm_process(i)
        
        return core.escalonador.Escalonador.executa(self)

'''
f = RoundRobin(processos_aptos=40)

print f.cores.cores
print f.aptos
print "====="

for i in range(4 * 8):
    f.executa()
    print f.quantum
    print f.cores.cores
    print f.aptos
    print "====="
'''

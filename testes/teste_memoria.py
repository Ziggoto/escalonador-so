__author__ = 'fabio'


from arbitro.round_robin import RoundRobin
from core.processo import Processo

f = RoundRobin()
print f.memoria.RAM
print f.memoria.RAM.is_alocavel()

aux = 0
for i in f.memoria.RAM.pos:
    p = Processo(aux)
    p.memoria_necessaria = i.tamanho
    f.memoria.RAM.malloc(p)
    print i.conteudo,
    aux += 1

print "\n",
print f.memoria.RAM.is_alocavel()
__author__ = 'fabio'

from arbitro.round_robin import RoundRobin
from core.processo import Processo

escalonador = RoundRobin(tamanho_ram=8, processos_aptos=40)
memoria = escalonador.memoria

aux = 1
for i in memoria.RAM.pos:
    i.conteudo = Processo(aux)
    aux += 1

RAM = memoria.RAM

print RAM

print memoria.swap()

print RAM

print memoria.swap()

print RAM


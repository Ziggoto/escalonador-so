from arbitro.fifo import FIFO
from arbitro.round_robin import RoundRobin

f = RoundRobin(processos_aptos=40)

while not f.cores.is_empty():
    f.executa()
from parser import Parser
from arbitro.round_robin import RoundRobin 
from core.processo import Processo

'''
0 = FIFO
1 = Fila de Prioridade
2 = Round Robin
3 = Shortest Job First
4 = Shortest Remaining Time
'''


p = Parser(None)

msg = '''{
  "atividade": "0",
  "algoritimo": "1",
  "cores": "4",
  "filas": "14",
  "quantum": "4"
  }'''


p.receive_msg(msg)
p.start()

import threading

def oi():
    print "Foi"
    p.escalonador.add_processo(Processo(50))
    
t = threading.Timer(5, oi)
t.start()

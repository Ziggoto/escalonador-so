import json

from core.escalonador import Escalonador

from arbitro.fifo import FIFO
from arbitro.prioridade import FilaPrioridade
from arbitro.round_robin import RoundRobin
from arbitro.shortest_job_first import ShortestJobFirst
from arbitro.shortest_remaining_time import ShortestRemainingTime

class Parser():
    
    def __init__(self):
        self.escalonador = Escalonador()
    
    def receive_msg(self, msg):
        self.msg = json.loads(msg)
        self.cores = int(self.msg['cores'])
        self.filas = int(self.msg['filas']) #qtde de processos na fila
        algoritimo = int(self.msg['algoritimo'])
        
        if algoritimo == 0:
            #FIFO
            self.escalonador = FIFO(self.cores, self.filas)
        elif algoritimo == 1:
            #Fila de Prioridade
            self.escalonador = FilaPrioridade(self.cores, self.filas)
        elif algoritimo == 2:
            #Round Robin
            self.escalonador = RoundRobin(self.cores, self.filas)
        elif algoritimo == 3:
            #Shortest Job First
            self.escalonador = ShortestJobFirst(self.cores, self.filas)
        elif algoritimo == 4:
            #Shortest Remaining Time
            self.escalonador = ShortestRemainingTime(self.cores, self.filas)
        else:
            print "Erro ao inicializar o escalonador"
    
    def start(self):
        pass
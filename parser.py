import json
import threading
import random

from core.escalonador import Escalonador
from core.processo import Processo

from arbitro.fifo import FIFO
from arbitro.prioridade import FilaPrioridade
from arbitro.round_robin import RoundRobin
from arbitro.shortest_job_first import ShortestJobFirst
from arbitro.shortest_remaining_time import ShortestRemainingTime

class Parser():
    
    def __init__(self, conn):
        self.escalonador = FIFO()
        self.conn = conn
    
    def receive_msg(self, msg):
        self.msg = json.loads(msg)
        opcao = int(self.msg['atividade'])
        
        def recria_escalonador():
            self.cores = int(self.msg['cores'])
            self.filas = int(self.msg['filas']) #qtde de processos na fila
            algoritimo = int(self.msg['algoritimo'])
            self.tempo_quantum = int(self.msg['quantum'])
            self.aux = self.filas
            
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
                
        def add_processo():
            self.escalonador.add_processo(Processo(random.randint(self.aux, 256)))
            self.aux += 1
    
        if opcao == 0:
            recria_escalonador()
        elif opcao == 1:
            add_processo()
    
    def start(self):
        def repete():
            #code = self.escalonador.draw_img()
            #self.conn.write_message(code) #Manda codigo
            print self.escalonador.cores.cores
            print self.escalonador.aptos
            print "========="
            
            e = self.escalonador.executa()
            print e
            self.start()
        t = threading.Timer(.01, repete)
        t.start()
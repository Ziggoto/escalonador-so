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
        self.escalonador = RoundRobin()
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
            tamanho_ram = int(self.msg['tamanho_ram'])
            
            if algoritimo == 0:
                #FIFO
                self.escalonador = FIFO(cores=self.cores, processos_aptos=self.filas)
            elif algoritimo == 1:
                #Fila de Prioridade
                self.escalonador = FilaPrioridade(cores=self.cores, processos_aptos=self.filas, tempo_quantum=self.tempo_quantum)
            elif algoritimo == 2:
                #Round Robin
                self.escalonador = RoundRobin(cores=self.cores, processos_aptos=self.filas, tempo_quantum=self.tempo_quantum, tamanho_ram=tamanho_ram)
            elif algoritimo == 3:
                #Shortest Job First
                self.escalonador = ShortestJobFirst(cores=self.cores, processos_aptos=self.filas)
            elif algoritimo == 4:
                #Shortest Remaining Time
                self.escalonador = ShortestRemainingTime(cores=self.cores, processos_aptos=self.filas, tempo_quantum=self.tempo_quantum)
            return 1
                
        def add_processo():
            self.escalonador.add_processo(Processo(self.aux))
            self.aux += 1
            return 0
    
        if opcao == 0:
            return recria_escalonador()
        elif opcao == 1:
            return add_processo()
    
    def start(self):
        def repete():
            code = self.escalonador.draw_img()
            self.conn.write_message(code) #Manda codigo
            #print self.escalonador.cores.cores
            #print self.escalonador.aptos
            #print "======"

            e = self.escalonador.executa()
            if e:
                self.start()
        t = threading.Timer(1, repete)
        t.start()
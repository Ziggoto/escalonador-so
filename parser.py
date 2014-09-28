import json

from core.escalonador import Escalonador

class Parser():
    
    def __init__(self):
        self.escalonador = Escalonador()
    
    def receive_msg(self, msg):
        self.msg = json.loads(msg)
        self.cores = msg['cores']
        self.filas = msg['filas'] #qtde de processos na fila
        
        if msg['algoritimo'] == 0:
            #FIFO
            pass
        elif msg['algoritimo'] == 1:
            #Fila de Prioridade
            pass
        elif msg['algoritimo'] == 2:
            #Round Robin
            pass
        elif msg['algoritimo'] == 3:
            #Shortest Job First
            pass
        elif msg['algoritimo'] == 4:
            #Shortest Remaining Time
            pass
        else:
            pass
    
raw_json = '{"algoritimo":"0","cores":"4","filas":"4"}'

p = Parser()
p.receive_msg(raw_json)
print p.msg
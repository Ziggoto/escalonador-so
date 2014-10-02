# -*- coding: utf-8 -*-

'''
### Metadados:
    
    1. PID
    2. Tempo de execução aleartório (entre 4 a 20 segundos)
    3. Estado (pronto, esperando, executando)
    4. Tempo restante
    5. Prioridade aleartória (entre 0 a 3)
'''
import random

class Processo():
    def __init__(self, pid):
        self.tempo_necessario = random.randint(4, 20)
        self.prioridade = random.randint(0, 3)
        self.tempo_restante = self.tempo_necessario #Inicialmente são iguais
        self.estado = "esperando"
        self.pid = pid
        self.quantum_necessario = 4 - self.prioridade #Somente para o Fila de Prioridade
        self.tempo_processando = 0 #Pros quantums
        
    def decrementa_tempo(self):
        self.tempo_necessario -= 1
        self.real_quantum -= 1
        
    def __str__(self):
        return str(self.pid)
    
    def __repr__(self):
        return self.__str__()
    
    def get_data(self):
        data = '''PID: %d\n
Tempo Restante: %d\n
Tempo Total: %d\n
Prioridade: %d ''' % (self.pid, self.tempo_restante, self.tempo_necessario, self.prioridade)
        return data
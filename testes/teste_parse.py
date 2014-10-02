from parser import Parser
from arbitro.round_robin import RoundRobin 

p = Parser(None)
p.escalonador = RoundRobin()
p.start()
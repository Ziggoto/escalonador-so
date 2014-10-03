from arbitro.prioridade import FilaPrioridade

f = FilaPrioridade(processos_aptos=15)

r = f.executa()
while r:
    r = f.executa()
    print f.exibe()

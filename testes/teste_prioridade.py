from arbitro.prioridade import FilaPrioridade

f = FilaPrioridade(processos_aptos=40)
f.exibe()

for i in range(30):
    f.executa()
    f.exibe()
    
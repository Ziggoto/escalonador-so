from arbitro.prioridade import FilaPrioridade

f = FilaPrioridade(processos_aptos=45, tempo_quantum=2)

for i in range(50):
    f.executa()
    f.exibe()
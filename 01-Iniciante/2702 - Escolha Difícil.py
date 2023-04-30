refeicoes_disponiveis = list(map(int, input().split()))
refeicoes_desejadas = list(map(int, input().split()))

passageiros_sem_ref = 0
for i in range(3):
    if refeicoes_disponiveis[i] < refeicoes_desejadas[i]:
        passageiros_sem_ref += refeicoes_desejadas[i] - refeicoes_disponiveis[i]

print(passageiros_sem_ref)


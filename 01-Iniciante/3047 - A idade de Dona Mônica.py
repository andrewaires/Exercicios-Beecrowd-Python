idade_monica = int(input())
idade_filho_1 = int(input())
idade_filho_2 = int(input())
idade_filho_3 = idade_monica - (idade_filho_1 + idade_filho_2)
if idade_filho_1 > idade_filho_2 and idade_filho_1 > idade_filho_3:
    print(idade_filho_1)
elif idade_filho_2 > idade_filho_1 and idade_filho_2 > idade_filho_3:
    print(idade_filho_2)
else:
    print(idade_filho_3)
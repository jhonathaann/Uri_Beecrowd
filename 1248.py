N = int(input())
aux = ""
janta = ""

for i in range(N):
    dietaDia = input()
    cafe = input()
    almoço = input()

    for j in range(len(cafe)):
        if cafe[j] not in dietaDia:
            janta = "CHEATER"

    for j in range(len(almoço)):
        if almoço[j] not in dietaDia:
            janta = "CHEATER"

    if janta != 'CHEATER':

        for j in range(len(dietaDia)):
            if dietaDia[j] not in cafe and dietaDia[j] not in almoço:
                aux += dietaDia[j]

        janta = ''.join(sorted(aux))

    print(janta)
    aux = ""
    janta = ""
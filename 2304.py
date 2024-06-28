dinheiroInicial,operacoes = map(int,input().split())
dalia = dinheiroInicial
eloi = dinheiroInicial
felix = dinheiroInicial

for i in range(operacoes):
    aux = input().split()

    if len(aux) == 3:
        if aux[0] == "C":
            if aux[1] == "D":
                dalia -= int(aux[2])
            elif aux[1] == "E":
                eloi -= int(aux[2])
            else:
                felix -= int(aux[2])
        elif aux[0] == "V":
            if aux[1] == "D":
                dalia += int(aux[2])
            elif aux[1] == "E":
                eloi += int(aux[2])
            else:
                felix += int(aux[2])

    elif len(aux) == 4:
        if aux[1] == "D":
            dalia += int(aux[3])
            if aux[2] == "E":
                eloi -= int(aux[3])
            else:
                felix -= int(aux[3])

        elif aux[1] == "E":
            eloi += int(aux[3])
            if aux[2] == "D":
                dalia -= int(aux[3])
            else:
                felix -= int(aux[3])
        else:
            felix += int(aux[3])
            if aux[2] == "D":
                dalia -= int(aux[3])
            else:
                eloi -= int(aux[3])
print(dalia,eloi,felix)
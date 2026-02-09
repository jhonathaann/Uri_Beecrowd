N = int(input())

for i in range(N):
    palavra_Secreta = ""

    texto = input()

    for i in range(len(texto)-1,-1,-1):
        if texto[i].islower():
            palavra_Secreta += texto[i]

    print(palavra_Secreta)
N = int(input())

for i in range(N):
    quantPessoas = int(input())

    for j in range(quantPessoas):
        idiomaNativo = input()

        if j == 0:
            aux = idiomaNativo
            continue

        if idiomaNativo != aux:
            idiomaFalado = "ingles"
            aux = False
            
        else:
            idiomaFalado = idiomaNativo

    print(idiomaFalado)
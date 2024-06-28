N = int(input())
nomeFinal = ""

for i in range(N):
    nome1 = input()
    nome2 = input()
    quant1 = int(len(nome1))

    for j in range(0,quant1,2):
        
        nomeFinal += nome1[j:j+2]
        nomeFinal += nome2[j:j+2]

    print(nomeFinal)
    nomeFinal = ""
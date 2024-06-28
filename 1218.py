paresIguais = 0
masculino = 0
feminino = 0
caso = 1

while True:
    try:
        numeraçao = input()
        naCaixa = input().split()
        quant_Caixa = len(naCaixa)

        for i in range(0,quant_Caixa,2):
            if naCaixa[i] == numeraçao:
                paresIguais += 1
                if naCaixa[i+1] == "F":
                    feminino += 1
                else:
                    masculino += 1

        if caso > 1:
            print()
        print(f"Caso {caso}:")
        print(f"Pares Iguais: {paresIguais}")
        print(f"F: {feminino}")
        print(f"M: {masculino}")
        caso += 1
        paresIguais = 0
        masculino = 0
        feminino = 0
        
    except:
        break
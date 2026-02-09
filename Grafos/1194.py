c = int(input())

def encontra_posfixa(prefixa, infixa):
    if not prefixa: return ""

    # raiz é sempre o primeiro elemento da prefixa
    raiz = prefixa[0]

    # encontrando o indice da raiz na infixa pra quebra ela exatamente nesse ponto
    indice_raiz = infixa.find(raiz)
    
    in_esquerda = infixa[:indice_raiz]
    in_direita = infixa[indice_raiz + 1:]

    # divindo a prefixa para saber quais letras pertencem a cada lado
    # o tamanho da parte esquerda da prefixa deve ser igual ao tamanho do lado esq da infixa
    tam_esq = len(in_esquerda)

    # a raiz a gente ja tem por isso começa do 1. como tem q ter o mesmo tamanho, e esta começando do 1, colocamos tam_esq+1
    pre_esquerda = prefixa[1: tam_esq +1 ]
    pre_direita = prefixa[tam_esq + 1 : ]

    # montamos a posfixa recursivamente
    return encontra_posfixa(pre_esquerda, in_esquerda) + encontra_posfixa(pre_direita, in_direita) + raiz

for i in range(c):
    linha = input().split()
    n = int(linha[0])
    prefixa = linha[1]
    infixa = linha[2]

    print(encontra_posfixa(prefixa, infixa))

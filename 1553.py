'''and len(repetidos) < flag'''
def busca(lista, repetidos, item, flag):
    contador = 0
    aux = 0

    if item in repetidos:
        return 0
    
    for i in range(len(lista)):        
        if lista[i] == item:
            contador += 1

    if contador >= flag:
        aux += 1
    return aux

rep = []
resposta = 0

n,k = map(int,input().split())

while n != 0 and k != 0:
    aux = [int(i) for i in input().split()]

    for i in range(len(aux)):
        resposta += busca(aux, rep, aux[i], k)
        rep.append(aux[i])

    print(resposta)
    resposta = 0
    rep = []

    n,k = map(int,input().split())
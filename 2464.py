def busca(string, letra):
    for i in range(len(string)):
        if string[i] == letra:
            return i


alf = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
resposta = ""

aux = input()
palavra = input()

for i in range(len(palavra)):
    posicao = busca(aux, palavra[i])
    resposta += alf[posicao]

print(resposta)
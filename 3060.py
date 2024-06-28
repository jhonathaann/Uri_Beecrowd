v = int(input())
p = int(input())
lista = []

if v % p == 0:
    for i in range(p):
        print(int(v/p))

else:
    resto = v % p
    valorMin = v // p
    valorMax = valorMin + 1

    for i in range(resto):
        lista.append(valorMax)

    for j in range(p - resto):
        lista.append(valorMin)

    for k in range(len(lista)):
        print(lista[k])
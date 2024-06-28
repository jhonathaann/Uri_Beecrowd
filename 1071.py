num1 = int(input())
num2 = int(input())

menorValor = num1
maiorValor = num1
soma = 0

if num2 < menorValor:
    menorValor = num2

if num2 > maiorValor:
    maiorValor = num2

for i in range(menorValor+1,maiorValor):
    if i % 2 != 0:
        soma += i

print(soma)
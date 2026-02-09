quantPositivo = 0
soma = 0

for i in range(6):
    numero = float(input())

    if numero > 0:
        soma += numero
        quantPositivo += 1

media = soma / quantPositivo
print(f"{quantPositivo} valores positivos")        
print(f"{media:.1f}")
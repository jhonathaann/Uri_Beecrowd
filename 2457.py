letra = input()
texto = input().split()
contador = 0

for i in range(len(texto)):
    if letra in texto[i]:
        contador += 1

porcentagem = (contador/len(texto)) * 100
print(f"{porcentagem:.1f}")
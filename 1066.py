quantPar = 0
quantImp = 0
quantPos = 0
quantNeg = 0

i = 0
while i < 5:
    num = int(input())
    if num % 2 == 0:
        quantPar += 1
    else:
        quantImp += 1

    if num > 0:
        quantPos += 1

    if num < 0:
        quantNeg += 1

    i += 1
    
print(f"{quantPar} valor(es) par(es)")
print(f"{quantImp} valor(es) impar(es)")
print(f"{quantPos} valor(es) positivo(s)")
print(f"{quantNeg} valor(es) negativo(s)")

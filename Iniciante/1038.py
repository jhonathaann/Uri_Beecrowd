codigoP,quantP = map(int,input().split())

if codigoP == 1:
    valorPago = quantP * 4

elif codigoP == 2:
    valorPago = quantP * 4.5

elif codigoP == 3:
    valorPago = quantP * 5

elif codigoP == 4:
    valorPago = quantP * 2

else:
    valorPago = quantP * 1.5

print(f"Total: R$ {valorPago:.2f}")
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

quantPares = 0

if num1 % 2 == 0:
    quantPares += 1

if num2 % 2 == 0:
    quantPares += 1

if num3 % 2 == 0:
    quantPares += 1

if num4 % 2 == 0:
    quantPares += 1

if num5 % 2 == 0:
    quantPares += 1

print(f"{quantPares} valores pares")    

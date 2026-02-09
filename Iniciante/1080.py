num1 = int(input())
maiorN = num1
entrada = 1

for i in range(99):
    num2 = int(input())

    if num2 > maiorN:
        maiorN = num2
        entrada = i + 2

print(maiorN)
print(entrada)
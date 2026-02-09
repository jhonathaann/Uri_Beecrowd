N = int(input())

for i in range(N):
        texto = input()

        num1 = int(texto[2:4])
        num2 = int(texto[5:8])
        num3 = int(texto[11:13])

        soma = num1 + num2 + num3
        print(soma)
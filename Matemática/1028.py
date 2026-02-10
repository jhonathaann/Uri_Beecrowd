n = int(input())

for i in range(n):
    num1, num2 = map(int, input().split())

    # algoritmo de euclides para encontrar o MDC entre dois numeros
    while(num1 % num2 != 0):
        resto = num1 % num2
        num1 = num2
        num2 = resto

    print(num2)

N = int(input())
diferenca = 0
casos = 1

while N != 0:
    print(f"Teste {casos}")

    for i in range(N):
        joao,ze = map(int,input().split())

        diferenca += joao - ze
        
        print(diferenca)

    N = int(input())

    print()

    if N == 0:
        break
    casos += 1
    diferenca = 0
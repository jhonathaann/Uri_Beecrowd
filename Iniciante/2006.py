N = int(input())
chas = input().split()
contador = 0

for i in range(len(chas)):
    if int(chas[i]) == N:
        contador += 1

print(contador)
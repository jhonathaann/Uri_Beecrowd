N = int(input())
aux = input().split()

somaPA = 0
somaAUX = 0

for i in range(N+1):
	somaPA += i

for j in range(len(aux)):
	somaAUX += int(aux[j])
	
pecaFaltando = somaPA - somaAUX

print(pecaFaltando)


# OUTRA SOLUÇÃO:

'''
N = int(input())
pecas = input().split()
falta = ""

for i in range(1,N+1):
    if str(i) not in pecas:
        falta = i
        break

print(falta)

'''
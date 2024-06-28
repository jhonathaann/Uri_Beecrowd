divisoes = int(input())
parteDivididas = input().split()

estoque = 0

for i in range(divisoes):
	estoque += int(parteDivididas[i]) - 1
print(estoque)
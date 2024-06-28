c,v = input().split()
carros = []
tempo = []
t = 0

for i in range(int(c)):
	aux = input().split()
	carros.append(i+1)
	
	for j in range(len(aux)):
		t += int(aux[j])
	tempo.append(t)
	t = 0
	
ind_min = 0
for i in range(len(tempo)):
	if tempo[i] < tempo[ind_min]:
						ind_min = i
						
primeiro = carros[ind_min]
del tempo[ind_min]
del carros[ind_min]

ind_min = 0
for j in range(len(tempo)):
	if tempo[j] < tempo[ind_min]:
		ind_min = j
segundo = carros[ind_min]

del tempo[ind_min]
del carros[ind_min]
ind_min = 0

for k in range(len(tempo)):
	if tempo[k] < tempo[ind_min]:
		ind_min = k
terceiro = carros[ind_min]

print(primeiro)
print(segundo)
print(terceiro)
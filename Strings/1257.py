n = int(input())

for k in range(n):
    total = 0
    L = int(input())

    for j in range(L):
        string = input()

        for i in range(len(string)):
            soma_parcial = 0        
            soma_parcial += j + i + ord(string[i]) - 65
            total += soma_parcial
            
    print(total)

N = int(input())

for i in range(N):
    x,y = map(int,input().split())

    rafael = (3*x)**2 + y**2
    beto = 2*(x**2) + (5*y)**2
    carlos = (-1)*100*x  + y**3

    if rafael > beto and rafael > carlos:
        print("Rafael ganhou")
    
    elif beto > rafael and beto > carlos:
        print("Beto ganhou")

    else: 
        print("Carlos ganhou")
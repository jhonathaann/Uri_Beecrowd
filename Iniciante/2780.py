d = int(input())

if d <= 800:
    cesta = 1
elif d > 800 and d <= 1400:
    cesta  = 2
elif d > 1400 and d <= 2000:
    cesta = 3
print(cesta)    
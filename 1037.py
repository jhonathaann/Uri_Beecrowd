numero = float(input())

if numero < 0 or numero > 100:
    print("Fora de intervalo")
elif 0 <= numero and numero <= 25:
    print("Intervalo [0,25]")
elif 25 < numero and numero <= 50:
    print("Intervalo (25,50]")
elif 50 < numero and numero <= 75:
    print("Intervalo (50,75]")
elif 70 < numero and numero <= 100:
    print("Intervalo (75,100]")
N = int(input())

somaKG = 0
somaDin = 0


for i in range(N):
    valorGasto = float(input())
    somaDin += valorGasto
    nomeFrutas = input().split()
    quantFrutas = len(nomeFrutas)
    somaKG += quantFrutas

    print(f"day {i + 1}: {quantFrutas} kg")

media = somaKG / N
mediaGasto = somaDin / N

print(f"{media:.2f} kg by day\nR$ {mediaGasto:.2f} by day")
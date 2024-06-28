N = int(input())
num = 1

for i in range(N):
    x = num
    y = num ** 2
    z = num ** 3

    print(f"{x} {y} {z}")

    num += 1
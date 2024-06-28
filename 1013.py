a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
x = (a + b + abs(a - b))/2
y = int((x + c + abs(x - c))/2)
print(y,"eh o maior")

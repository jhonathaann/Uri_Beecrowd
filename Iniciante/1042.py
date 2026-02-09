num1 = int(input())
num2 = int(input())
num3 = int(input())

if (num1 < num2) & (num1 < num3):
    if(num2 < num3):
        print(num1)
        print(num2)
        print(num3)
    else:
        print(num1)
        print(num3)
        print(num2)

elif(num2 < num1) & (num2 < num3):
    if(num1 < num3):
        print(num2)
        print(num1)
        print(num3)
    else:
        print(num2)
        print(num3)
        print(num1)
else:
    if(num1 < num2):
        print(num3)
        print(num1)
        print(num2)
    else:
        print(num3)
        print(num2)
        print(num1)

# printando os numeros na ordem em que fora lidos
print("\n")
print(num1)
print(num2)
print(num3)

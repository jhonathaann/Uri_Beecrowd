num1 = int(input())

for i in range(num1):
    numN = int(input())

    if numN == 0:
        print("NULL")

    if numN % 2 == 0 and numN > 0:
        print("EVEN POSITIVE")
    if numN % 2 == 0 and numN < 0:
        print("EVEN NEGATIVE")


    if numN % 2 != 0 and numN > 0:
        print("ODD POSITIVE")
    if numN % 2 != 0 and numN < 0:
        print("ODD NEGATIVE")  
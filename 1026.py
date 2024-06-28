while True:
    try:
        num1,num2 = map(int,input().split())
        somaBin = num1 ^ num2
        print(somaBin)
    except:
        break


# SOLUÇÃO COM TIMILIMT

'''
while True:
    try:
        num1,num2 = map(int,input().split())

        somaBin = ""

        bin1 = format(num1,'032b')
        bin2 = format(num2,'032b')

        for i in range(32):
            if bin1[i] == bin2[i]:
                somaBin += '0'
            else:
                somaBin += '1'
        somaBin = int(somaBin,2)        
        
        print(somaBin)

    except:
        break

'''
a,b,c = map(float,input().split())

if a == b and a ==c:
    print("TRIANGULO ACUTANGULO\nTRIANGULO EQUILATERO")

elif a >= b and a >= c:
    if a >= b + c:
        print("NAO FORMA TRIANGULO")
    elif a**2 == b**2 + c**2:
        if b == c:
            print("TRIANGULO RETANGULO\nTRIANGULO ISOCELES")
        else:
            print("TRIANGULO RETANGULO")

    elif a**2 > b**2 + c**2:
        if b == c:
            print("TRIANGULO OBTUSANGULO\nTRIANGULO ISOSCELES")
        else:
             print("TRIANGULO OBTUSANGULO")
    elif a**2 < b**2 + c**2:
        if b == c or b == a or a == c:
            print("TRIANGULO ACUTANGULO\nTRIANGULO ISOSCELES")
        else:
            print("TRIANGULO ACUTANGULO")

elif b >= a and b >= c:
    if b >= a + c:
        print("NAO FORMA TRIANGULO")
    elif b**2 == a**2 + c**2:
        if a == c:
            print("TRIANGULO RETANGULO\nTRIANGULO ISOCELES")
        else:
            print("TRIANGULO RETANGULO")

    elif b**2 > a**2 + c**2:
        if a == c:
            print("TRIANGULO OBTUSANGULO\nTRIANGULO ISOSCELES")
        else:
             print("TRIANGULO OBTUSANGULO")
    elif b**2 < a**2 + c**2:
        if a == c or a == b or b == c:
            print("TRIANGULO ACUTANGULO\nTRIANGULO ISOSCELES")
        else:
            print("TRIANGULO ACUTANGULO")
    
elif c >= a and c >= b:
    if c >= a + b:
        print("NAO FORMA TRIANGULO")
    elif c**2 == a**2 + b**2:
        if a == b:
            print("TRIANGULO RETANGULO\nTRIANGULO ISOCELES")
        else:
            print("TRIANGULO RETANGULO")

    elif c**2 > a**2 + b**2:
        if a == b:
            print("TRIANGULO OBTUSANGULO\nTRIANGULO ISOSCELES")
        else:
             print("TRIANGULO OBTUSANGULO")
    elif c**2 < a**2 + b**2:
        if a == b or a == c or c == b:
            print("TRIANGULO ACUTANGULO\nTRIANGULO ISOSCELES")
        else:
            print("TRIANGULO ACUTANGULO")
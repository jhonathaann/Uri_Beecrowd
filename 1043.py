A,B,C = map(float,input().split())

if A < (B + C) and A > abs(B - C) and B < (A + C) and B > abs(A - C) and C < (A + B) and C > abs(A - B):
    perimetro = + A + B + C
    print(f"Perimetro = {perimetro:.1f}")
else:
    areaTrapezio = ((A + B)* C) / 2
    print(f"Area = {areaTrapezio:.1f}")
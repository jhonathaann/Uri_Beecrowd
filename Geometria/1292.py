import math

while True:
    try:
        lado_pentagono = float(input()) # le o lado do quadrado
        
        seno_108 = math.sin(math.radians(108)) # angulo interno do pentagono regular = 108 graus
        seno_63 = math.sin(math.radians(63)) # angulo resultante no ponto de toque (C) (180 - 108 - 9)

        # lei dos senos: X / sin(108) = L / sin(63)
        # X = L * sin(108) / sin(63)
        lado_quadrado = lado_pentagono * (seno_108 / seno_63)
        
        print(f"{lado_quadrado:.10f}")

    except EOFError:
        break
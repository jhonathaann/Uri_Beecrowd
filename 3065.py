N = int(input())
casos = 1
inicio = 0
resultado = 0
aux = "+++"

while N != 0:
    expressao = input()

    print(f"Teste {casos}")

    if "+" not in expressao and "-" not in expressao:
        resultado += int(expressao)
    elif "+" not in expressao[1:] and "-" not in expressao[1:]:
        resultado += int(expressao)
        
    for i in range(1,len(expressao)):
        if expressao[i] == "+":
            resultado += int(expressao[inicio:i])
            inicio = i
            aux = expressao[i:]

        elif expressao[i] == "-":
            resultado += int(expressao[inicio:i])
            inicio = i
            aux = expressao[i:]

        if "+" not in aux[1:] and "-" not in aux[1:]:
            resultado += int(aux)
            aux = expressao
            inicio = 0
    
    print(resultado)
    print()
    resultado = 0
    casos += 1

    N = int(input())
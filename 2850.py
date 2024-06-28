while True:
    try:
        texto = input()

        if texto == "esquerda":
            print("ingles")

        elif texto == "direita":
            print("frances")

        elif texto == "nenhuma":
            print("portugues")

        elif texto == "as duas":
            print("caiu")

    except:
        break

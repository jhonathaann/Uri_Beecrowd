# resposta --> numero de movimentos = numero de areasta unicas * 2

T = int(input()) # numero de grafos da entrada

for i in range(T):
    vertice_origem = int(input())

    # quant de verticces e quant de arestas
    v, a = map(int, input().split())

    # criando o conjunto para guardar as arestas unicas
    arestas_unicas = set()

    # numero de linhas lidas agr = numero de arestas informado
    for i in range(a):
        vertice1, vertice2 = map(int, input().split())

        # ordenando para garantir que (1,0) seja igual a (0,1)
        if(vertice1 < vertice2):
            arestas_unicas.add((vertice1, vertice2))
        else:
            arestas_unicas.add((vertice2, vertice1))
        
    print(len(arestas_unicas) * 2)
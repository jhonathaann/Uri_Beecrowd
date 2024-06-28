horaI,horaF = map(int,input().split())

termino = 0

if horaI < horaF:
    for i in range((horaF - horaI)):
        termino += 1
    print(f"O JOGO DUROU {termino} HORA(S)")
elif horaI > horaF:
    diferença = 24 - horaI
    for i in range(diferença):
        termino += 1
    termino += horaF    
    print(f"O JOGO DUROU {termino} HORA(S)")
else:
    print("O JOGO DUROU 24 HORA(S)")
horaI,minutoI,horaF,minutoF = map(int,input().split())
      
if horaI < horaF:
    totalMinutos = (horaF*60 + minutoF) - (horaI*60 + minutoI)
    novaHora = totalMinutos // 60
    novoMinuto = totalMinutos % 60
    print(f"O JOGO DUROU {novaHora} HORA(S) E {novoMinuto} MINUTO(S)")

elif horaI == horaF and minutoI == minutoF:
    print(f"O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")

elif horaI == horaF and minutoI < minutoF:
    novoMinuto = minutoF - minutoI
    print(f"O JOGO DUROU 0 HORA(S) E {novoMinuto} MINUTO(S)")

else:
    totalMinutos = ((horaF*60 + minutoF) + 1440) - (horaI*60 + minutoI)
    novaHora = totalMinutos // 60
    novoMinuto = totalMinutos % 60
    print(f"O JOGO DUROU {novaHora} HORA(S) E {novoMinuto} MINUTO(S)")

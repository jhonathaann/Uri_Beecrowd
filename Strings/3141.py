nome = input()
diaAtual,mesAtual,anoAtual = map(int,input().split("/"))
diaNasc,mesNasc,anoNasc = map(int,input().split("/"))

dataAtual = diaAtual + mesAtual*30 + anoAtual*365
dataNasc = diaNasc + mesNasc*30 + anoNasc*365
idade = (dataAtual - dataNasc)//365

if diaAtual == diaNasc and mesAtual == mesNasc:
    print("Feliz aniversario!")
    print(f"Voce tem {idade} anos {nome}.")
else:
    print(f"Voce tem {idade} anos {nome}.")
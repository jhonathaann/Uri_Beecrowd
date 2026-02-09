quantPalavras = int(input())


for repetiçoes in range(quantPalavras):
        palavraCrip = ""
        palavraInv = ""
        palavra = input()

        for i in range(len(palavra)):
                if palavra[i].isalpha() == True:
                        letraBin = ord(palavra[i]) + 3
                        letraBin = chr(letraBin)
                        palavraCrip += letraBin
                else: 
                        palavraCrip += palavra[i]

        
        palavraInv = palavraCrip[::-1]
	

        indice = int(len(palavraInv)/2)
        palavraInv2 = palavraInv[indice:]
        palavraInv3 = palavraInv[:indice]
	
        palavraFinal = ""
	
        for k in range(len(palavraInv2)):
            letraBin2 = ord(palavraInv2[k]) -1
            letraBin2 = chr(letraBin2)
            palavraFinal += letraBin2
		
            palavraFINAL = palavraInv3 + palavraFinal	


        print(palavraFINAL)
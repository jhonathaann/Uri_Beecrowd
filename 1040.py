n1,n2,n3,n4 = map(float,input().split())

media = (n1*2 +n2*3 + n3*4 + n4)/(10)

if media >= 7:
	print(f"Media: {media:.1f}\nAluno aprovado.")
elif media < 5:
	print(f"Media: {media:.1f}\nAluno reprovado.")
else:
	print(f"Media: {media:.1f}\nAluno em exame.")
	notaExame = float(input())
	novaMedia = (notaExame + media)/2
	if novaMedia >= 5:
		print(f"Nota do exame: {notaExame:.1f}\nAluno aprovado.\nMedia final: {novaMedia:.1f}")
	else:
		print(f"Aluno reprovado.\nMedia final: {novaMedia:.1f}")
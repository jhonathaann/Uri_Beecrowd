salario = float(input())

if 0 <= salario and salario <= 400.00:
    novoSal = salario * 1.15
    reajSal = salario * 0.15
    print(f"Novo salario: {novoSal:.2f}")
    print(f"Reajuste ganho: {reajSal:.2f}")
    print("Em percentual: 15 %")
elif 400.01 <= salario and salario <= 800.00:
    novoSal = salario * 1.12
    reajSal = salario * 0.12
    print(f"Novo salario: {novoSal:.2f}")
    print(f"Reajuste ganho: {reajSal:.2f}")
    print("Em percentual: 12 %")
elif 800.01 <= salario and salario <= 1200.00:
    novoSal = salario * 1.10
    reajSal = salario * 0.10
    print(f"Novo salario: {novoSal:.2f}")
    print(f"Reajuste ganho: {reajSal:.2f}")
    print("Em percentual: 10 %")
elif 1200.00 <= salario and salario <= 2000.00:
    novoSal = salario * 1.07
    reajSal = salario * 0.07
    print(f"Novo salario: {novoSal:.2f}")
    print(f"Reajuste ganho: {reajSal:.2f}")
    print("Em percentual: 7 %")
else:
    novoSal = salario * 1.04
    reajSal = salario * 0.04
    print(f"Novo salario: {novoSal:.2f}")
    print(f"Reajuste ganho: {reajSal:.2f}")
    print("Em percentual: 4 %")
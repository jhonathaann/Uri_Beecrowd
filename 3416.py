estudantes,litros,consumoMILI = map(int,input().split())
consumoMinimo = litros

consumoL = (estudantes * consumoMILI) / 1000

if consumoL <= litros:
    print(consumoMinimo)
else:
    while consumoL > litros:
        consumoMinimo += litros
        consumoL -= litros
    print(consumoMinimo)
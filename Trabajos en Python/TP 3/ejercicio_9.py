pesos=float(input("Ingrese la cantidad de pesos argentinos: "))
dolares=pesos*80.5
reales=pesos*14.1
euros=pesos*69.5
print(f"Usted tiene ${pesos} pesos argentinos, los cuales se convierten en:")
print(f"-U${dolares} dólares")
print(f"-R${reales} reales")
print(f"-€{euros} euros")
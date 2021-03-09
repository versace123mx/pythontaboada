numero = int(input("Ingresa un numero: "))

if numero > 0:
    print(f"El numero {numero} es positivo.")
else:
    if numero < 0:
        print(f"El numero {numero} es negativo.")
    else:
        print(f"El numero {numero} no es positivo ni negativo.")
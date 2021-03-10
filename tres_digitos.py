num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa otro numero: "))
num3 = int(input("Ingresa otro numero: "))

if num1 > num2 and num1 > num3:
    print(f"El numero {num1} es mayor.")
elif num2 > num1 and num2 > num3:
    print(f"El numero {num2} es mayor.")
elif num3 > num1 and num3 > num2:
    print(f"El numero {num3} es mayor.")
else:
    print("Ninguno de los numeros cumple con las condiciones.")
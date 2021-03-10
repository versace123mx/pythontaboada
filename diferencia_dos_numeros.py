num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa otro numero: "))

if num1 > num2:
    print(f"El numero {num1} es mayor que {num2}")
elif num1 < num2:
    print(f"El numero {num2} es mayor que {num1}")
else:
    print(f"Los numeros {num1} y {num2} son iguales")
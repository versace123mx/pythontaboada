num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa otro numero: "))

if num1 % 2 == 0 and num2 % 2 == 0:

    print("Los numero ingresados son pares")

elif num1 % 2 == 0:

    print(f"El numero {num1} es par")

elif num2 % 2 == 0:

    print(f"El numero {num2} es par")

else:

    print("Ninguno de los numeros es par")
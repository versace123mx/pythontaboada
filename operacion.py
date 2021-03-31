num1 = float(input("Ingresa un numero: "))
num2 = float(input("Ingresa otro numero: "))
operacion = input("Inserta una s para suma, r para resta, m para multiplicacion, d para divicion: ").lower()

if operacion == 's':

    print("La suma es: ",num1 + num2)

elif operacion == 'r':

    print("La resta es: ",num1 - num2)

elif operacion == 'm':

    print("La multiplicacion es: ",num1 * num2)

elif operacion == 'd':

    print("La divicion es: ",num1 / num2)

else:

    print("No hay coincidencias en el tipo de operacion")
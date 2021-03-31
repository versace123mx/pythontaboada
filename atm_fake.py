print("\n\t..::Cajero ATM FAKE::..\n")
menu = int(input("Seleccona una opccion\n"
             "1) Ingresar dinero a la cuenta\n"
             "2) Retirar dinero de la cuenta\n"
             "3) Mostrar dinero disponible\n"
             "4) Salir\n"))
money = 1000

if menu == 1:

    insertMoney = float(input("Ingresa el monto a almacenar: "))
    money += insertMoney
    print("Ahora tienes: ", money)

elif menu == 2:

    retryMoney = float(input("Ingresa el monto a retirar: "))

    if retryMoney > money:
        print("No puedes retirar ese monto, ya que tu saldo es menor.")
    else:
        money -= retryMoney
        print("Ahora tienes: ", money)

elif menu == 3:

    print("Tu dinero disponible es: ", money)

elif menu == 4:

    print("Gracias por vicitar Cajeros ATM Fake")

else:

    print("Opccion Invalida")
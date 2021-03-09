totalcompra = float(input("Ingresa el monto total de la compra: "))
totalcompra = totalcompra - ( totalcompra *.15 )
print(f"El monto total menos descuento del 15%: ${totalcompra:.2f}")
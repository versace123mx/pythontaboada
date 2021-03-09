import math

radio = float(input("Ingresa radio: "))
area = math.pi * math.pow(radio, 2)
longitud = 2 * math.pi * radio
print(f"El area es: {area:.2f}")
print(f"El radio es: {longitud:.2f}")
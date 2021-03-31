'''
las listas son como un array
'''
lista = ["Lunes","Martes","Miercoles","jueves","Viernes","Sabado","Domingo"]

print(lista)
print(lista[0])
print(lista[0:3])
print(lista[2:])

print(len(lista))

########################################################################################
#insertar un elemento al final de la lista
listas2 = [1,2,3,4,5]
print(listas2)
listas2.append(6)
print(listas2)


########################################################################################
#insertar un elemento en un lugar especifico de la lista
listas3 = [1,2,4,5]
listas3.insert(2,3)
print(listas3)


########################################################################################
#insertar varios elementos en una lista, al final de la lista
listas4 = [1,2,4,5]
listas4.extend([6,7,8,9])
print(listas4)


########################################################################################
#unir dos listas
listas5 = [1,2,4,5]
listas6 = [6,7,8,9]
listas7 = listas5 + listas6
print(listas7)

########################################################################################
#buscar un elemento dentro de la lista
listas8 = [1,2,4,5]
print(3 in listas8)

########################################################################################
#buscar un indice de algun elemento
listas9 = [1,2,4,5]
print(listas9.index(2))

########################################################################################
#buscar numero de coincidencias
listas10 = [1,2,4,5,1,2,3,4,1]
print(listas10.count(1))

########################################################################################
#eliminar el ultimo elemento de la lista
listas11 = [1,2,4,5,1,2,3,4,1]
print(listas11.pop())

########################################################################################
#eliminar un indice especifico de la lista
listas12 = [1,2,4,5,1,2,3,4,1]
print(listas12.pop(3))

########################################################################################
#eliminar un elemento sin saber el indice
listas13 = [1,2,4,5,1,2,3,4,1]
listas13.remove(2)
print(listas13)

########################################################################################
#eliminar comletamente la lista
listas14 = [1,2,4,5,1,2,3,4,1]
listas14.clear()
print(listas14)


########################################################################################
#lista ordenada a la inverza
listas15 = [1,2,4,5]
listas15.reverse()
print(listas15)


########################################################################################
#lista duplicada
listas16 = [1,2,4,5] * 3
print(listas16)


########################################################################################
#ordernar lista acendente
listas17 = [1,9,8,4,5,12,7,2]
listas17.sort()
print(listas17)

########################################################################################
#ordernar lista descendente
listas18 = [1,9,8,4,5,12,7,2]
listas18.sort( reverse=True )
print(listas18)
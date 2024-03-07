# PROBLEMA 10


lista1= input("Ingrese una lista de mínimo 6 elementos separados por espacios: ")
lista2 = lista1.split()

if len(lista2)>= 6:
    lista2.remove(lista2[0]) 
    lista2.remove(lista2[3])
    lista2.remove(lista2[3])  

    print(lista2)
else:
    print("inserte una lista con más de 5 elementos")
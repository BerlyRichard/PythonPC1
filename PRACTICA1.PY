# PROBLEMA 1

nombre=input('Por favor ingrese su nombre de usuario: ')
print(f'¡Hola {nombre}!')

#PROBLEMA 2

consumo=float(input('¿Cuánto fue su consumo en el restaurante? '))
porcentaje_propina=float(input('¿Qué porcentaje de propina desea dejar? '))
propina=consumo * (porcentaje_propina/100)
print('Usted debe dejar',propina,'dolares de propina')

# PROBLEMA 3

payasos= int(input('Ingrese el número de payasos vendidos: '))*112
muñecas= int(input('Ingrese el número de muñecas vendidas: '))*75
paquete=payasos+muñecas
print('El peso total del paquete enviado es de',paquete,'g')

# PROBLEMA 4

N= int(input('Ingrese un número entero positivo: '))
suma=int((N*(N+1))/2)
print('La suma de los',N,'primeros enteros positivos es:',suma)

# PROBLEMA 5

shows=int(input('¿Cuántos shows musicales ha visto en el último año? '))
if shows>3:
    print(True)
else:
    print(False)

#PROBLEMA 6

edad = float(input('¿Cual es la edad del cliente?'))
if edad<4:
    precio=0
elif edad<=18:
    precio=5
elif edad>18:
    precio=10
print('El precio de la entrada es $',precio)

# PROBLEMA 7

numero1=float(input('Ingrese un número:'))
numero2=float(input('Ingrese otro número:'))
respuesta=int(input("""Elija una opción (1 / 2 / 3):
                1. Mostrar suma
                2. Mostrar resta
                3. Mostrar multiplicación 
                   """))
if respuesta == 1:
    print('La suma de los números es',numero1+numero2)
elif respuesta ==2:
    print('La resta de los números es',numero1-numero2)
elif respuesta ==3:
    print('La multiplicación de los números es',numero1*numero2)
else:
    print('La opción ingresada es incorrecta')

# PROBLEMA 8

time = input("Por favor ingresa la hora en formato de 24 horas HH:MM : ")

horas,minutos= time.split(":")
horas= int(horas)
minutos= int(minutos)
if 7 <= horas <= 8:
        print("Es hora del desayuno.")
elif 12 <= horas <= 13:
        print("Es hora del almuerzo.")
elif 18 <= horas <= 19:
        print( "Es hora de la cena.")
else:
         None

# PROBLEMA 9

lista1= input("Ingrese una lista de elementos separados por espacios: ")
lista2 = lista1.split()
lista2.reverse()

print(lista2)

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

# PROBLEMA 11

lista_original = [1, 1, 2, 3, 4, 4, 5, 1]
lista_procesada = list(set(lista_original))
print(lista_procesada)
list()

# PROBLEMA 12

diccionario_mime = {
        'gif': 'image/gif',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'pdf': 'application/pdf',
        'txt': 'text/plain',
        'zip': 'application/zip'
    }
nombre_archivo = input("Ingrese nombre del archivo: ").lower()
extrae = nombre_archivo.split(".")
if len(extrae)>1:
    extension_archivo= extrae[-1].lower()

    if extension_archivo in diccionario_mime:
        print(diccionario_mime[extension_archivo])
else:
        print("application/octet-stream")


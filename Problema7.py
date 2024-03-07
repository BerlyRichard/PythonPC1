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
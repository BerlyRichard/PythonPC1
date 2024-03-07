#PROBLEMA 6

edad = float(input('¿Cual es la edad del cliente?'))
if edad<4:
    precio=0
elif edad<=18:
    precio=5
elif edad>18:
    precio=10
print('El precio de la entrada es $',precio)
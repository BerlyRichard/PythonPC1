#PROBLEMA 2

consumo=float(input('¿Cuánto fue su consumo en el restaurante? '))
porcentaje_propina=float(input('¿Qué porcentaje de propina desea dejar? '))
propina=consumo * (porcentaje_propina/100)
print('Usted debe dejar',propina,'dolares de propina')
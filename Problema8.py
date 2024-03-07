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
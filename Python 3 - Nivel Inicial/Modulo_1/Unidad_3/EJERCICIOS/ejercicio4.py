"""
Ejercicio 4
Escriba un programa que solicite la edad de la persona e imprima todos los años que la persona ha cumplido. 
"""

from datetime import datetime

edad = input("Por favor ingrese su edad: \n")
hoy = datetime.now()
año_hoy = hoy.year
año_nacimiento = año_hoy - int(edad)

for year in range(año_nacimiento, año_hoy + 1):
    print(year)

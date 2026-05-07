"""
Ejercicio 3:
Escriba un programa que solicite el
perímetro. Presente el resultado en la terminal del editor.
Utilice la siguiente fórmula:
L = 2 · π · r
L = Longitud de perímetro
π = Número pí igual a 3.1416
r = Radio
"""
radio = int(input(f"Ingrese el radio de la circunferencia\n"))

pi = 3.1416

perimetro = 2 * pi * radio

print(f"El perímetro calculado para el radio ingresado es: {perimetro}")


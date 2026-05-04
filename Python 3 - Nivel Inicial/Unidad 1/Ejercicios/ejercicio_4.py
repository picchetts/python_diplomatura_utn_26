""" Ejercicio 4:
Escriba un programa que solicite el radio de una circunferencia y permita calcular el
área. Presente el resultado en la terminal del editor.
Utilice la siguiente fórmula:
𝐴 = 𝜋. 𝑟ଶ
A = Área
"""

radio = int(input(f"Ingrese el radio de la circunferencia\n"))

pi = 3.1416

area = (pi * radio) ** 2

print(f"El área para una circunferencia  de radio {radio} es: {area}")
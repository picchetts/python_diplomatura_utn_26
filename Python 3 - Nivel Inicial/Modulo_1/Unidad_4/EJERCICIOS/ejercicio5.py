"""
Ejercicio 5 – Dificultad media
Cree un programa que utilizando una función, solicite la edad de la persona e imprima
todos los años que la persona ha cumplido según el siguiente formato de ejemplo.
1, 2, 3, 4, 5
Y
5, 4, 3, 2, 1
"""
def listar_años_de_vida(edad):
    for año in range(int(edad), 0, -1):
        print(2026-año)



print(listar_años_de_vida(input("Por favor ingrese su edad: ")))
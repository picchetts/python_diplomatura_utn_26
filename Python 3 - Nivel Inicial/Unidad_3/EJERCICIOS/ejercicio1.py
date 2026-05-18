"""
Ejercicio 1
Tome el ejercicio de cálculo de números pares e impares de la unidad 2 y
agréguele un bucle al código de forma de simplificarlo. 

"""

import sys
parametro_1 = int(sys.argv[1])
parametro_2 = int(sys.argv[2])


argumentos = sys.argv[1:]
for arg in argumentos:
    if int(arg) % 2 == 0:
        print(f"el parámetro: {arg} ingresado SI es múltiplo de 2")
    else:
        print(f"el parámetro: {arg} ingresado NO es múltiplo de 2")




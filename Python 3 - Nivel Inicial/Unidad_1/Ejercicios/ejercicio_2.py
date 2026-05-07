"""
Ejercicio 2:
Cree un programa que incorpore el módulo sys, al cual desde la terminal se le puedan
pasar tres parámetros. El programa debe tomar los parámetros e indicar en la terminal si
son múltiplos de dos.

"""

import sys
parametro_1 = int(sys.argv[1])
parametro_2 = int(sys.argv[2])

#print(type(parametro_2))

if parametro_1 % 2 == 0:
    print("el primer parámetro ingresados es múltiplo de 2")
else:
    print("el primer parámetro ingresados no es múltiplo de 2")

if parametro_2 % 2 == 0:
    print("el segundo parámetro ingresados es múltiplo de 2")
else:
    print("el segundo parámetro ingresados no es múltiplo de 2")



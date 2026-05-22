"""
Ejercicio 4 – Dificultad alta
Crear una función lambda que tome como parámetro una frase y la escriba al revés.
"""

#frase = input("Escriba una frase para luego mostrala al revés: \n")

frase = "hola"


#for x in range(len(frase)-1, -1, -1):
#    #print(x)
#    print(frase[x])


al_reves = lambda frase: print(frase[range(len(frase)-1, -1, -1)])    #
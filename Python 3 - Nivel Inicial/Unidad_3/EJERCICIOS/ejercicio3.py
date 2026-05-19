"""
Ejercicio 3
Escriba un programa que consulte al usuario por una oración y comente al usuario cuantas veces aparecen todas las vocales considerando minúsculas, mayúsculas y acentos.  
"""
vocales = ("a", "e", "i", "o", "u", "á", "é", "í", "ó","ú")
oracion = input("Por favo ingrese una oración:\n")

hits = []
for caracter in oracion:
    if caracter.lower() in vocales:
        hits.append(caracter)

print(f"En la oración ingresada aparecen {len(hits)} vocales")

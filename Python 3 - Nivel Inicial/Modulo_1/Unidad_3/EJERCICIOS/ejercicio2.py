"""
Ejercicio 2
Escriba un programa que consulte al usuario por una oración y comente al usuario cuantas veces aparece la letra “a”. 
"""
oracion = input("Por favo ingrese una oración:\n")
cantidad = oracion.count("a")

print(f"La letra 'a' aparece {cantidad} veces en l oración '{oracion}'")
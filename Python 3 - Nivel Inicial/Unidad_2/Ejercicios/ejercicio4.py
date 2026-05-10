"""
Ejercicio 4
Realice un programa que consulte la edad y en caso de que el valor ingresado supere la
fecha de jubilación, presente en la terminal el mensaje "Ya esta en edad de jubilarse" en 
caso contrario que presente “Aun está en edad de trabajar"
"""

edad = int(input("Ingrese su edad\n"))
if edad > 64:
    print("Usted ya se encurntra en edad de jubilarse")
else:
    print("A seguir remando!")


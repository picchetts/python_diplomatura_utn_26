"""
Ejercicio 5
Realice nuevamente los ejercicios de la unidad 1 (3, 4 y 5), pero tratando de utilizar una función, de forma que la operación 
se realice dentro de la misma.
Presente el resultado en la terminal del editor
"""

def ejercicio1():
    print("EJERCICIO 1\n Cree un programa que tome tres valores por consola multiplique el primero por el segundo y le sume el tercero. Presente el resultado en la terminal\n")
    variable_1 = int(input("Ingrese el primer valor\n"))
    variable_2 = int(input("Ingrese el segundo valor\n"))
    variable_3 = int(input("Ingrese el tercer valor\n"))

    resultado = variable_1 * variable_2 + variable_3
    print(f"El resultado es: {resultado}")

def ejercicio2():
    print("EJERCICIO 2\n Cree una lista de frutas de 2 elementos, y realice un programa que muestre una oración conteniendo los dos elementos de la lista concatenándolos con texto para formar una oración con sentido. Presente el resultado en la terminal del editor\n")
    frutas = ["naranja", "pomelo"]
    print(f"En invierno, prefiero comer frutas cítricas como {frutas[0]} y {frutas[-1]}.")

def ejercicio3():
    print("EJERCICIO 3:\n Tome dos valores por consola, y guarde en una lista [primer_valor, segundo_valor, la_suma_de_los_valores]. Presente el resultado en la terminal del editor\n")
    primer_valor = int(input("Ingrese el primer valor"))
    segundo_valor = int(input("Ingrese el segundo valor\n"))
    lista_valores = [primer_valor, segundo_valor, primer_valor + segundo_valor]
    print(lista_valores)


def ejercicio4():
    print("EJERCICIO 4\n Realice un programa que consulte la edad y en caso de que el valor ingresado supere la fecha de jubilación, presente en la terminal el  mensaje 'Ya esta en edad de jubilarse' en caso contrario que presente 'Aun está en edad de trabajar'\n")
    edad = int(input("Ingrese su edad\n"))
    if edad > 64:
        print("Usted ya se encurntra en edad de jubilarse")
    else:
        print("A seguir remando!")

ejercicio1()

ejercicio2()

ejercicio3()

ejercicio4
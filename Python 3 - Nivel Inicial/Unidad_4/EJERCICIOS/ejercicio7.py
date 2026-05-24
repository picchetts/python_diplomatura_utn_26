"""
Ejercicio 7 – Dificultad muy alta
isinstance(x, list) permite consultar si el elementos x es del tipo lista.
A partir de la siguiente función recursiva que permite
lista = ["elemento1n1", "elemento2n1", "elemento3n1",
["elemento1n2", "elemento2n2", "elemento3n2",
["elemento1n3", "elemento2n3", "elemento3n3"]]]
def recorre_lista(item):
for x in item:
if isinstance(x, list):
recorrer_lista(x)
else:
print(x)
recorrer_lista(lista)
Optimice el código de forma que el programa considere:
e-Learning SCEU UTN - BA.
/ Fax +54 11 4032 0148
e-learning
la siguiente lista y reordene de menor a mayor sus
recorrer los niveles de una lista:
p. 4
Centro de e
Medrano 951 2do piso (1179) // Tel. +54 11 4867 7589
www.sceu.frba.utn.edu.ar/e
 Un valor de lista por defecto
 Permita tomar un segundo parámetro que lleve un
encuentra (en qué grado del anidamiento)
 Permita tomar un valor por defecto de cero para el parámetro anterior.
 Presente la salida según el siguiente formato:
elemento1n1
elemento2n1
elemento3n1
elemento1n2
elemento2n2
elemento3n2
elemento1n3
elemento2n3
elemento3n3

"""

lista = [
    "elemento1n1", 
    "elemento2n1", 
    "elemento3n1",
    [
        "elemento1n2", 
        "elemento2n2", 
        "elemento3n2",
        [
            "elemento1n3", 
            "elemento2n3", 
            "elemento3n3"
        ]
    ]
]

def recorrer_lista(item, nivel=1):
    for x in item:
        if isinstance(x, list):
            nivel += 1
            recorrer_lista(x, nivel)
        else:
            for i in range(nivel):
                print("\t" * i, end='')
            print(x, f"Nivel: {nivel}")

recorrer_lista(lista)
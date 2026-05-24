"""
Ejercicio 6 – Dificultad alta
Cree una función que tome la siguiente lista y reordene de menor a mayor sus componentes:
[3, 44, 21, 78, 5, 56, 9]
"""


def el_menor(lista):
    el_menor = None    
    for elemento in lista:
        if el_menor == None:
            el_menor = elemento
        else:
            if elemento <=  el_menor:
                el_menor = elemento

    return el_menor
    

lista = [3, 44, 21, 78, 5, 56, 9]
lista_ordenada = []
while len(lista) != 0:
    menor_de_la_lista = el_menor(lista)
    if menor_de_la_lista != None:
        lista_ordenada.append(menor_de_la_lista)
        lista.remove(menor_de_la_lista)

print(lista_ordenada)





            

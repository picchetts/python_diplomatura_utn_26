"""
Ejercicio 7
A partir del ejercicio 5 cree un programa que vaya agregando en un diccionario las compras realizadas.
"""
lista_compras = []
seguir_comprando = "y"

while seguir_comprando != "n":
    tipo_producto, cantidad, precio = input("Ingrese los datos de su compra separados por comas, de la siguiente manera: tipo de producto, cantidad, precio:\n").split(",")
    producto = {"producto": tipo_producto, "cantidad": cantidad, "precio": precio}
    lista_compras.append(producto)
    

    seguir_comprando = input("Si no desea seguir comprando ingrese 'N, sino, ingrese 'Y: \n").lower()

monto_total = 0
for item in lista_compras:
    monto_compra = int(item["cantidad"]) * int(item["precio"])
    monto_total += monto_compra

print(f"Monto total gastado: {monto_total}")
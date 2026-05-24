"""
Ejercicio 6
A partir del ejercicio 5 cree un programa que vaya agregando en una lista las compras realizadas.
"""
lista_compras = []
seguir_comprando = "y"

while seguir_comprando != "n":
    cantidad, precio = input("Ingrese la cantidad de productos comprados y el precio separados por coma:\n").split(",")
    compra = int(cantidad) * int(precio)
    lista_compras.append(compra)
    seguir_comprando = input("Si no desea seguir comprando ingrese 'N, sino, ingrese 'Y: \n").lower()

monto_total = 0
for item in lista_compras:
    monto_total += int(item)

print(f"Monto total gastado: {monto_total}")



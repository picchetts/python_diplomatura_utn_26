"""
Ejercicio 5
Suponga que tiene una verdulería y carga la cantidad y el precio de lo comprado por un cliente. Realice un programa que tome de a uno la cantidad y el precio comprado por el cliente y al finalizar la compra retorne el monto total gastado. 

"""
monto_total = 0
seguir_comprando = "y"

while seguir_comprando != "n":
    cantidad, precio = input("Ingrese la cantidad de productos comprados y el precio separados por coma:\n").split(",")
    compra = int(cantidad) * int(precio)
    monto_total += compra
    seguir_comprando = input("Si no desea seguir comprando ingrese 'N, sino, ingrese 'Y: \n").lower()

print(f"Monto total gastado: {monto_total}")



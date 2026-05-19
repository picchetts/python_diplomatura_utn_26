"""
Ejercicio8
A partir del ejerció 6 cree un programa con 4 funciones:
alta() para dar de alta la nueva compra
baja() para dar de baja una compra
consulta() para consultar por todas las compras realizadas hasta el momento
modificar() para modificar una compra realizada

"""
#lista_compras = []
#seguir_comprando = "y"
#
#while seguir_comprando != "n":
#    cantidad, precio = input("Ingrese la cantidad de productos comprados y el precio separados por coma:\n").split(",")
#    compra = int(cantidad) * int(precio)
#    lista_compras.append(compra)
#    seguir_comprando = input("Si no desea seguir comprando ingrese 'N, sino, ingrese 'Y: \n").lower()
#
#monto_total = 0
#for item in lista_compras:
#    monto_total += int(item)
#
#print(f"Monto total gastado: {monto_total}")


### MODELO ###

lista_compras = []

def alta(cantidad, precio):
    total_compra = int(cantidad) * int(precio)
    lista_compras.append(total_compra)
    print(f"\n ------> Compra agregada al carrito: Precio por unidad: {precio}, Cantidad: {cantidad}")

def baja(id_compra):
    lista_compras.pop(id_compra)
    print(f"\n ------> Compra N° {id_compra} retirada del carrito: Precio por unidad: {precio}, Cantidad: {cantidad}")

def modificacion(id_compra, cantidad, precio):
    total_compra = int(cantidad) * int(precio)
    lista_compras[id_compra] = total_compra
    print(f"\n ------> Compra N° {id_compra} modificada: Precio por unidad: {precio}, Cantidad: {cantidad}, Total: {total_compra}")

def consulta():
    print("\nListando compras en el Carrito...")
    print("##"*15)
    for index in range(0, len(lista_compras)):        
        print(f"Compra N°: {index} | Precio total:{lista_compras[index]}")
    print("##"*15)






### VISTA ###
while True:
    print("--"*40)
    operacion = input("""\nIngrese la operación que desea realizar:
                      - Ingrese 'A' para alta de una nueva compra
                      - Ingrese 'B' para baja de una compra
                      - Ingrese 'C' para consulta de una compra
                      - Ingrese 'M' para modificación de una compra\n
                      """)
    print("--"*40)
    
    ### CONTROLADOR ###
    #Lógica validación de entrada y llamado a funciones Modelo
    if operacion.lower() == "a":
        cantidad, precio = input("Ingrese la cantidad de productos comprados y el precio separados por coma:\n").split(",")
        alta(cantidad, precio)
    elif operacion.lower() == "b":
        baja(int(input("Ingrese el Número Identificador de la compra a retirar del carrito:\n")))
    elif operacion.lower() == "m":
        id_producto = int(input("Ingrese el Id de la compra a modificar:\n"))
        cantidad, precio = input("Ingrese,separados por coma; la cantidad y el precio a modificar en esta compra:\n").split(",")
        modificacion(id_producto, cantidad, precio)
    elif operacion.lower() == "c":
        consulta()





    ### END CONTROLADOR ###
    
    
    
    # Submenú seguir Operando
    print("\n"*2)
    print("**"*30)
    seguir_operando = input("Si desea seguir operando ingrese 'Y, sino, ingrese 'N: \n").lower()
    
    if seguir_operando == "y":
        continue
    elif seguir_operando == "n":
        break
    else: 
        print("Selección incorrecta, volviendo al menú principal \n")










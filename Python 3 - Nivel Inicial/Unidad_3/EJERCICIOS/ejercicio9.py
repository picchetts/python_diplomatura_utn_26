"""
Ejercicio9
A partir del ejerció 7 cree un programa con 4 funciones:
alta() para dar de alta la nueva compra
baja() para dar de baja una compra
consulta() para consultar por todas las compras realizadas hasta el momento
modificar() para modificar una compra realizada

Pregunta: Considera que es más fácil guardar la información en listas o en diccionarios


"""


### MODELO ###

lista_compras = []

def alta(tipo_producto, cantidad, precio):
    compra = {"producto": tipo_producto, "cantidad": cantidad, "precio": precio}
    lista_compras.append(compra)
    print(f"\n ------> Compra agregada al carrito: Producto: {compra['producto']} Precio por unidad: {compra['precio']}, Cantidad: {compra['cantidad']}")

def baja(id_compra):
    lista_compras.pop(id_compra)
    print(f"\n ------> Compra N° {id_compra} retirada del carrito")

def modificacion(id_compra, tipo_producto, cantidad, precio):
    nueva_compra = {"producto": tipo_producto, "cantidad": cantidad, "precio": precio}
    lista_compras[id_compra] = nueva_compra
    print(f"\n ------> Compra N° {id_compra} modificada: Precio por unidad: {nueva_compra['producto']}, Precio por unidad: {nueva_compra['precio']}, Cantidad: {nueva_compra['cantidad']}")

def consulta():
    print("\nListando compras en el Carrito...")
    print("##"*15)
    for index in range(0, len(lista_compras)):        
        print(f"Compra N°: {index} | Tipo Producto:{lista_compras[index]['producto']} | Precio por Unidad:{lista_compras[index]['precio']} | Cantidad:{lista_compras[index]['cantidad']}")
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
        tipo_producto, cantidad, precio = input("Ingrese el tipo de producto, la cantidad y el precio separados por coma:\n").split(",")
        alta(tipo_producto, cantidad, precio)
    elif operacion.lower() == "b":
        baja(int(input("Ingrese el Número Identificador de la compra a retirar del carrito:\n")))
    elif operacion.lower() == "m":
        id_producto = int(input("Ingrese el Id de la compra a modificar:\n"))
        tipo_producto, cantidad, precio = input("Ingrese los datos a modificar en esta compra separados por coma: tipo de producto, cantidad, precio :\n").split(",")
        modificacion(id_producto, tipo_producto, cantidad, precio)
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
        print("Gracias por comprar en Chango Más!!!!")
        break
    else: 
        print("Selección incorrecta, volviendo al menú principal \n")










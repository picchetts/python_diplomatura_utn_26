"""
Escriba un programa que guarde en una variable una contraseña y consulte al usuario por la contraseña hasta que esta sea correcta. El programa debe informar al usuario si la contraseña fue correcta o no.  
"""

while True:
    first_input = input("Por favor ingrese la contraseña por primera vez\n")
    second_input = input("Por favor ingrese la contraseña por primera vez\n")
    if second_input == first_input:
        print("Las contraseñas coinciden!!!!!")
        break
    else:
        print("Las contraseñas coinciden.. Por favor intentelo de nuevo")
        
from tkinter import *

#CREACION VENTANA
root = Tk()
# **********************************
#Defino Objetos Tkinter

#Pack de tipo campo de entrada. Se parace a otro elemento campo de entrada llamado Grid. Grid que es una grilla fija de elementos
# Pack permite mover el campo
entrada_numerica = Entry(root)
entrada_numerica.pack()

entrada_texto = Entry(root)
entrada_texto.pack()

# **********************************
#Logica Python
a = 4
b = 5
c = a + b
d = f"Mi resultado es: {str(c)}"

#Defino variables Tkinter
# **********************************
#IntVar() --> Tipo de Dato Entero de Tkinter
#BoolVar() --> Tipo de Dato Booleano de Tkinter
#StringVar() --> Tipo de Dato String de Tkinter
int_var = IntVar()
string_var = StringVar()

# **********************************
#Mapeo Objetos a Variables Tkinter
#Configuro campo de entrada con variable (la variable puede obtener o setear valores del campo de entrada)
entrada_numerica.config(textvariable=int_var)
entrada_texto.config(textvariable=string_var)

# **********************************
#Hago Get/Set de variables en Obj Tkinter
int_var.set(c)
string_var.set(d)

# **********************************
#CIERRE VENTANA
root.mainloop()
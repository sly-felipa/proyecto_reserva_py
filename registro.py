from tkinter import *
import sqlite3
import datetime
import re

#genera la ventana
raiz = Tk()

#variable
nombre = StringVar()
apellido = StringVar()
usuario = StringVar()
password = StringVar()
rePassword = StringVar()
email = StringVar()
listaVerificacion = []
validacionOK = None
matchLetras = '^[a-z\sáéíóúñ]+$'
matchAlfanumerico = '^[a-z0-9]+$'
matchPass = '[^\s]$'
matchEmail = '^[a-zA-Z0-9\._-]+@[a-zA-Z0-9-]{2,}[.][a-zA-Z]{2,4}$'

def run():

    global listaVerificacion
    listaVerificacion.append(validarDatos(nombre.get(),matchLetras))
    listaVerificacion.append(validarDatos(apellido.get(),matchLetras))
    listaVerificacion.append(validarDatos(usuario.get(),matchAlfanumerico))
    listaVerificacion.append(validarDatos(password.get(),matchPass))
    listaVerificacion.append(validarDatos(rePassword.get(),matchPass))
    listaVerificacion.append(validarDatos(email.get(),matchEmail))

# se verifica que todos los elementos de listaVerificacion sean True
    verfificarValidacion()

# se agrega el usuario nuevo a la BBDD
    agregarFilaBBDD()


def validarDatos(datoIngresado, match):

    if re.search(match,datoIngresado,re.I) is not None:
        print("Usuario correcto! " + datoIngresado)
        ingresoCorrecto = True
    else:
        print("Usuario incorrecto! " + datoIngresado)
        ingresoCorrecto =False
    
    return ingresoCorrecto

def verfificarValidacion():

    global validacionOK

    if False in listaVerificacion:
        validacionOK = False
    else:
        validacionOK = True

def agregarFilaBBDD():

# establacer conexión
    conexion = sqlite3.connect("./sqlite3/bbdd.sql")

# seleccionar cursor para realizar la consulta
    consulta = conexion.cursor()

    datos = (usuario.get(), nombre.get(), apellido.get(), password.get(), datetime.date.today(), email.get())
    usuarioNuevoBBDD = """
    INSERT INTO usuario values (?, ?, ?, ?, ?, ?)""" 
    # usuarioNuevoBBDD = """
    # INSERT INTO usuario values ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')""" .format(usuario.get(), nombre.get(), apellido.get(), password.get(), datetime.date.today())

    if consulta.execute(usuarioNuevoBBDD, datos):
        print("ingreso correcto")
        conexion.commit()
    else:
        print("Error en la consulta a la BBDD")

    consulta.close()
    conexion.close()

    return None
    
# raiz.geometry("650x350")

raiz.title("Registro")

raiz.resizable(0,0)

# raiz.iconbitmap("") ruta

# crear frame, agregar a la raiz
frameMain = Frame(raiz, width="650",height="350")

# empaquetar frame dentro de la raiz, se expande x/y
frameMain.pack(fill="both", expand="true")

# frameMain.config(bg="blue")

labelCampoObligatorio = Label(frameMain, fg="gray", text="* campos obligatorios")
labelCampoObligatorio.grid(row=0,column=2, pady=10, padx=10)

# nombre
labelNombre = Label(frameMain, text="Nombre *", font=(12))
labelNombre.grid(row=1,column=0, sticky="w", pady=10, padx=10)

campoNombre = Entry(frameMain, justify=CENTER, textvariable=nombre)
campoNombre.grid(row=1,column=1, padx=10)

labelNombreObligatorio = Label(frameMain, fg="red", text="Campo obligatorio!")
labelNombreObligatorio.grid(row=1,column=2, sticky="w", pady=10, padx=15)
labelNombreObligatorio.grid_remove()

# apellido
labelApellido = Label(frameMain, text="Apellido *", font=(12))
labelApellido.grid(row=2,column=0, sticky="w", pady=10, padx=10)

campoApellido = Entry(frameMain, justify=CENTER, textvariable=apellido)
campoApellido.grid(row=2,column=1, padx=10)

labelApellidoObligatorio = Label(frameMain, fg="red", text="Campo obligatorio!")
labelApellidoObligatorio.grid(row=2,column=2, sticky="w", pady=10, padx=15)
labelApellidoObligatorio.grid_remove()

# usuario
labelUsuario = Label(frameMain, text="Usuario *", font=(12))
labelUsuario.grid(row=3,column=0, sticky="w", pady=10, padx=10)

campoUsuario = Entry(frameMain, justify=CENTER, textvariable=usuario)
campoUsuario.grid(row=3,column=1, padx=10)

labelUsuarioObligatorio = Label(frameMain, fg="red", text="Campo obligatorio!")
labelUsuarioObligatorio.grid(row=3,column=2, sticky="w", pady=10, padx=15)
labelUsuarioObligatorio.grid_remove()

# pass
labelPassword = Label(frameMain, text="Contraseña *", font=(12))
labelPassword.grid(row=4,column=0, sticky="w", pady=10, padx=10)

campoPassword = Entry(frameMain,  justify=CENTER, textvariable=password)
campoPassword.grid(row=4,column=1, padx=10)
campoPassword.config(show="*")

labelPasswordObligatorio = Label(frameMain, fg="red", text="Campo obligatorio!") # verificar contraseña
labelPasswordObligatorio.grid(row=4,column=2, sticky="w", pady=10, padx=15)
labelPasswordObligatorio.grid_remove()

# re pass
labelRepassword = Label(frameMain, text="Reingresa la contraseña *", font=(12))
labelRepassword.grid(row=5,column=0, sticky="w", pady=10, padx=10)

campoRepassword = Entry(frameMain,  justify=CENTER, textvariable=rePassword)
campoRepassword.grid(row=5,column=1, padx=10)
campoRepassword.config(show="*")

labelRepasswordObligatorio = Label(frameMain, fg="red", text="Campo obligatorio!")
labelRepasswordObligatorio.grid(row=5,column=2, sticky="w", pady=10, padx=15)
labelRepasswordObligatorio.grid_remove()

# email
labelEmail = Label(frameMain, text="Email *",  font=(12))
labelEmail.grid(row=6,column=0, sticky="w", pady=10, padx=10)

campoEmail = Entry(frameMain, justify=CENTER, textvariable=email)
campoEmail.grid(row=6,column=1, padx=10)

labelEmailObligatorio = Label(frameMain, fg="red", text="Campo obligatorio!")
labelEmailObligatorio.grid(row=6,column=2, sticky="w", pady=10, padx=15)
labelEmailObligatorio.grid_remove()

# botón
botonRegistro= Button(frameMain, text="Registrarse", command=lambda:run())
botonRegistro.grid(row=7,column=1,sticky="s", pady=10, padx=1, ipady=5, ipadx=5)






# obligatorio para que aparezca
raiz.mainloop()


from tkinter import *
import sqlite3

#genera la ventana
raiz = Tk()

#variable
nombre = StringVar()
apellido = StringVar()
usuario = StringVar()
password = StringVar()
rePassword = StringVar()
email = StringVar()
validacionDatos = None

def verificarDatosIngresados():
    x = None
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
botonRegistro= Button(frameMain, text="Registrarse", command=lambda:verificarDatosIngresados())
botonRegistro.grid(row=7,column=1,sticky="s", pady=10, padx=1)






# obligatorio para que aparezca
raiz.mainloop()


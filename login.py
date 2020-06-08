from tkinter import *
import sqlite3

#genera la ventana
raiz = Tk()

#variable
usuario = StringVar()
password = StringVar()
validacionDatos = None

def verificarDatosIngresados():

# establacer conexión
    conexion = sqlite3.connect("./sqlite3/bbdd.sql")

# seleccionar cursor para realizar la consulta
    consulta = conexion.cursor()
    # sql = "select * from usuario where nombre_usuario={0} and contraseña={1}" .format(usuario.get(), password.get()) 

    buscarUsuario = True
    buscarPassword = True

    if consulta.execute("select * from usuario"):
        # fila = consulta.fetchone()
        filas = consulta.fetchall()
        for fila in filas:
            # print(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
            if fila[0] == usuario.get() and buscarUsuario == True:
                print("usuario - ok")
                buscarUsuario = False
                if fila[3] == password.get() and buscarPassword == True:
                    buscarPassword = False
                    validacionDatos = True
                    print("pass - ok")
    else:
        print("Error en la consulta a la BBDD")
    
    if buscarUsuario == True:
        print("Usuario incorrecto")
        validacionDatos = False
        campoUsuario.delete(0, 'end')

    if buscarPassword == True:
        print("Password incorrecto")
        campoPassword.delete(0, 'end')

    # if fila is None:

    consulta.close()
    conexion.close()

    cerrarVentanaLogin(validacionDatos)

def cerrarVentanaLogin(validacion):

    if validacion == True:
       print("salir")
       # llama a la ventana reservas
       raiz.quit()
    else:
         print("no salir")




# raiz.geometry("650x350")

raiz.title("Login")

# raiz.resizable(0,0)

# raiz.iconbitmap("") ruta

# crear frame, agregar a la raiz
frameMain = Frame(raiz, width="650",height="350")

# empaquetar frame dentro de la raiz, se expande x/y
frameMain.pack(fill="both", expand="true")

# frameMain.config(bg="blue")

labelUsuario = Label(frameMain, text="Usuario", fg="red", font=(12))
labelUsuario.grid(row=0,column=0, sticky="w", pady=4, padx=4)

campoUsuario = Entry(frameMain, justify=CENTER, textvariable=usuario)
campoUsuario.grid(row=0,column=1, padx=10)

labelPassword = Label(frameMain, text="Contraseña",fg="red", font=(12))
labelPassword.grid(row=1,column=0, sticky="w", pady=4, padx=4)

campoPassword = Entry(frameMain,  justify=CENTER, textvariable=password)
campoPassword.grid(row=1,column=1, padx=10)
campoPassword.config(show="*")

botonLogin = Button(frameMain, text="Login", command=lambda:verificarDatosIngresados())
botonLogin.grid(row=2,column=0,sticky="e", pady=4,padx=1)

botonRegistro= Button(frameMain, text="Registrarse", command=raiz.quit)
botonRegistro.grid(row=2,column=1,sticky="s", pady=4, padx=1)






# obligatorio para que aparezca
raiz.mainloop()


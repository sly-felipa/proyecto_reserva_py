from tkinter import *
import sqlite3

#genera la ventana
raiz = Tk()

#variable
usuario = StringVar()
password = StringVar()
verificacion=True

def verificarDatosIngresados():

    global verificacion
# establacer conexión
    conexion = sqlite3.connect("./sqlite3/bbdd.sql")

# seleccionar cursor para realizar la consulta
    consulta = conexion.cursor()

    sql = "select * from usuario where nombre_usuario={0} and contraseña={1}" .format(usuario.get(), password.get()) 

    consulta.execute(sql)

    fila = consulta.fetchone()
        # print(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
    if fila is None:
        print(fila)
        print('Verifica los datos ingresados.')
    else:
        print(fila)
        print('Ingreso correcto!')
  
    consulta.close()
    conexion.commit()
    conexion.close()


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

# botonLogin = Button(frameMain, text="Login")
botonLogin = Button(frameMain, text="Login", command=lambda:verificarDatosIngresados())
botonLogin.grid(row=2,column=0,sticky="e", pady=4,padx=1)

botonRegistro= Button(frameMain, text="Registrarse", command=raiz.quit)
botonRegistro.grid(row=2,column=1,sticky="s", pady=4, padx=1)





# obligatorio para que aparezca
raiz.mainloop()


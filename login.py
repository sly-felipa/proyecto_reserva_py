from tkinter import *

#genera la ventana
raiz = Tk()

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

campoUsuario = Entry(frameMain)
campoUsuario.grid(row=0,column=1, padx=10)

labelPassword = Label(frameMain, text="Contraseña",fg="red", font=(12))
labelPassword.grid(row=1,column=0, sticky="w", pady=4, padx=4)

campoPassword = Entry(frameMain)
campoPassword.grid(row=1,column=1, padx=10)
campoPassword.config(show="*")

# botonLogin = Button(frameMain, text="Login")
botonLogin = Button(frameMain, text="Login", command=raiz.quit)
botonLogin.grid(row=2,column=0,sticky="news", pady=4,padx=1)

botonRegistro= Button(frameMain, text="Registrarse", command=raiz.quit)
botonRegistro.grid(row=2,column=1,sticky="news", pady=4, padx=1)




# obligatorio para que aparezca
raiz.mainloop()


from tkinter import ttk
import tkinter

root = tkinter.Tk()

btn = ttk.Style().configure("TButton", padding=6, relief="flat",
   background="red")

btn = ttk.Entry(text="Sample")
btn.pack()

root.mainloop()
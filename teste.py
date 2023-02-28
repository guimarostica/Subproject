import tkinter as tk
import ttkbootstrap as ttkb

root = tk.Tk()

var = tk.DoubleVar() # Criando uma variável para armazenar o valor do Spinbox

def increment_spinbox():
    var.set(var.get() + 0.1) # Incrementando o valor da variável em 0,1

spinbox = ttkb.Spinbox(root, from_=0, to=1, textvariable=var, format='%.1f')
spinbox.pack()

button = ttkb.Button(root, text="Incrementar", command=increment_spinbox)
button.pack()

root.mainloop()
import tkinter as tk
from tkinter import Tk, Menu
from tkinter.ttk import Treeview
from ttkbootstrap import Style

root = Tk()
style = Style(theme='cosmo')

treeview = Treeview(root)
treeview.insert('', 'end', text='Parent 1')
treeview.insert('', 'end', text='Parent 2')

def right_click(event):
    item_id = treeview.identify_row(event.y)
    if item_id:
        menu.post(event.x_root, event.y_root)

def add_child():
    parent_id = treeview.focus()
    name = f'Child {len(treeview.get_children(parent_id)) + 1}'
    treeview.insert(parent_id, 'end', text=name)

def delete():
     # Seleciona o item atual
    item_selecionado = treeview.focus()
    # Remove o item atual do treeview
    treeview.delete(item_selecionado)


def abrir_janela(event):
    # Seleciona o item atual
    item_selecionado = treeview.focus()
    # Obtém os valores do item selecionado
    values = treeview.item(item_selecionado)['values']
    # Cria a janela separada
    window = tk.Toplevel(root)
    window.title(f'Item {values[0]}')
    # Adiciona um rótulo com as informações do item selecionado
    tk.Label(window, text=f'Nome: {values[1]}').pack()
    tk.Label(window, text=f'Telefone: {values[2]}').pack()

treeview.bind('<Button-3>', right_click)
treeview.bind('<Double-Button-1>', abrir_janela)

menu = Menu(root, tearoff=0)
menu.add_command(label='New', command=lambda: add_child())
menu.add_command(label='Import', command=lambda: delete())
menu.add_command(label='Delete', command=lambda: delete())

treeview.pack()
root.mainloop()
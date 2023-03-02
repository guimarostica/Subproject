import subprocess
import tkinter as tk
from tkinter import messagebox

def set_network():
    ssid = ssid_entry.get()
    password = password_entry.get()
    
    # Configure o SSID e a senha do WiFi
    command = ['netsh', 'wlan', 'set', 'profileparameter', 'name="{}"'.format(ssid), 'keyMaterial="{}"'.format(password)]
    output = subprocess.check_output(command)
    
    # Mensagem de confirmação
    messagebox.showinfo(title="Configuração Concluída", message="A rede foi configurada com sucesso!")
    
    # Debug output
    print(output.decode())

# Criação da janela principal
window = tk.Tk()
window.title("Configuração de Rede")

# Criação dos campos de entrada
tk.Label(window, text="SSID:").grid(row=0, column=0, sticky="w")
ssid_entry = tk.Entry(window)
ssid_entry.grid(row=0, column=1)

tk.Label(window, text="Senha:").grid(row=1, column=0, sticky="w")
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=1, column=1)

# Botão de configuração
tk.Button(window, text="Configurar Rede", command=set_network).grid(row=2, column=0, columnspan=2)

window.mainloop()
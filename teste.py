from tkinter.filedialog import asksaveasfile, askopenfilename


def save_file():

    f = asksaveasfile(initialfile = 'Untitled.gui',defaultextension=".gui",filetypes=[("Pallet File","*.gui")])
    return f

def open_file():
     # Abre a janela de seleção de arquivo
    caminho_arquivo = askopenfilename(filetypes=[("Arquivos de texto", "*.gui")])
    # Lê o conteúdo do arquivo
    with open(caminho_arquivo, "r") as arquivo:
        conteudo = arquivo.read()
    return conteudo

def create_gui_file(conteudo):
    t = save_file()
   
    t.write(str(conteudo))
   
# Exemplo de variável a ser salva em arquivo
# numero = {}
# numero["Ola"] = (0,2,3,4)
# numero["tudo_bem"] = (0,2,3,5)
# # Salvando o valor da variável em um arquivo de texto
# nome_arquivo = 'numero_salvo.txt'
# create_gui_file(numero)

# Lendo o valor do arquivo e atribuindo a uma nova variável
numero_lido = open_file()

numero_lido = eval(numero_lido)

print(numero_lido["Ola"][2])

# Verificando se o valor lido é o mesmo da variável original
print(numero_lido)
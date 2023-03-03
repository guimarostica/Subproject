from tkinter.filedialog import asksaveasfile, askopenfilename

class Gui_File:

    def save_file(self):
        f = asksaveasfile(initialfile = 'Untitled.gui',defaultextension=".gui",filetypes=[("Pallet File","*.gui")])
        return f

    def open_file(self):
        # Abre a janela de seleção de arquivo
        caminho_arquivo = askopenfilename(filetypes=[("Arquivos de texto", "*.gui")])
        # Lê o conteúdo do arquivo
        with open(caminho_arquivo, "r") as arquivo:
            conteudo = arquivo.read()
        return conteudo

    def create_gui_file(self,box_position, box_orientation):
        t = self.save_file()
    
        t.write(str(box_position) + "\n" + str(box_orientation))
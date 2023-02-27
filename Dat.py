#Aquivo .dat
from tkinter.filedialog import asksaveasfile
from Src import Src_File

class Dat_File:

    src = Src_File()

    def save_file(self):

        f = asksaveasfile(initialfile = 'Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt"),("DAT File","*.dat"),("Source File","*.src")])
        return f
    
    def create_dat_file(self,n_camadas,n_caixas,h,dic):
        rx = "0.0"
        ry = "0.0"
        t = self.save_file()
        intro = ";------------ PALLET AUTOMATION ------------ \n\n\n&ACCESS RV1\nDEFDAT  VARIAVEL PUBLIC\n;FOLD EXTERNAL DECLARATIONS;%{PE}%MKUKATPBASIS,%CEXT,%VCOMMON,%P\n;FOLD BASISTECH EXT;%{PE}%MKUKATPBASIS,%CEXT,%VEXT,%P\nEXT  BAS (BAS_COMMAND  :IN,REAL  :IN )\nDECL INT SUCCESS\n;ENDFOLD (BASISTECH EXT)\n;FOLD USER EXT;%{E}%MKUKATPUSER,%CEXT,%VEXT,%P\n;Make your modifications here\n\n;ENDFOLD (USER EXT)\n;ENDFOLD (EXTERNAL DECLARATIONS)\n\n"
        init = "DECL GLOBAL FRAME POSPEGA["+ str(n_camadas) + "," + str(n_caixas) + "] \n"
        t.write(intro + init)
        ind = 1
        for key in dic:
            values = dic.get(key)
            text = "POSPEGA[1,"+ str(ind)+ "]={X " + str(values[0]) +",Y "+ str(values[1]) +",Z " + h +",A " + rx + ",B " + ry + ",C "+ rx +"}\n"
            t.write(text)
            ind+=1
        final = "ENDDAT"
        t.write(final)

        self.src.create_src_file(n_camadas, n_caixas)





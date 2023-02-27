#Aquivo .src
from tkinter.filedialog import asksaveasfile

class Src_File:

    def save_file(self):

        f = asksaveasfile(initialfile = 'Untitled.src',defaultextension=".src",filetypes=[("Source File","*.src")])
        return f
    
    def create_src_file(self,n_camadas,n_caixas):
        t = self.save_file()
        intro = "&ACCESS RV1\nDEF  VARIAVEL ( )\n\tIF TEST==1 THEN\n\tFOR ICAMADA = 1 TO 1 STEP 1\n"
        init = "\t\tFOR ICAIXA = 1 TO "+ str(n_caixas) +" STEP 1\n\t\t\tPOSPEGA[ICAMADA,ICAIXA].z=ALTURA*(2-ICAMADA)\n"
        t.write(intro + init)
        final = "\t\tENDFOR\n\tENDFOR\nENDIF\nEND"
        t.write(final)

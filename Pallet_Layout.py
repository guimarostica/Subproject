from tkinter import * 
from PIL import ImageTk, Image
from tkinter import messagebox


class Pallet():
        
    
    def init(self,x,y,listas, text_rotate):
        self.text_rotate = text_rotate
        self.keys = list(self.text_rotate.keys())
        self.listas = listas
        self.root = Tk()
        self.root.geometry(f"{1100}x{580}")

        self.x = int((int(x)*600)/1200)
        self.y = int((int(y)*500)/1000)

        self.root.grid_columnconfigure(1, weight=0)
        self.root.grid_columnconfigure((2, 3), weight=0)
        self.root.grid_rowconfigure((0, 1, 2), weight=1)

        self.impares, self.pares = self.separar_pares_impares(listas)
        print(" O DICIONARIO É : ", self.text_rotate)
        print(" AS KEYS SÃO : ", self.keys)

        


        btn = Button(self.root, text="Press Here!", command=self.add_pallet)
        btn.grid(row=0,column=0, padx=10, pady=10)


    def separar_pares_impares(self,lista_nomes):
        nomes_pares = []
        nomes_impares = []
        for i, nome in enumerate(lista_nomes):
            if i % 2 == 0:
                nomes_pares.append(nome)
            else:
                nomes_impares.append(nome)
        return nomes_pares, nomes_impares

    def add_pallet(self):

        self.my_canvas = Canvas(self.root, width=self.x, height=self.y, bg="white")
        self.my_canvas.grid(row=1, column=2)

        for i,impar in enumerate(self.impares):
            tag = self.keys[i]
            ang = self.text_rotate[tag]
            print("ANGULO: ", ang)
            CENTER_X = ((impar[2] - impar[0])/2)+impar[0]
            CENTER_Y = ((impar[3] - impar[1])/2)+impar[1]
            print("IMPARRRR:", impar)
            self.canvas_item_id = self.my_canvas.create_rectangle( impar[0], impar[1], impar[2], impar[3],outline = "black", fill="gray", activefill = "blue")

            self.my_canvas.create_text(CENTER_X, CENTER_Y, text="ID: "+str(i+1), state="disabled",tags= tag)
            print("oi, tag:", tag)
            self.update_text_position(tag,ang,CENTER_X, CENTER_Y )

    def update_text_position(self,tag,ang,CENTER_X, CENTER_Y):
        print("DANDO UPDATE")
        print("Tag é : ", tag)
        current_angle = 0
        print(current_angle)
        next_ang = current_angle + ang
        # Atualizar a posição do texto
        self.my_canvas.coords(tag, CENTER_X, CENTER_Y)
        self.my_canvas.itemconfigure(tag, angle=ang)

            

        

 
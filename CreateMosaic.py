import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap import Style
from tkinter import Canvas
import math
from Dat import Dat_File
from Src import Src_File
from Pallet_Layout import Pallet


class CreateMosaic(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('{}x{}'.format(1100, 600))
   
        #Creating the widgets

        #Frames
        global create_mosaic_frame, aux_frame, canva_frame 
        create_mosaic_frame= ttk.Frame(self,bootstyle="dark",  width=450)
        aux_frame = ttk.Frame(create_mosaic_frame,bootstyle="info", width=250, height=500)
        
        canva_frame = ttk.Frame(create_mosaic_frame,bootstyle="dark", width=680)
        top_frame = ttk.Frame(self,bootstyle="success",width=622,height=50)
        self.sub_frame_1 = ttk.Frame(create_mosaic_frame,bootstyle="dark", width=100)
        self.sub_frame_2 = ttk.Frame(aux_frame,bootstyle="success", width=250, height=500)
        self.sub_frame_3 = ttk.Frame(aux_frame,bootstyle="success", width=250)
        self.sub_frame_4 = ttk.Frame(aux_frame,bootstyle="success", width=250)
        self.sub_frame_5 = ttk.Frame(canva_frame,bootstyle="success", width=250)
    
     
        #Labels
        
        #Buttons
        self.button_1 = ttk.Button(self.sub_frame_1, text= "Pallet Info", width=10, bootstyle="secondary", command=self.click_1)
        self.button_2 = ttk.Button(self.sub_frame_1, text= "Box Info", width=10,bootstyle="secondary", command=self.click_2)
        self.button_3 = ttk.Button(self.sub_frame_1, text= "Gripper Info", width=10,bootstyle="secondary", command=self.click_3)
        #self.button_4 = ttk.Button(top_frame, text= "Press", width=10,bootstyle="secondary", command=self.get_poses)
        self.button_5 = ttk.Button(self.sub_frame_2, text= "Insert", width=10,bootstyle="secondary")

        
        #Others

        self.name_mosaic_entry = ttk.Entry(top_frame, bootstyle="dark")
        self.button_save_mosaic = ttk.Button(top_frame, bootstyle="dark", text="Save", command= self.save_button_event)
        
        self.sub_frame_2.columnconfigure((0,1,2), weight=0)
        self.sub_frame_2.rowconfigure((0,1,2), weight=0)

        
        #Packing the widgets
        top_frame.pack(side="top", anchor="nw",fill="x", expand=False)
        create_mosaic_frame.pack(side="left", anchor="nw",fill="both", expand=True)
        self.sub_frame_1.pack(side="left", anchor="nw", fill="x", pady=20, padx=(20,0.5))
        aux_frame.pack(side="left", anchor="nw", fill="both", pady=20)
       
        canva_frame.pack(side="left", fill="both")
        self.button_1.pack(fill="x", ipady=30, pady=(0,0.5))
        self.button_2.pack(fill="x", ipady=30, pady=(0,0.5))
        self.button_3.pack(fill="x", ipady=30, pady=(0,0.5))
        #self.button_4.pack()

        self.name_mosaic_entry.pack(side="right")
        self.button_save_mosaic.pack(side="right")

        

        self.bind("<Left>", self.left)
        self.bind("<Right>", self.right)
        self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)
        self.bind("<Delete>", self.delete_box)
        self.bind("<Button-3>", self.rotate)
        self.bind("<BackSpace>", self.reset)

    

        global current_tag
        current_tag = 1

        self.pallet_info = PalletInfo()
        self.pallet_info.show(self.sub_frame_2)
        self.box_info = BoxInfo()
        

        global var_scale
        var_scale = 10

    def click_1(self):
        self.pallet_info.show(self.sub_frame_2)
        self.box_info.hide(self.sub_frame_3)

    def click_2(self):
        self.box_info.show(self.sub_frame_3)
        self.pallet_info.hide(self.sub_frame_2)

    def click_3(self):
        self.box_info.hide(self.sub_frame_3)
        self.pallet_info.hide(self.sub_frame_2)     

    def reset(self, event):
        print("Heloo")
        my_canvas.moveto(id,0,0)
        self.update_text_position(0)
        
    def delete_box(self, event):
        my_canvas.delete(id)
        


    def rotate(self, event):
        angle = 90
        # obtém as coordenadas do retângulo
        x1, y1, x2, y2 = my_canvas.coords(id)
        
        # calcula o ponto central do retângulo
        cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
        
        # rotaciona as coordenadas do retângulo
        x1r = cx + (x1 - cx) * math.cos(math.radians(angle)) - (y1 - cy) * math.sin(math.radians(angle))
        y1r = cy + (x1 - cx) * math.sin(math.radians(angle)) + (y1 - cy) * math.cos(math.radians(angle))
        x2r = cx + (x2 - cx) * math.cos(math.radians(angle)) - (y2 - cy) * math.sin(math.radians(angle))
        y2r = cy + (x2 - cx) * math.sin(math.radians(angle)) + (y2 - cy) * math.cos(math.radians(angle))
        
        # atualiza as coordenadas do retângulo
        my_canvas.coords(id, x1r, y1r, x2r, y2r)
        self.update_text_position(90)

    def update_text_position(self,ang):
        print("DANDO UPDATE")
        
        # Obter as coordenadas atuais do retângulo
        x1, y1, x2, y2 = my_canvas.coords(id)
        print("o self id é : ", id)
        # Calcular a posição central do retângulo
        x_center = (x1 + x2) / 2
        y_center = (y1 + y2) / 2

        tag = "tag"+str(id[0])
        
        get_current_angle = my_canvas.itemconfig(tag, 'angle')
        print("ang:::", get_current_angle)
        current_angle = float(get_current_angle[4])
        print(current_angle)
        if current_angle == -360.0:
            current_angle = 0.0
        next_ang = current_angle + ang
        # Atualizar a posição do texto
        my_canvas.coords(tag, x_center, y_center)
        my_canvas.itemconfigure(tag, angle=current_angle-ang)

    def left(self, event):
        x = - var_scale
        y = 0
        (x1, y1, x2, y2) = my_canvas.coords(id)
        print("mexendo")
        if x1 > 0:
            my_canvas.move(id, x,y)
            self.update_text_position(0)
        else:
            pass
        #self.state_label(id)

    def right(self, event):
        x = var_scale
        y = 0
        print("Valor: ", x)
        print("self>>>", id)
        (x1, y1, x2, y2) = my_canvas.coords(id)
        print("mexendo")
        pallet_x = int((int(entry_pallet_x.get())*600)/1200)
        print(pallet_x)
        print("x2: ", x2)
        if x2 < pallet_x:
            my_canvas.move(id, x,y)
            self.update_text_position(0)
        else:
            pass
        #self.state_label(id)
        
    def up(self, event):
        x = 0
        y = -var_scale
        (x1, y1, x2, y2) = my_canvas.coords(id)
        if y1 > 0:
            my_canvas.move(id, x,y)
            self.update_text_position(0)
        else:
            pass
        #self.state_label(id)
        
    def down(self, event):
        x = 0
        y = var_scale
        pallet_y = int((int(entry_pallet_y.get())*600)/1200)
        (x1, y1, x2, y2) = my_canvas.coords(id)
        if y2 < pallet_y:
            my_canvas.move(id, x,y)
            self.update_text_position(0)
        else:
            pass
        #self.state_label(id)

    def get_poses(self):
        dat_file = Dat_File()

        n_camadas = int((int(entry_pallet_max_height) - int(entry_pallet_height))/int(entry_box_z))
        n=1
        h = entry_box_z*n
        ids =my_canvas.find_all()
        n_caixas = len(ids)
        dic = {}
        
        for id in ids:
            coords = self.state_label(id)
            print(coords)

            dic[id] =  coords


        dat_file.create_dat_file(n_camadas,n_caixas,h,dic)

    def update_scale(self, num):
        self.var_scale = num 

    def clicked_set(self):
       self.var_scale = float(self.scale.get())


    def save_button_event(self):
        canva = Canva()
        canva.box_list()
        
        pallet = Pallet()
        pallet.init(entry_pallet_x.get(), entry_pallet_y.get(), box_lista)
 


#-----------------------------  Functions   -----------------------------

class PalletInfo:
    def show(self, frame):
        frame.pack(side="left", fill="both", expand=True)        
        #-----------------------Pallet-----------------------
        self.Label_1 = ttk.Label(frame, text="Pallet Information", font=("Arial", 11,"bold"), bootstyle="inverse-success")
        # X:
        self.pre_label_x = ttk.Label(frame, text="X: ", font=("Arial", 8, "bold"), bootstyle="inverse-success", anchor="e")
        self.pos_label_x = ttk.Label(frame, text="mm", font=("Arial", 8, "bold"), bootstyle="inverse-success")
        # Y:
        self.pre_label_y = ttk.Label(frame, text="Y: ", font=("Arial", 8, "bold"), bootstyle="inverse-success" )
        self.pos_label_y = ttk.Label(frame, text="mm", font=("Arial", 8, "bold"), bootstyle="inverse-success")
        # Pallet Height:
        self.pre_label_pallet = ttk.Label(frame, text="Pallet\n Height: ", font=("Arial", 8, "bold"), bootstyle="inverse-success" )
        self.pos_label_pallet = ttk.Label(frame, text="mm", font=("Arial", 8, "bold"), bootstyle="inverse-success")
        # Maximum Height:
        self.pre_label_max = ttk.Label(frame, text="Maximum\n Height: ", font=("Arial", 8, "bold"), bootstyle="inverse-success" )
        self.pos_label_max = ttk.Label(frame, text="mm", font=("Arial", 8, "bold"), bootstyle="inverse-success")
        #Entry
        self.entry_pallet_x = ttk.Entry(frame, bootstyle="default", width=10,font=('Arial', 10) )
        self.entry_pallet_y = ttk.Entry(frame, bootstyle="default", width=10,font=('Arial', 10) )
        self.entry_pallet_height = ttk.Entry(frame, bootstyle="default", width=10,font=('Arial', 10) )
        self.entry_pallet_max_height = ttk.Entry(frame, bootstyle="default", width=10,font=('Arial', 10) )
        #Button
        self.button_4 = ttk.Button(frame, text= "Insert", width=10,bootstyle="secondary", command=self.click_insert)
        #Others:
        self.separator = ttk.Separator(frame, bootstyle="dark")

        #GRID
        self.Label_1.grid(row=0, column=1, sticky="we",pady=(10,40), padx=(10,20))
        self.separator.grid(column=0,columnspan=3, row=0, sticky="we")  
        #---
        self.pre_label_x.grid(row=1, column=0,  pady=(0,20), padx=(30,0))
        self.entry_pallet_x.grid(row=1, column=1, sticky="nsew", pady=(0,20))
        self.pos_label_x.grid(row=1, column=2, sticky="w", pady=(0,20), padx=(0,50))
        self.pre_label_y.grid(row=2, column=0,  pady=(0,20), padx=(30,0)) 
        self.entry_pallet_y.grid(row=2, column=1, sticky="nsew", pady=(0,20))
        self.pos_label_y.grid(row=2, column=2, sticky="w", pady=(0,20))
        self.pre_label_pallet.grid(row=3, column=0,  pady=(0,20), padx=(30,0))
        self.entry_pallet_height.grid(row=3, column=1, sticky="nsew", pady=(0,20))
        self.pos_label_pallet.grid(row=3, column=2, sticky="w", pady=(0,20))
        self.pre_label_max.grid(row=4, column=0,  pady=(0,20), padx=(30,0))
        self.entry_pallet_max_height.grid(row=4, sticky="nsew", column=1, pady=(0,20))
        self.pos_label_max.grid(row=4, column=2, sticky="w", pady=(0,20)) 
        #---
        self.button_4.grid(row=5, column=1, pady=20)
    def hide(self, frame):
        frame.pack_forget()

    def click_insert(self):
        global entry_pallet_x, entry_pallet_y, entry_pallet_max_height, entry_pallet_height

        entry_pallet_x = self.entry_pallet_x
        entry_pallet_y = self.entry_pallet_y
        entry_pallet_height = self.entry_pallet_height
        entry_pallet_max_height = self.entry_pallet_max_height

        pallet = Canva()
        pallet.add_pallet(self.entry_pallet_x.get(), self.entry_pallet_y.get())

    
        
class BoxInfo:
    def show(self, frame):
        frame.pack(side="left", fill="both")  
        self.variavel_local = 1
        #-----------------------Pallet-----------------------
        self.Label_1 = ttk.Label(frame, text="Box Information", font=("Arial", 11,"bold"), bootstyle="inverse-success")
        # X:
        self.pre_label_2_x = ttk.Label(frame, text="X: ", font=("Arial", 8, "bold"), bootstyle="inverse-success", anchor="e")
        self.pos_label_2_x = ttk.Label(frame, text="mm", font=("Arial", 8, "bold"), bootstyle="inverse-success")
        # Y:
        self.pre_label_2_y = ttk.Label(frame, text="Y: ", font=("Arial", 8, "bold"), bootstyle="inverse-success" )
        self.pos_label_2_y = ttk.Label(frame, text="mm", font=("Arial", 8, "bold"), bootstyle="inverse-success")
        # Pallet Height:
        self.pre_label_2_z = ttk.Label(frame, text="Z: ", font=("Arial", 8, "bold"), bootstyle="inverse-success" )
        self.pos_label_2_z = ttk.Label(frame, text="mm", font=("Arial", 8, "bold"), bootstyle="inverse-success")
        # Maximum Height:
        self.pre_label_2_weight = ttk.Label(frame, text="Box Weight: ", font=("Arial", 8, "bold"), bootstyle="inverse-success" )
        self.pos_label_2_weight = ttk.Label(frame, text="Kg", font=("Arial", 8, "bold"), bootstyle="inverse-success")
        #Entry
        self.entry_box_x = ttk.Entry(frame, bootstyle="default", width=10,font=('Arial', 10) )
        self.entry_box_y = ttk.Entry(frame, bootstyle="default", width=10,font=('Arial', 10) )
        self.entry_box_z = ttk.Entry(frame, bootstyle="default", width=10,font=('Arial', 10) )
        self.entry_box_weight = ttk.Entry(frame, bootstyle="default", width=10,font=('Arial', 10) )
        self.entry_trans_x = ttk.Entry(frame, bootstyle="default", width=5,font=('Arial', 10) )
        self.entry_trans_y = ttk.Entry(frame, bootstyle="default", width=5,font=('Arial', 10) )
        #Button
        self.button_5 = ttk.Button(frame, text= "Insert", width=10,bootstyle="secondary", command=self.click_insert)
        self.button_6 = ttk.Button(frame, text= "Move", width=10,bootstyle="secondary", command=self.click_move)

        #Others:
        self.separator_2 = ttk.Separator(frame, bootstyle="dark")
        self.separator_3 = ttk.Separator(frame, bootstyle="dark")

        self.pre_trans_x = ttk.Label(frame, text="X: ", font=("Arial", 6, "bold"), bootstyle="inverse-success", anchor="e")
        self.pre_trans_y = ttk.Label(frame, text="Y: ", font=("Arial", 6, "bold"), bootstyle="inverse-success", anchor="e")

        #Scale:

        # Criando um widget Label para mostrar o valor selecionado no Scale
        self.label_scale = ttk.Label(frame, text="Scale",  bootstyle="inverse-success" )

        # Criando um widget Scale e configurando-o para ajustar valores de 1 em 1
        self.scale = ttk.Spinbox(frame,  bootstyle="dark", from_= 0, to = 10, width=4)
        
        self.button_7 = ttk.Button(frame, text = "Set",bootstyle="secondary", command=self.clicked_set)
        
        #GRID
        self.Label_1.grid(row=0, column=1, sticky="we",pady=(10,40), padx=(10,20))
        self.separator_2.grid(column=0,columnspan=3, row=0, sticky="we")  
        #---
        self.pre_label_2_x.grid(row=1, column=0,  pady=(0,20), padx=(30,0))
        self.entry_box_x.grid(row=1, column=1, sticky="nsew", pady=(0,20))
        self.pos_label_2_x.grid(row=1, column=2, sticky="w", pady=(0,20), padx=(0,50))
        self.pre_label_2_y.grid(row=2, column=0,  pady=(0,20), padx=(30,0)) 
        self.entry_box_y.grid(row=2, column=1, sticky="nsew", pady=(0,20))
        self.pos_label_2_y.grid(row=2, column=2, sticky="w", pady=(0,20))
        self.pre_label_2_z.grid(row=3, column=0,  pady=(0,20), padx=(30,0))
        self.entry_box_z.grid(row=3, column=1, sticky="nsew", pady=(0,20))
        self.pos_label_2_z.grid(row=3, column=2, sticky="w", pady=(0,20))
        self.pre_label_2_weight.grid(row=4, column=0,  pady=(0,20), padx=(30,0))
        self.entry_box_weight.grid(row=4, sticky="nsew", column=1, pady=(0,20))
        self.pos_label_2_weight.grid(row=4, column=2, sticky="w", pady=(0,20)) 
        #---
        self.button_5.grid(row=5, column=1, pady=20)
        self.separator_3.grid(row=6, column=0, columnspan=3, sticky="we")  
        #---
        self.pre_trans_x.grid(row=7, column=0,sticky="w",padx=(10,0) )
        self.entry_trans_x.grid(row=7, column=0,sticky="e",padx=(0,10),pady=20 )

        self.pre_trans_y.grid(row=7, column=1,sticky="w",padx=(10,0) )
        self.entry_trans_y.grid(row=7, column=1,pady=20)

        self.button_6.grid(row=7, column=2, sticky="w", padx=(0,10))

        self.label_scale.grid(row=8, column=1 , pady=(20,10))
        self.scale.grid(row=9, column=1, sticky="w")
        self.button_7.grid(row=9, column=1, sticky="e")

        global entry_box_z


        entry_box_z = self.entry_box_z
    def hide(self, frame):
        frame.pack_forget()

    def click_insert(self):
        pallet = Canva()
        pallet.add_box(self.entry_box_x.get(), self.entry_box_y.get(), self.entry_box_z.get())
    
    def click_move(self):
        self.teletransport(self.entry_trans_x.get(), self.entry_trans_y.get())

    def teletransport(self, x, y):
        pallet_x = int((int(entry_pallet_x.get())*600)/1200)
        pallet_y = int((int(entry_pallet_y.get())*600)/1200)
        x = int((int(x)*600)/1200)
        y = int((int(y)*600)/1200)
        if (x > 0 and x < pallet_x) and (y > 0 and y < pallet_y):
            my_canvas.moveto(id, x,y)
            self.update_text_position(0)

    def update_text_position(self,ang):
        print("DANDO UPDATE")
        
        # Obter as coordenadas atuais do retângulo
        x1, y1, x2, y2 = my_canvas.coords(id)
        print("o self id é : ", id)
        # Calcular a posição central do retângulo
        x_center = (x1 + x2) / 2
        y_center = (y1 + y2) / 2

        tag = "tag"+str(id[0])
        
        get_current_angle = my_canvas.itemconfig(tag, 'angle')
        print("ang:::", get_current_angle)
        current_angle = float(get_current_angle[4])
        print(current_angle)
        if current_angle == -360.0:
            current_angle = 0.0
        next_ang = current_angle + ang
        # Atualizar a posição do texto
        my_canvas.coords(tag, x_center, y_center)
        my_canvas.itemconfigure(tag, angle=current_angle-ang)

    def clicked_set(self):
        global var_scale
        var_scale = self.scale.get()



class Canva:
    def add_pallet(self,x,y):
        self.pallet_button_event(x,y)
  
    def pallet_button_event(self,x,y):
        x = int((int(x)*600)/1200)
        print(x)
        y = int((int(y)*500)/1000)
        print(y)
        x2 = int((int(400)*600)/1200)
        y2 = int((int(300)*500)/1000)
        global my_canvas
        my_canvas = Canvas(canva_frame, width=x, height=y)
        my_canvas.pack(side="left", padx=20,expand = False )
        
        
        #my_canvas.bind('<B1-Motion>', self.move)

    def add_box(self,x,y,z):
        global current_tag
        #print("Current: ", current_tag)
        self.x = int((int(x)*600)/1200)
        self.y = int((int(y)*500)/1000)
        self.canvas_item_id =my_canvas.create_rectangle( 0, 0, self.x, self.y, outline = "black", fill="gray", activefill = "blue")
        self.text = my_canvas.create_text(self.x/2, self.y/2, text="ID: "+str(current_tag), state="disabled",tags= "tag"+str(self.canvas_item_id))
        my_canvas.bind("<Button-1>", self.click_box)

        
    
        current_tag += 1

   
    def click_box(self, event):
        global id
        id = my_canvas.find_withtag(CURRENT)
        print("id ====",id)
        print('Item', id, 'Clicked!', my_canvas.coords(id))
        print(my_canvas.find_all())
        
    
   

    def canvas_list(self, event):
        list = my_canvas.find_all()
        return list 
    
    def get_coordinates(self, id):
        (x1, y1, x2, y2) = my_canvas.coords(id)
        x1 = int((int(x1*1200)/600))
        y1 = int((int(y1*1200)/600))
        x2 = int((int(x2*1200)/600))
        y2 = int((int(y2*1200)/600))
        
        return x1, y1, x2, y2
    

    def get_poses(self):
        dat_file = Dat_File()

        n_camadas = int((int(entry_pallet_max_height) - int(entry_pallet_height))/int(entry_box_z))
        n=1
        h = self.entry_box_z.get()*n
        ids =my_canvas.find_all()
        n_caixas = len(ids)
        dic = {}
        
        for id in ids:
            coords = self.state_label(id)
            print(coords)

            dic[id] =  coords


        dat_file.create_dat_file(n_camadas,n_caixas,h,dic)
            

    def move(self, e):
        pallet_x = int((int(self.entry_pallet_x.get())*600)/1200)
        pallet_y = int((int(self.entry_pallet_y.get())*600)/1200)
        if (e.x > 0 and e.x < pallet_x) and (e.y > 0 and e.y < pallet_y):
            my_canvas.moveto(id, e.x,e.y)
        self.state_label(id)
        
    def state_label(self, id):
        x1,y1,x2,y2 = self.get_coordinates(id)
        x0 = int((int(self.x*1200)/600))
        y0 = int((int(self.y*1200)/600))

        center_x = x2 - (x0/2)
        center_y = y2 - (y0/2)
        print("Center_x: ", x2)
        print("Center_y: ", y2)
        self.root.config(text="Coordinate x:" + str(center_x)+ " y:" + str(center_y))

        return center_x, center_y
    def box_list(self):
        global box_lista
        box_lista = []

        lists = my_canvas.find_all()

        for list in lists:
            coords = my_canvas.coords(list)
            box_lista.append(coords)
    



if __name__ == "__main__":
    app = CreateMosaic()
    app.mainloop()



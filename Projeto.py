from tkinter import *
import tkinter.messagebox
import customtkinter
from tkinter.filedialog import asksaveasfile
from Dat import Dat_File
from Pallet_Layout import Pallet
import math
from CreateMosaic import CreateMosaic
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Pallet Automation")
        #self.iconbitmap('icon_1.ico')
        global i
        i=0

        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Pallet Automation", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Project", command=self.sidebar_button1_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Settings", command=self.sidebar_button1_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.main_button_1 = customtkinter.CTkButton(master=self.sidebar_frame, text= "Export",fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=self.get_poses)
        self.main_button_1.grid(row=5, column=0, padx=20, pady=(10, 10))

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250, height=500)
        self.tabview.grid(row=0, column=1, padx=(20, 20), pady=(20, 0))
        self.tabview.add("Pallet")
        self.tabview.add("Box")
        self.tabview.add("Gripper")
        self.tabview.tab("Pallet").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Box").grid_columnconfigure(0, weight=1)

       
        # Pallet

        # X:
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Pallet"), text="X: ")
        self.label_tab_2.grid(row=0, column=0)
        self.entry_pallet_x = customtkinter.CTkEntry(self.tabview.tab("Pallet"))
        self.entry_pallet_x.grid(row= 0, column = 1)
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Pallet"), text="mm")
        self.label_tab_2.grid(row=0, column=2, padx=(10,10), pady=(10, 10))
        # Y:
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Pallet"), text="Y: ")
        self.label_tab_2.grid(row=1, column=0)
        self.entry_pallet_y = customtkinter.CTkEntry(self.tabview.tab("Pallet"))
        self.entry_pallet_y.grid(row= 1, column = 1)
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Pallet"), text="mm")
        self.label_tab_2.grid(row=1, column=2, padx=(10,10), pady=(10, 10))

        # Pallet Height:
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Pallet"), text="Pallet Height: ")
        self.label_tab_2.grid(row=2, column=0)
        self.entry_pallet_height = customtkinter.CTkEntry(self.tabview.tab("Pallet"))
        self.entry_pallet_height.grid(row= 2, column =1)
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Pallet"), text="mm")
        self.label_tab_2.grid(row=2, column=2, padx=(10,10), pady=(10, 10))

        # Maximum Height:
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Pallet"), text="Maximum Height: ")
        self.label_tab_2.grid(row=3, column=0)
        self.entry_pallet_max_height = customtkinter.CTkEntry(self.tabview.tab("Pallet"))
        self.entry_pallet_max_height.grid(row= 3, column = 1)
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Pallet"), text="mm")
        self.label_tab_2.grid(row=3, column=2, padx=(10,10), pady=(10, 10))

        # Add
        self.button_pallet =  customtkinter.CTkButton(self.tabview.tab("Pallet"), text="Add", command=self.pallet_button_event)
        self.button_pallet.grid(row=6, column=1, padx=20, pady=10)
        

        # Box

        # X:
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Box"), text="X: ")
        self.label_tab_2.grid(row=0, column=0)
        self.entry_box_x = customtkinter.CTkEntry(self.tabview.tab("Box"))
        self.entry_box_x.grid(row= 0, column = 1)
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Box"), text="mm")
        self.label_tab_2.grid(row=0, column=2, padx=(10,10), pady=(10, 10))
        # Y:
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Box"), text="Y: ")
        self.label_tab_2.grid(row=1, column=0)
        self.entry_box_y = customtkinter.CTkEntry(self.tabview.tab("Box"))
        self.entry_box_y.grid(row= 1, column = 1)
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Box"), text="mm")
        self.label_tab_2.grid(row=1, column=2, padx=(10,10), pady=(10, 10))

        # Z:
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Box"), text="Z: ")
        self.label_tab_2.grid(row=2, column=0)
        self.entry_box_z = customtkinter.CTkEntry(self.tabview.tab("Box"))
        self.entry_box_z.grid(row= 2, column =1)
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Box"), text="mm")
        self.label_tab_2.grid(row=2, column=2, padx=(10,10), pady=(10, 10))

        # WEIGHT:
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Box"), text="Box Weight: ")
        self.label_tab_2.grid(row=3, column=0)
        self.entry_box_weight = customtkinter.CTkEntry(self.tabview.tab("Box"))
        self.entry_box_weight.grid(row= 3, column = 1)
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Box"), text="Kg")
        self.label_tab_2.grid(row=3, column=2, padx=(10,10), pady=(10, 10))

        # Add
        self.button_pallet =  customtkinter.CTkButton(self.tabview.tab("Box"), text="Add", command= self.box_button_event)
        self.button_pallet.grid(row=6, column=1, padx=20, pady=10)

        #label
        self.my_label = Label(self.tabview.tab("Box"), text="")
        self.my_label.grid(row=8, column=1, padx=20, pady=10)
        
    
        # Gripper

        # X:
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Gripper"), text="Maximum Capacity: ")
        self.label_tab_2.grid(row=0, column=0)
        self.entry_gripper_x = customtkinter.CTkEntry(self.tabview.tab("Gripper"))
        self.entry_gripper_x.grid(row= 0, column = 1)
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Gripper"), text="Kg")
        self.label_tab_2.grid(row=0, column=2, padx=(10,10), pady=(10, 10))
        # Y:
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Gripper"), text="Gripper Length")
        self.label_tab_2.grid(row=1, column=0)
        self.entry_gripper_x = customtkinter.CTkEntry(self.tabview.tab("Gripper"))
        self.entry_gripper_x.grid(row= 1, column = 1)
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Gripper"), text="mm")
        self.label_tab_2.grid(row=1, column=2, padx=(10,10), pady=(10, 10))

        # Tipo de Garra
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Gripper"), text="Type of Gripper")
        self.label_tab_2.grid(row=2, column=0)
        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("Gripper"), dynamic_resizing=False, values=["Side Suction", "Empty"])
        self.optionmenu_1.grid(row=2, column=1, padx=(10,10), pady=(10, 10))

        # Tipo de Pega
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Gripper"), text="Type of Pick")
        self.label_tab_2.grid(row=3, column=0)
        self.optionmenu_2 = customtkinter.CTkOptionMenu(self.tabview.tab("Gripper"), dynamic_resizing=False, values=["Simple", "Multiple"])
        self.optionmenu_2.grid(row=3, column=1, padx=(10,10), pady=(10, 10))

        # Add
        self.button_gripper =  customtkinter.CTkButton(self.tabview.tab("Gripper"), text="Set")
        self.button_gripper.grid(row=6, column=1, padx=20, pady=10)


        


        self.bind("<Left>", self.left)
        self.bind("<Right>", self.right)
        self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)
        self.bind("<Delete>", self.delete_box)
        self.bind("<space>", self.rotate)
        self.bind("<BackSpace>", self.reset)
        
        global current_tag
        current_tag = 1
        
    #----------------------------------------------------------------------------------------------

    # def save_file(self):
    #     f = asksaveasfile(initialfile = 'Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt"),("DAT File","*.dat"),("Source File","*.src")])
    #     return f
    def iconbitmap(self, bitmap=None, default=None):
        self._iconbitmap_method_called = True
        super().wm_iconbitmap(bitmap, default)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def box_list(self):
        lists = self.my_canvas.find_all()

        box_list = []

        for list in lists:
            coords = self.my_canvas.coords(list)
            box_list.append(coords)
        print(box_list)
        return box_list

    def sidebar_button1_event(self):
        pallet = Pallet()
        box_list = self.box_list()
        pallet.init(self.entry_pallet_x.get(), self.entry_pallet_y.get(), box_list)


    def pallet_button_event(self):
        x = int((int(self.entry_pallet_x.get())*600)/1200)
        y = int((int(self.entry_pallet_y.get())*500)/1000)
        self.my_canvas = Canvas(self, width=x, height=y, bg="white")
        self.my_canvas.grid(row = 0, column= 3)
        self.my_canvas.bind("<Button-1>", self.click_box)
        self.my_canvas.bind('<B1-Motion>', self.move)
        
        
    
    def box_button_event(self):
        self.x = int((int(self.entry_box_x.get())*600)/1200)
        self.y = int((int(self.entry_box_y.get())*500)/1000)
        self.add_canvas_item(self.x,self.y)

    def add_canvas_item(self,x,y):
        global current_tag
        print("Current: ", current_tag)
        self.canvas_item_id = self.my_canvas.create_rectangle( 0, 0, x, y, outline = "black", fill="gray", activefill = "blue")
        self.text = self.my_canvas.create_text(x/2, y/2, text="ID: "+str(current_tag), state="disabled",tags= "tag"+str(self.canvas_item_id))
        current_tag += 1
    
    def reset(self, event):
        print("Heloo")
        self.my_canvas.moveto(self.id,0,0)
        self.update_text_position(0)
        
        
    def left(self, event):
        x = -10
        y = 0
        (x1, y1, x2, y2) = self.my_canvas.coords(self.id)
        if x1 > 0:
            self.my_canvas.move(self.id, x,y)
            self.update_text_position(0)
        else:
            pass
        self.state_label(self.id)
        

    def right(self, event):
        x = 10
        y = 0
        print("self>>>", self.id)
        (x1, y1, x2, y2) = self.my_canvas.coords(self.id)
        pallet_x = int((int(self.entry_pallet_x.get())*600)/1200)
        print(pallet_x)
        print("x2: ", x2)
        if x2 < pallet_x:
            self.my_canvas.move(self.id, x,y)
            self.update_text_position(0)
        else:
            pass
        self.state_label(self.id)
        

    def up(self, event):
        x = 0
        y = -10
        (x1, y1, x2, y2) = self.my_canvas.coords(self.id)
        if y1 > 0:
            self.my_canvas.move(self.id, x,y)
            self.update_text_position(0)
        else:
            pass
        self.state_label(self.id)
        

    def down(self, event):
        x = 0
        y = 10
        pallet_y = int((int(self.entry_pallet_y.get())*600)/1200)
        (x1, y1, x2, y2) = self.my_canvas.coords(self.id)
        if y2 < pallet_y:
            self.my_canvas.move(self.id, x,y)
            self.update_text_position(0)
        else:
            pass
        self.state_label(self.id)
        

    def rotate(self, event):
        angle = 90
        # obtém as coordenadas do retângulo
        x1, y1, x2, y2 = self.my_canvas.coords(self.id)
        
        # calcula o ponto central do retângulo
        cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
        
        # rotaciona as coordenadas do retângulo
        x1r = cx + (x1 - cx) * math.cos(math.radians(angle)) - (y1 - cy) * math.sin(math.radians(angle))
        y1r = cy + (x1 - cx) * math.sin(math.radians(angle)) + (y1 - cy) * math.cos(math.radians(angle))
        x2r = cx + (x2 - cx) * math.cos(math.radians(angle)) - (y2 - cy) * math.sin(math.radians(angle))
        y2r = cy + (x2 - cx) * math.sin(math.radians(angle)) + (y2 - cy) * math.cos(math.radians(angle))
        
        # atualiza as coordenadas do retângulo
        self.my_canvas.coords(self.id, x1r, y1r, x2r, y2r)
        self.update_text_position(90)

    def update_text_position(self,ang):
        print("DANDO UPDATE")
        
        # Obter as coordenadas atuais do retângulo
        x1, y1, x2, y2 = self.my_canvas.coords(self.id)
        print("o self id é : ", self.id)
        # Calcular a posição central do retângulo
        x_center = (x1 + x2) / 2
        y_center = (y1 + y2) / 2

        tag = "tag"+str(self.id[0])
        
        get_current_angle = self.my_canvas.itemconfig(tag, 'angle')
        print("ang:::", get_current_angle)
        current_angle = float(get_current_angle[4])
        print(current_angle)
        if current_angle == -360.0:
            current_angle = 0.0
        next_ang = current_angle + ang
        # Atualizar a posição do texto
        self.my_canvas.coords(tag, x_center, y_center)
        self.my_canvas.itemconfigure(tag, angle=current_angle-ang)

    def click_box(self, event):
        self.id = self.my_canvas.find_withtag(CURRENT)
        print("self.id ====",self.id)
        print('Item', self.id, 'Clicked!', self.my_canvas.coords(self.id))
        print(self.my_canvas.find_all())
        
    
    def delete_box(self, event):
        self.my_canvas.delete(self.id)

    def canvas_list(self, event):
        list = self.my_canvas.find_all()
        return list 
    
    def get_coordinates(self, id):
        (x1, y1, x2, y2) = self.my_canvas.coords(id)
        x1 = int((int(x1*1200)/600))
        y1 = int((int(y1*1200)/600))
        x2 = int((int(x2*1200)/600))
        y2 = int((int(y2*1200)/600))
        
        return x1, y1, x2, y2
    

    def get_poses(self):
        dat_file = Dat_File()

        n_camadas = int((int(self.entry_pallet_max_height.get()) - int(self.entry_pallet_height.get()))/int(self.entry_box_z.get()))
        n=1
        h = self.entry_box_z.get()*n
        ids =self.my_canvas.find_all()
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
            self.my_canvas.moveto(self.id, e.x,e.y)
        self.state_label(self.id)
        
    def state_label(self, id):
        x1,y1,x2,y2 = self.get_coordinates(id)
        x0 = int((int(self.x*1200)/600))
        y0 = int((int(self.y*1200)/600))

        center_x = x2 - (x0/2)
        center_y = y2 - (y0/2)
        print("Center_x: ", x2)
        print("Center_y: ", y2)
        self.my_label.config(text="Coordinate x:" + str(center_x)+ " y:" + str(center_y))

        return center_x, center_y




if __name__ == "__main__":
    app = App()
    app.mainloop()
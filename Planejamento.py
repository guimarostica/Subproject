import tkinter as tk
import ttkbootstrap as ttk
from tkinter import Canvas
#from CreateMosaic import CreateMosaic



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pallet Automation")
        #self.iconbitmap('icon_1.ico')       
        
        self.title('Model Definition')
        self.geometry('{}x{}'.format(1200, 600))
   
        #Creating the widgets

        #Frames
        self.create_mosaic_frame = ttk.Frame(self,  width=450)
        self.sub_frame_1 = ttk.Frame(self.create_mosaic_frame,bootstyle="success", width=525)
        self.sub_frame_2 = ttk.Frame(self.create_mosaic_frame,bootstyle="warning", width=525)
        self.create_layer_frame = ttk.Frame(self, bootstyle="success", width=150)
        self.create_sequence_frame = ttk.Frame(self, bootstyle="warning", width=150)
        self.side_frame = ttk.Frame(self, bootstyle="light", width=150,height=150)
        

        #Labels
        #self.mosaic_title = ttk.Label(self.create_mosaic_frame, text="Pallet Automation",background="white").pack()
        self.layer_title = ttk.Label(self.create_layer_frame, text="Pallet Automation",bootstyle="danger").pack()
        self.sequence_title = ttk.Label(self.create_sequence_frame, text="Pallet Automation", bootstyle="danger").pack()
        self.title = ttk.Label(self.side_frame, text="Pallet Automation", bootstyle="light")
        self.title.config(font=("Helvetica", 12, "bold"), foreground="black")

        #Buttons
        self.btn1 = ttk.Button(self.side_frame, text="Create Mosaic", width=30,bootstyle="info", command=self.click1)
        self.btn2 = ttk.Button(self.side_frame, text="Create Layer", width=30,bootstyle="info", command=self.click2)
        self.btn3 = ttk.Button(self.side_frame, text="Create Sequence", width=30,bootstyle="info", command=self.click3)
        self.exp_btn = ttk.Button(self.side_frame, text="Export", width=30, bootstyle="info",command=self.click3)

        #Others
        self.separator = ttk.Separator(self.side_frame, bootstyle="info")
        
        
        #Packing the widgets
        
        self.side_frame.pack(side="left", fill="y")
        self.title.pack(padx=20, pady=(40,0))
        self.separator.pack(fill="x", pady=(0,40))
        self.btn1.pack(pady=10, fill="x")
        self.btn2.pack(pady=10, fill="x")
        self.btn3.pack(pady=10, fill="x")
        self.exp_btn.pack(side="bottom", pady=10)
        self.sub_frame_1.pack(side="left", fill="y")
        self.sub_frame_2.pack(side="left", fill="y")

        self.tela = CreateMosaic()
#-----------------------------  Functions   -----------------------------
    def click1(self):
     
        self.tela.show(self)
        # self.create_mosaic_frame.pack(side="left",fill="both", expand=True)
        self.create_layer_frame.pack_forget()
        self.create_sequence_frame.pack_forget()
    def click2(self):
        self.create_layer_frame.pack(side="left",fill="both", expand=True)
        self.tela.hide()
        self.create_sequence_frame.pack_forget()
    def click3(self):
        self.create_sequence_frame.pack(side="left",fill="both", expand=True)
        self.create_layer_frame.pack_forget()
        self.create_mosaic_frame.pack_forget()

class CreateMosaic:

    def show(self, canva):
        #Frames
        global create_mosaic_frame, aux_frame, canva_frame 
        create_mosaic_frame = ttk.Frame(canva,bootstyle="dark",  width=450)
        aux_frame = ttk.Frame(create_mosaic_frame,bootstyle="info", width=250)
        canva_frame = ttk.Frame(create_mosaic_frame,bootstyle="dark", width=680)
        self.sub_frame_1 = ttk.Frame(create_mosaic_frame,bootstyle="dark", width=100)
        self.sub_frame_2 = ttk.Frame(aux_frame,bootstyle="success", width=250)
        self.sub_frame_3 = ttk.Frame(aux_frame,bootstyle="success", width=250)
        self.sub_frame_4 = ttk.Frame(aux_frame,bootstyle="success", width=250)
        self.sub_frame_5 = ttk.Frame(canva_frame,bootstyle="success", width=250)
    
     
        #Labels
        
        #Buttons
        self.button_1 = ttk.Button(self.sub_frame_1, text= "Pallet Info", width=10, bootstyle="secondary")
        self.button_2 = ttk.Button(self.sub_frame_1, text= "Box Info", width=10,bootstyle="secondary")
        self.button_3 = ttk.Button(self.sub_frame_1, text= "Gripper Info", width=10,bootstyle="secondary")

        #-----------------------Box-----------------------
        self.Label_2 = ttk.Label(self.sub_frame_2, text="Box Information", font=("Arial", 11,"bold"), bootstyle="inverse-success")
        # X:
        self.pre_label_2_x = ttk.Label(self.sub_frame_2, text="X: ", font=("Arial", 8, "bold"), bootstyle="inverse-success", anchor="e")
        self.pos_label_2_x = ttk.Label(self.sub_frame_2, text="mm", font=("Arial", 8, "bold"), bootstyle="inverse-success")
        # Y:_
        self.pre_label_2_y = ttk.Label(self.sub_frame_2, text="Y: ", font=("Arial", 8, "bold"), bootstyle="inverse-success" )
        self.pos_label_2_y = ttk.Label(self.sub_frame_2, text="mm", font=("Arial", 8, "bold"), bootstyle="inverse-success")
        # Pallet Height:
        self.pre_label_2_pallet = ttk.Label(self.sub_frame_2, text="Z: ", font=("Arial", 8, "bold"), bootstyle="inverse-success" )
        self.pos_label_2_pallet = ttk.Label(self.sub_frame_2, text="mm", font=("Arial", 8, "bold"), bootstyle="inverse-success")
        # Maximum Height:
        self.pre_label_2_max = ttk.Label(self.sub_frame_2, text="Box Weight: ", font=("Arial", 8, "bold"), bootstyle="inverse-success" )
        self.pos_label_2_max = ttk.Label(self.sub_frame_2, text="Kg", font=("Arial", 8, "bold"), bootstyle="inverse-success")
        #Buttons
        self.button_1 = ttk.Button(self.sub_frame_1, text= "Pallet Info", width=10, bootstyle="secondary", command=self.click_1)
        self.button_2 = ttk.Button(self.sub_frame_1, text= "Box Info", width=10,bootstyle="secondary", command=self.click_2)
        self.button_3 = ttk.Button(self.sub_frame_1, text= "Gripper Info", width=10,bootstyle="secondary", command=self.click_3)
        
        self.button_5 = ttk.Button(self.sub_frame_2, text= "Insert", width=10,bootstyle="secondary")

        
        #Others
        
        self.sub_frame_2.columnconfigure(2, weight=0)
        self.sub_frame_2.rowconfigure((0,1,2), weight=0)

        
        #Packing the widgets
        
        create_mosaic_frame.pack(side="left",fill="both", expand=True)
        self.sub_frame_1.pack(side="left", fill="both", pady=50, padx=(20,0.5))
        aux_frame.pack(side="left", fill="both", pady=50)
        canva_frame.pack(side="left", fill="both")
        self.button_1.pack(fill="x", ipady=30, pady=(0,0.5))
        self.button_2.pack(fill="x", ipady=30, pady=(0,0.5))
        self.button_3.pack(fill="x", ipady=30, pady=(0,0.5))


        self.pallet_info = PalletInfo()
        self.pallet_info.show(self.sub_frame_2)
        self.box_info = BoxInfo()
    def click_1(self):
        self.pallet_info.show(self.sub_frame_2)
        self.box_info.hide(self.sub_frame_3)

    def click_2(self):
        self.box_info.show(self.sub_frame_3)
        self.pallet_info.hide(self.sub_frame_2)

    def click_3(self):
        self.box_info.hide(self.sub_frame_3)
        self.pallet_info.hide(self.sub_frame_2)     
 
    def hide(self):
        self.create_mosaic_frame.pack_forget()
        #self.sub_frame_1.pack_forget()
        #self.sub_frame_2.pack_forget()

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
        pallet = Canva()
        pallet.add_pallet(self.entry_pallet_x.get(), self.entry_pallet_y.get())   
        
class BoxInfo:
    def show(self, frame):
        frame.pack(side="left", fill="both")  
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
        #Button
        self.button_5 = ttk.Button(frame, text= "Insert", width=10,bootstyle="secondary", command=self.click_insert)
        #Others:
        self.separator_2 = ttk.Separator(frame, bootstyle="dark")

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
    def hide(self, frame):
        frame.pack_forget()
    
    def click_insert(self):
        pallet = Canva()
        pallet.add_box(self.entry_box_x.get(), self.entry_box_y.get(), self.entry_box_z.get())

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
        
        #self.my_canvas.bind("<Button-1>", self.click_box)
        #self.my_canvas.bind('<B1-Motion>', self.move)

    def add_box(self,x,y,z):
        #global current_tag
        #print("Current: ", current_tag)
        self.x = int((int(x)*600)/1200)
        self.y = int((int(y)*500)/1000)
        self.canvas_item_id =my_canvas.create_rectangle( 0, 0, self.x, self.y, outline = "black", fill="gray", activefill = "blue")
        self.text = my_canvas.create_text(self.x/2, self.y/2, text="ID: "+str(1), state="disabled",tags= "tag"+str(self.canvas_item_id))
        #current_tag += 1


if __name__ == "__main__":
    app = App()
    app.mainloop()
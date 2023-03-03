import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap import Style
from tkinter import Canvas
import math
from Dat import Dat_File
from Src import Src_File
from Pallet_Layout import Pallet


class CreateSequence(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pallet Automation")
        #self.iconbitmap('icon_1.ico')       

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
        self.button_1 = ttk.Button(self.sub_frame_1, text= "Gripper \nInfo", width=10, bootstyle="secondary", command=self.click_1)
        self.button_2 = ttk.Button(self.sub_frame_1, text= "Create \nSequence", width=10,bootstyle="secondary", command=self.click_2)
        #self.button_4 = ttk.Button(top_frame, text= "Press", width=10,bootstyle="secondary", command=self.get_poses)
        self.button_5 = ttk.Button(self.sub_frame_2, text= "Insert", width=10,bootstyle="secondary")

        
        #Others
        
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
        
        #self.button_4.pack()

    

        global current_tag
        current_tag = 1

        global mosaicos
        mosaicos = {}

        global var_scale
        var_scale = 10

    def hide(self, frame):
        frame.config(state="disable")

    def click_1(self):
        pass
      

    def click_2(self):
        pass
        

    def click_3(self):
        pass

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
         

if __name__ == "__main__":
    app = CreateSequence()
    app.mainloop()
   
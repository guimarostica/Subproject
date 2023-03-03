import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap import Style
from tkinter import Canvas
import math
from Dat import Dat_File
from Src import Src_File
from Pallet_Layout import Pallet
from PIL import Image, ImageTk


class CreateSequence(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pallet Automation")
        #self.iconbitmap('icon_1.ico')     
        self.geometry('{}x{}'.format(1100, 600))  

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
        self.button_5 = ttk.Button(self.sub_frame_2, text= "Insert", width=10,bootstyle="secondary")
        self.button_6 = ttk.Button(top_frame, text= "Press", width=10,bootstyle="secondary")
        
        #Others
        
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

        self.gripper_info = GripperInfo(self.sub_frame_2)
        self.sequence_info = SequenceInfo(self.sub_frame_3)
        self.gripper_info.show(self.sub_frame_2)
        # self.button_1.config(state="disable")
        

    def hide(self, frame):
        frame.config(state="disable")

    def click_1(self):
        self.gripper_info.show(self.sub_frame_2)
        self.sequence_info.hide(self.sub_frame_3)

    def click_2(self):
        self.sequence_info.show(self.sub_frame_3)
        self.gripper_info.hide(self.sub_frame_2)

    def click_3(self):
        self.gripper_info.hide(self.sub_frame_3)
        self.sequence_info.hide(self.sub_frame_2)     

class GripperInfo:

    def __init__(self, frame):
               
        #-----------------------Pallet-----------------------
        self.Label_1 = ttk.Label(frame, text="Gripper Information", font=("Arial", 11,"bold"), bootstyle="inverse-success")
        # X:
        self.pre_combobox= ttk.Label(frame, text="Grasp Type: ", font=("Arial", 8, "bold"), bootstyle="inverse-success", anchor="e")
        # Y:
        self.pre_entry = ttk.Label(frame, text="Box Number per Grasp: ", font=("Arial", 8, "bold"), bootstyle="inverse-success" )

        self.button_4 = ttk.Button(frame, text= "Set", width=10,bootstyle="secondary", command=self.click_insert)
        #Others:
        self.separator = ttk.Separator(frame, bootstyle="dark")

        self.sequence_entry = ttk.Entry(frame, bootstyle="dark")

        #Check Button
        self.combobox = ttk.Combobox(frame, textvariable = "oi" ,values=['Mult Vaccun','Rastelo','Pá'], bootstyle = "dark")

        #GRID
        self.Label_1.pack(anchor="center", padx=(40),pady=(10,15))
        self.separator.pack(anchor="center", fill="both")
        #---
        self.pre_combobox.pack(pady=(20,5))
        self.combobox.pack(pady=(0,20))
        self.pre_entry.pack(pady=(0,5))
        self.sequence_entry.pack(pady=(0,20))
       
        # self.pre_label_y.grid(row=2, column=0,  pady=(0,20), padx=(30,0)) 
        
        self.button_4.pack(pady=40)
    def show(self,frame):
        frame.pack(side="left", fill="both", expand=True)   

    
    def hide(self, frame):
        frame.pack_forget()

    def click_insert(self):
        self.n_boxes = self.sequence_entry.get()
        self.gasp_type = self.combobox.get()
        print("n: ", self.n_boxes)
        print("type: ", self.gasp_type)

class SequenceInfo:
    def __init__(self, frame):
              
        #-----------------------Pallet-----------------------
        self.Label_1 = ttk.Label(frame, text="Gripper Information", font=("Arial", 11,"bold"), bootstyle="inverse-success")
        # X:
        self.pre_combobox= ttk.Label(frame, text="Grasp Type: ", font=("Arial", 8, "bold"), bootstyle="inverse-success", anchor="e")
        # Y:
        self.pre_entry = ttk.Label(frame, text="Box Number per Grasp: ", font=("Arial", 8, "bold"), bootstyle="inverse-success" )

        self.button_4 = ttk.Button(frame, text= "Set", width=10,bootstyle="secondary", command=self.click_insert)
        #Others:
        self.separator = ttk.Separator(frame, bootstyle="dark")

        self.sequence_entry = ttk.Entry(frame, bootstyle="dark")

        #Check Button
        self.combobox = ttk.Combobox(frame, textvariable = "oi" ,values=['Mult Vaccun','Rastelo','Pá'], bootstyle = "dark")

        #GRID
        # self.Label_1.pack(anchor="center", padx=(40),pady=(10,15))
        # self.separator.pack(anchor="center", fill="both")
        # #---
        # self.pre_combobox.pack(pady=(20,5))
        # self.combobox.pack(pady=(0,20))
        # self.pre_entry.pack(pady=(0,5))
        # self.sequence_entry.pack(pady=(0,20))
       
        # self.pre_label_y.grid(row=2, column=0,  pady=(0,20), padx=(30,0)) 
        
        self.button_4.pack(pady=40)

    def show(self, frame):
        frame.pack(side="left", fill="both", expand=True)  

    def hide(self, frame):
        frame.pack_forget()

    def click_insert(self):
        self.n_boxes = self.sequence_entry.get()
        self.gasp_type = self.combobox.get()
        print("n: ", self.n_boxes)
        print("type: ", self.gasp_type)
         

if __name__ == "__main__":
    app = CreateSequence()
    app.mainloop()
   
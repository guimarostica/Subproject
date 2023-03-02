import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
from tkinter import Canvas
from tkinter import Canvas
import math
from Dat import Dat_File
from Src import Src_File
from Pallet_Layout import Pallet
from CreateMosaic import *



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

        self.bind("<Left>", self.tela.left)
        self.bind("<Right>", self.tela.right)
        self.bind("<Up>", self.tela.up)
        self.bind("<Down>", self.tela.down)
        self.bind("<Delete>", self.tela.delete_box)
        self.bind("<Button-3>", self.tela.rotate)
        self.bind("<BackSpace>", self.tela.reset)
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

if __name__ == "__main__":
    app = App()
    app.mainloop()
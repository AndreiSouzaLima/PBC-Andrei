
import tkinter as tk

from tkinter import *

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        
        # Create text widget and specify size.
        self.label_massa= Label(self.master,text="Massa(Kg)")
        self.label_massa.config(font =("Courier", 14))
        self.label_massa.pack()  
        self.massa = Text(self.master, height = 5, width = 52)
        self.massa.pack(side="top")
              


        self.label_altura= Label(self.master,text="Altura(cm)")
        self.label_altura.config(font =("Courier", 14))
        self.label_altura.pack()

        self.altura = Text(self.master, height = 5, width = 52)
        self.altura.pack(side="top")

        tton_calcular = tk.Button(self)
        self.button_calcular["text"] = "Calcular"
        self.button_calcular["command"] = self.calcular
        self.button_calcular.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")
        self.bu




    def calcular(self):
        print(float(self.massa.get("1.0",END)))

root = tk.Tk()
app = Application(master=root)
app.mainloop()
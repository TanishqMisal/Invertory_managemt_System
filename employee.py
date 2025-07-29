from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from tkinter import *

class employee_Class:
    def __init__(self, parent):
        self.main_frame = Frame(parent, bg="white")
        self.main_frame.place(x=0, y=0, relwidth=1, relheight=1)

     
        Label(self.main_frame, text="Employee Section", font=("Segoe UI", 16), bg="white").pack(pady=20)
        Button(self.main_frame, text="Add Employee", font=("Segoe UI", 12)).pack(pady=10)


if __name__=="__main__":
    root = Tk()
    obj = employee_Class(root)
    root.mainloop()

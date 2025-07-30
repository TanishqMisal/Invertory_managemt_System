from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class employee_Class:
    def __init__(self, parent):
        # === Main Frame ===
        self.main_frame = Frame(parent, bg="white")
        self.main_frame.place(x=0, y=0, relwidth=1, relheight=1)

        # === Modern Header (optional aesthetic) ===
        title = Label(self.main_frame, text="Employee Manager", font=("Segoe UI", 16, "bold"),
                      bg="white", fg="#4B0082")
        title.place(x=30, y=20)

        # === Modern Search Bar ===
        # Just like Google Search - flat and clean
        self.search_by = ttk.Combobox(self.main_frame, values=["Search by", "Email", "Name", "Contact"],
                                      font=("Segoe UI", 10), state="readonly", justify="center")
        self.search_by.place(x=30, y=70, width=120)
        self.search_by.current(0)

        self.search_entry = Entry(self.main_frame, font=("Segoe UI", 11),
                                  bg="#f0f0ff", fg="black", bd=0, relief=FLAT)
        self.search_entry.place(x=160, y=70, width=300, height=25)

        # Fancy underline (simulated using a Frame)
        underline = Frame(self.main_frame, bg="#4B0082")
        underline.place(x=160, y=95, width=300, height=2)

        self.search_btn = Button(self.main_frame, text="Search",
                                 font=("Segoe UI", 10, "bold"),
                                 bg="#4B0082", fg="white", bd=0,
                                 activebackground="#5E4B8B", cursor="hand2")
        self.search_btn.place(x=470, y=68, width=80, height=28)

        # === Add your table or search results below here ===

if __name__ == "__main__":
    root = Tk()
    root.title("Inventory Management System")
    root.geometry("1200x600+100+100")
    obj = employee_Class(root)
    root.mainloop()

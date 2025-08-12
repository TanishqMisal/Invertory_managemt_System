from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from pathlib import Path
from employee import employee_Class 

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")

        # Base directory for image assets (relative to this script)
        BASE_DIR = Path(__file__).parent
        IMAGE_DIR = BASE_DIR / "images"

        # Helper function to load and resize images
        def load_image(filename, size):
            path = IMAGE_DIR / filename
            return ImageTk.PhotoImage(Image.open(path).resize(size))

        self.icon_title = load_image("LOGO.png", (50,50))
        title = Label(
            self.root, text="  Inventory Management System",
            image=self.icon_title, compound=LEFT,
            font=("Segoe UI", 20, "bold"),
            bg="#5A55CA", fg='white', anchor='w', padx=10
        )
        title.pack(side=TOP, fill=X)

        
        body_frame = Frame(self.root)
        body_frame.pack(fill=BOTH, expand=True)

        self.menu_frame = Frame(body_frame, width=220, bg="#E3DAFF")
        self.menu_frame.pack(side=LEFT, fill=Y)

        self.content_frame = Frame(body_frame, bg="#FFFFFF")
        self.content_frame.pack(side=LEFT, fill=BOTH, expand=True)

        
        self.home_icon = load_image("house-black-silhouette-without-door.png", (40, 40))
        self.employee_icon = load_image("emp.png", (30, 30))
        self.suppy_icon = load_image("SUPPLY.png", (30, 30))
        self.product_icon = load_image("PET SUPPLIES.png",(30, 30))
        self.inv_icon = load_image("INVEN.png", (30, 30))
        self.sales_icon = load_image("coupon.png", (30, 30))
        self.logout_icon = load_image("turn-off.png", (30, 30))
        self.grooming_icon = load_image("grooming.png",(30,30))
        self.daybook_icon = load_image("money.png",(30,30))

        self.active_tab = None
        self.menu_buttons = {}
    
        Button(
            self.menu_frame, text="Dashboard",
            font=("Segoe UI", 16, "bold"),
            bg="#3D3B8E", fg="white", pady=10,
            image=self.home_icon, compound=LEFT, padx=10,
            bd=0,activebackground='#4B48A9',cursor="hand2",
            command=self.show_home
        ).pack(fill=X)


        btn_style = {
            "font": ("Segoe UI", 14),
            "bg": "#FFFFFF", "fg": "#333",
            "bd": 0, "cursor": "hand2",
            "anchor": "w", "padx": 20
        }

        
        emp_btn = Button(self.menu_frame,text="Employee",image=self.employee_icon,compound=LEFT,**btn_style,command=lambda:[self.employee(),self.highlight_tab("employee")])
        emp_btn.pack(fill=X,pady=2)
        self.menu_buttons["employee"]=emp_btn
            
        sup_btn = Button(self.menu_frame, text="Supplier",image=self.suppy_icon,compound=LEFT,**btn_style, command=self.toggle_supplier_menu)
        sup_btn.pack(fill=X,pady=2)
        
        self.menu_buttons["supplier"] = sup_btn

        self.supplier_sub_buttons = [

            Button(self.menu_frame,text="Manage Supplier", **btn_style,command=self.supplier_manage),
            Button(self.menu_frame,text="Add Supplier", **btn_style,command=self.supplier_add)
        ]
        self.supplier_dropdown_visible = False

        Button(self.menu_frame, text="Products", image=self.product_icon, compound=LEFT, **btn_style).pack(fill=X, pady=2)
        Button(self.menu_frame, text="Inventory", image=self.inv_icon, compound=LEFT, **btn_style).pack(fill=X, pady=2)
        Button(self.menu_frame, text="Sales", image=self.sales_icon, compound=LEFT, **btn_style).pack(fill=X, pady=2)
        Button(self.menu_frame,text="Grooming",image=self.grooming_icon,compound=LEFT,**btn_style).pack(fill=X,pady=2)
        Button(self.menu_frame,text="Collection",image=self.daybook_icon,compound=LEFT,**btn_style).pack(fill=X,pady=2)
        Button(self.menu_frame, text="Logout", image=self.logout_icon, compound=LEFT, **btn_style).pack(fill=X, pady=30)

        
        self.show_home()

    def supplier_add(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        Label(self.content_frame,text="Add Supplier",font=("Segoe UI",20),bg='#FFFFFF',fg='#333').pack(padx=20)

    def supplier_manage(self):
        for widget in self.content_frame.winfo_children():
             widget.destroy()
        Label(self.content_frame,text="Manage Supplier",font=("Segoe UI",20), bg='#FFFFFF',fg="#333").pack(pady=20)

    def toggle_supplier_menu(self):
        if self.supplier_dropdown_visible:
            for btn in self.supplier_sub_buttons:
                  btn.pack_forget()
            self.supplier_dropdown_visible = False
        else:
            for btn in self.supplier_sub_buttons:
                  btn.pack(fill = X, padx=40)
            self.supplier_dropdown_visible = True

    def highlight_tab(self,tab_name):
            for name, btn in self.menu_buttons.items():
                if name == tab_name:
                    btn.config(bg= '#5A55CA',fg='white')
                else:
                        btn.config(bg="#FFFFFF",fg = '#333')
            self.active_tab = tab_name  

    def show_home(self):
        for widget in self.content_frame.winfo_children():
                widget.destroy()

        Label(
            self.content_frame,text="Welcome to IMS Dashboard!",
            font=("Segoe UI",20),bg='#FFFFFF',fg='#333'
            ).pack(pady=20)

    def employee(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        self.employee_obj = employee_Class(self.content_frame)

    def supplier(self):
         for widget in self.content_frame.winfo_children():
              widget.destroy()
         Label(self.content_frame,text="Supplier Section",font=("Segoe UI",20),bg='#FFFFFF',fg='#333').pack(pady=20)

if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
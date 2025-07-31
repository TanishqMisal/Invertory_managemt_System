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
        self.suppy_icon = load_image("product-lifecycle.png", (30, 30))
        self.product_icon = load_image("animal.png", (30, 30))
        self.inv_icon = load_image("track.png", (30, 30))
        self.sales_icon = load_image("coupon.png", (30, 30))
        self.logout_icon = load_image("power-off.png", (30, 30))



    
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

        
        Button(self.menu_frame, text="Employee", command=self.employee, image=self.employee_icon, compound=LEFT, **btn_style).pack(fill=X, pady=2)
        Button(self.menu_frame, text="Supplier", image=self.suppy_icon, compound=LEFT, **btn_style).pack(fill=X, pady=2)
        Button(self.menu_frame, text="Products", image=self.product_icon, compound=LEFT, **btn_style).pack(fill=X, pady=2)
        Button(self.menu_frame, text="Inventory", image=self.inv_icon, compound=LEFT, **btn_style).pack(fill=X, pady=2)
        Button(self.menu_frame, text="Sales", image=self.sales_icon, compound=LEFT, **btn_style).pack(fill=X, pady=2)
        Button(self.menu_frame, text="Logout", image=self.logout_icon, compound=LEFT, **btn_style).pack(fill=X, pady=30)

        
        self.show_home()

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

if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
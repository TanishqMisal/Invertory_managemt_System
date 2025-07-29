from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from employee import employee_Class  # Make sure this is correct

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")

       
        icon_image = Image.open(r'C:\python\Invertory management\images\photo_2025-07-28_02-47-39.png').resize((30, 30))
        self.icon_title = ImageTk.PhotoImage(icon_image)

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

        
        self.home_icon = ImageTk.PhotoImage(Image.open(r'C:\python\Invertory management\images\house-black-silhouette-without-door.png').resize((40, 40)))
        self.employee_icon = ImageTk.PhotoImage(Image.open(r'C:\python\Invertory management\images\emp.png').resize((30, 30)))
        self.suppy_icon = ImageTk.PhotoImage(Image.open(r'C:\python\Invertory management\images\product-lifecycle.png').resize((30, 30)))
        self.product_icon = ImageTk.PhotoImage(Image.open(r'C:\python\Invertory management\images\animal.png').resize((30, 30)))
        self.inv_icon = ImageTk.PhotoImage(Image.open(r'C:\python\Invertory management\images\track.png').resize((30, 30)))
        self.sales_icon = ImageTk.PhotoImage(Image.open(r'C:\python\Invertory management\images\coupon.png').resize((30, 30)))
        self.logout_icon = ImageTk.PhotoImage(Image.open(r'C:\python\Invertory management\images\power-off.png').resize((30, 30)))

        Label(
            self.menu_frame, text="Dashboard",
            font=("Segoe UI", 16, "bold"),
            bg="#3D3B8E", fg="white", pady=10,
            image=self.home_icon, compound=LEFT, padx=10
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


        Label(
            self.content_frame, text="Welcome to IMS Dashboard!",
            font=("Segoe UI", 20), bg="#FFFFFF", fg="#333"
        ).pack(pady=20)

    def employee(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        self.employee_obj = employee_Class(self.content_frame)

if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
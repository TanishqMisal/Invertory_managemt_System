from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog
import os

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

        Label(self.main_frame,text="ADD NEW EMPLOYEE",font=("Segoe UI",15,"bold"), fg="#555",bg='#FFFFFF').place(x=30,y=120)
   
        name_box = Label(self.main_frame,text="Name",
                         font=("Segoe UI",10, "bold"),
                         fg='#555',bg='white')
        name_box.place(x=30,y=160)

        self.name_entry = Entry(self.main_frame,
                                font=("Segoe UI",11),
                                bd=1, relief=FLAT,bg='white',fg='#333',
                                highlightcolor='#4B0082',highlightbackground='#ccc',highlightthickness=1)
        self.name_entry.place(x=30,y=185,width=250,height=30)

        contact_no = Label(self.main_frame,text="Contact No.",font=("Segoe UI",10,"bold"),
                           fg='#555',bg='white')
        contact_no.place(x=297,y=160)

        self.contant_entry = Entry(self.main_frame,
                                   font=("Segoe UI",11),bd=1,relief=FLAT,bg='white',fg='#333',
                                   highlightcolor='#4B0082',highlightbackground='#ccc',highlightthickness=1)
        self.contant_entry.place(x=300,y=185,width=250,height=30)

        email_box = Label(self.main_frame,text="Email",
                          font=("Segoe UI",10,'bold'),
                          fg='#555',bg='white')
        email_box.place(x=30,y=225)

        self.email_entry = Entry(self.main_frame,font=("segoe UI",11),
                                 bd=1,relief=FLAT,bg='white',fg='#333',
                                 highlightcolor="#4B0082",highlightbackground='#ccc',highlightthickness=1)
        self.email_entry.place(x=30,y=250,width=250,height='30')

        salary_box = Label(self.main_frame,text="Salary",
                          font=("Segoe UI",10,'bold'),
                          fg='#555',bg='white')
        salary_box.place(x=297,y=225)

        self.salary_entry = Entry(self.main_frame,font=("segoe UI",11),
                                 bd=1,relief=FLAT,bg='white',fg='#333',
                                 highlightcolor="#4B0082",highlightbackground='#ccc',highlightthickness=1)
        self.salary_entry.place(x=300,y=250,width=250,height='30')

        Role_box = Label(self.main_frame,text="Role",
                         font=("Segoe UI",10, "bold"),
                         fg='#555',bg='white')
        Role_box.place(x=30,y=285)

        self.Role_box = Entry(self.main_frame,
                                font=("Segoe UI",11),
                                bd=1, relief=FLAT,bg='white',fg='#333',
                                highlightcolor='#4B0082',highlightbackground='#ccc',highlightthickness=1)
        self.Role_box.place(x=30,y=310,width=250,height=30)

        #photo upload
        
        photo_lable = Label(self.main_frame,text='photo',
                            font=("Segoe UI",10,"bold"),
                            fg='#555',bg='White'
                            )
        photo_lable.place(x=297,y=285)

        self.upload_btn = Button(self.main_frame,text="Upload Photo",
                                 font=("Segoe UI",10),bg="#4B0082",fg='white',bd=0,
                                 command=self.upload_photo
                                 )
        self.upload_btn.place(x=300,y=440,width=125,height=30)

        self.photo_preview = Label(self.main_frame,bg='white',bd=1, relief=SOLID)
        self.photo_preview.place(x=300,y=310,width=125,height=125)

        self.selected_photo_path = None

        btn_save = Button(self.main_frame, text="Save ",
                          font=("Inter", 14),bg="#4B0082",
                          bd= 0, cursor='hand2',fg='white',foreground='white',
                          activebackground='#5E4B8B',
                          highlightthickness=2,
                          highlightcolor='white'
                          
                          ).place(x=30,y=400,width=80)
        
        btn_update = Button(self.main_frame, text="Update",
                          font=("Inter", 14),bg="#D6C24A",
                          bd= 0, cursor='hand2',fg='white',foreground='white',
                          activebackground='#E8DC89',
                          highlightthickness=2,
                          highlightcolor='white'
                          
                          ).place(x=160,y=400,width=80)
        
        btn_delete = Button(self.main_frame, text="Delete",
                          font=("Inter", 14),bg="#F30A0A",
                          bd= 0, cursor='hand2',fg='white',foreground='white',
                          activebackground="#FFA3A3",
                          highlightthickness=2,
                          highlightcolor='white'
                          
                          ).place(x=30,y=475,width=80)
        
        btn_clear = Button(self.main_frame, text="clear",
                          font=("Inter", 14),bg="#CDBEE7",
                          bd= 0, cursor='hand2',fg='white',foreground='white',
                          activebackground="#FFFFFF",
                          highlightthickness=2,
                          highlightcolor='white'
                          
                          ).place(x=160,y=475,width=80)
        

    def upload_photo(self):
        file_path = filedialog.askopenfilename(
            title = "Select photo",
            filetype = [("Image Files", "*.jpg *.jpeg *.png *.gif")]
            )
            
        if file_path:
            self.selected_photo_path = file_path

            img = Image.open(file_path)
            img = img.resize((100,100))
            self.tk_img = ImageTk.PhotoImage(img)

            self.photo_preview.config(image=self.tk_img)

            



if __name__ == "__main__":
    root = Tk()
    root.title("Inventory Management System")
    root.geometry("1200x600+100+100")
    obj = employee_Class(root)
    root.mainloop()

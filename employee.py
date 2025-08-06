from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkinter import filedialog
import os
import sqlite3
from io import BytesIO

class employee_Class:
    def __init__(self, parent):
        # === Main Frame ===
        self.main_frame = Frame(parent, bg="white")
        self.main_frame.place(x=0, y=0, relwidth=1, relheight=1)

        title = Label(self.main_frame, text="Employee Manager", font=("Segoe UI", 16, "bold"),
                      bg="white", fg="#4B0082")
        title.place(x=30, y=20)

        self.search_by = ttk.Combobox(self.main_frame, values=["Search by", "Email", "Name", "Contact"],
                                      font=("Segoe UI", 10), state="readonly", justify="center")
        self.search_by.place(x=30, y=70, width=120)
        self.search_by.current(0)

        self.search_entry = Entry(self.main_frame, font=("Segoe UI", 11),
                                  bg="#f0f0ff", fg="black", bd=0, relief=FLAT)
        self.search_entry.place(x=160, y=70, width=300, height=25)

        underline = Frame(self.main_frame, bg="#4B0082")
        underline.place(x=160, y=95, width=300, height=2)

        self.search_btn = Button(self.main_frame, text="Search",
                                 font=("Segoe UI", 10, "bold"),
                                 bg="#4B0082", fg="white", bd=0,
                                 activebackground="#5E4B8B", cursor="hand2")
        self.search_btn.place(x=470, y=68, width=80, height=28)

        Label(self.main_frame, text="ADD NEW EMPLOYEE", font=("Segoe UI", 15, "bold"), fg="#555", bg='#FFFFFF').place(x=30, y=120)

        Label(self.main_frame, text="Name", font=("Segoe UI", 10, "bold"), fg='#555', bg='white').place(x=30, y=160)
        self.name_entry = Entry(self.main_frame, font=("Segoe UI", 11), bd=1, relief=FLAT, bg='white', fg='#333',
                                highlightcolor='#4B0082', highlightbackground='#ccc', highlightthickness=1)
        self.name_entry.place(x=30, y=185, width=250, height=30)

        Label(self.main_frame, text="Contact No.", font=("Segoe UI", 10, "bold"), fg='#555', bg='white').place(x=297, y=160)
        self.contact_entry = Entry(self.main_frame, font=("Segoe UI", 11), bd=1, relief=FLAT, bg='white', fg='#333',
                                   highlightcolor='#4B0082', highlightbackground='#ccc', highlightthickness=1)
        self.contact_entry.place(x=300, y=185, width=250, height=30)

        Label(self.main_frame, text="Email", font=("Segoe UI", 10, 'bold'), fg='#555', bg='white').place(x=30, y=225)
        self.email_entry = Entry(self.main_frame, font=("segoe UI", 11), bd=1, relief=FLAT, bg='white', fg='#333',
                                 highlightcolor="#4B0082", highlightbackground='#ccc', highlightthickness=1)
        self.email_entry.place(x=30, y=250, width=250, height=30)

        Label(self.main_frame, text="Salary", font=("Segoe UI", 10, 'bold'), fg='#555', bg='white').place(x=297, y=225)
        self.salary_entry = Entry(self.main_frame, font=("segoe UI", 11), bd=1, relief=FLAT, bg='white', fg='#333',
                                  highlightcolor="#4B0082", highlightbackground='#ccc', highlightthickness=1)
        self.salary_entry.place(x=300, y=250, width=250, height=30)

        Label(self.main_frame, text="Role", font=("Segoe UI", 10, "bold"), fg='#555', bg='white').place(x=30, y=285)
        self.Role_box = Entry(self.main_frame, font=("Segoe UI", 11), bd=1, relief=FLAT, bg='white', fg='#333',
                              highlightcolor='#4B0082', highlightbackground='#ccc', highlightthickness=1)
        self.Role_box.place(x=30, y=310, width=250, height=30)

        Label(self.main_frame, text='Photo', font=("Segoe UI", 10, "bold"), fg='#555', bg='White').place(x=297, y=285)

        self.upload_btn = Button(self.main_frame, text="Upload Photo", font=("Segoe UI", 10),
                                 bg="#4B0082", fg='white', bd=0, command=self.upload_photo)
        self.upload_btn.place(x=300, y=440, width=125, height=30)

        self.photo_preview = Label(self.main_frame, bg='white', bd=1, relief=SOLID)
        self.photo_preview.place(x=300, y=310, width=125, height=125)
        self.selected_photo_path = None

        Button(self.main_frame, text="Save", font=("Inter", 14), bg="#4B0082", fg='white', bd=0, cursor='hand2',
               activebackground='#5E4B8B', highlightthickness=2, highlightcolor='white', command=self.add).place(x=30, y=350, width=80)
        Button(self.main_frame, text="Update", font=("Inter", 14), bg="#D6C24A", fg='white', bd=0, cursor='hand2',
               activebackground='#E8DC89', highlightthickness=2, highlightcolor='white',command=self.update).place(x=160, y=350, width=80)
        Button(self.main_frame, text="Delete", font=("Inter", 14), bg="#F30A0A", fg='white', bd=0, cursor='hand2',
               activebackground="#FFA3A3", highlightthickness=2, highlightcolor='white',command=self.delete).place(x=30, y=400, width=80)
        Button(self.main_frame, text="Clear", font=("Inter", 14), bg="#CDBEE7", fg='white', bd=0, cursor='hand2',
               activebackground="#FFFFFF", highlightthickness=2, highlightcolor='white',command=self.clear_fields).place(x=160, y=400, width=80)

        Label(self.main_frame, text="Employee List", bg="#4B0082", fg="white",
              font=("Segoe UI", 14, "bold")).place(x=30, y=495, width=950, height=30)

        list_frame = Frame(self.main_frame, bd=2, relief=RIDGE, bg='white')
        list_frame.place(x=30, y=525, width=950, height=200)

        scroll_x = Scrollbar(list_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(list_frame, orient=VERTICAL)

        self.employee_table = ttk.Treeview(list_frame, columns=("Name", "Contact No.", "Email", "Salary", "Role"),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        for heading in ("Name", "Contact No.", "Email", "Salary", "Role"):
            self.employee_table.heading(heading, text=heading)
            self.employee_table.column(heading, width=150)

        self.employee_table["show"] = "headings"
        self.employee_table.pack(fill=BOTH, expand=1)
        self.employee_table.bind("<ButtonRelease-1>",self.show_data)

        self.show()

        

    def upload_photo(self):
        file_path = filedialog.askopenfilename(
            title="Select photo",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif")]
        )

        if file_path:
            self.selected_photo_path = file_path
            img = Image.open(file_path).resize((100, 100))
            self.tk_img = ImageTk.PhotoImage(img)
            self.photo_preview.config(image=self.tk_img)

    def show_error(self, error_title="Error", message="Name required", code="Name Error"):
        error_win = Toplevel(self.main_frame)
        error_win.title("Error")
        error_win.config(bg="#f44336")
        error_win.resizable(False, False)

        popup_widht = 300
        popup_height = 200

        self.main_frame.update_idletasks()
        main_x = self.main_frame.winfo_rootx()
        main_y = self.main_frame.winfo_rooty()
        main_widht = self.main_frame.winfo_width()
        main_height = self.main_frame.winfo_height()

        center_x = main_x +(main_widht//2)-( popup_widht //2)
        center_y = main_y+(main_height//2)-(popup_height//2)

        error_win.geometry(f"{popup_widht}x{popup_height}+{center_x}+{center_y}")

        Label(error_win, text="😞", font=("Segoe UI", 40), bg="#f44336", fg="white").pack(pady=(10, 0))
        Label(error_win, text=error_title, font=("Segoe UI", 16, "bold"), bg="#f44336", fg="white").pack()
        Label(error_win, text=f"{message}\n({code})", font=("Segoe UI", 10),
              bg="#f44336", fg="white", justify="center").pack(pady=10)

        Button(error_win, text="OK", font=("Segoe UI", 10, "bold"),
               bg="white", fg='#f44336', cursor="hand2",
               command=error_win.destroy).pack(pady=10)

        error_win.transient(self.main_frame)
        error_win.grab_set()
        self.main_frame.wait_window(error_win)

        self.show()

    def add(self):
        name = self.name_entry.get()
        contact = self.contact_entry.get()
        email = self.email_entry.get()
        salary = self.salary_entry.get()
        role = self.Role_box.get()

        if not name:
            self.show_error(message="Name is required", code="EMP1001")
            return

        photo_data = None
        if self.selected_photo_path:
            with open(self.selected_photo_path, 'rb') as file:
                photo_data = file.read()

        try:
            con = sqlite3.connect("employee.db")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS employee (name TEXT, contact TEXT, email TEXT, salary TEXT, role TEXT, photo BLOB)")
            cur.execute("INSERT INTO employee VALUES (?, ?, ?, ?, ?, ?)", (name, contact, email, salary, role, photo_data))
            con.commit()
            con.close()
            self.show()
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Database Error", f"Error: {str(e)}")

    def show(self):
        try:
            con = sqlite3.connect("ims.db")
            cur = con.cursor()
            cur.execute("SELECT name, contact, email, salary, role FROM employee")
            rows = cur.fetchall()
            con.close()

            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert('', END, values=row)
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def clear_fields(self):
        self.name_entry.delete(0, END)
        self.contact_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.salary_entry.delete(0, END)
        self.Role_box.delete(0, END)
        self.selected_photo_path = None
        self.photo_preview.config(image='')

    def show_data(self, event):
        selected = self.employee_table.focus()
        if not selected:
            return

        data = self.employee_table.item(selected)['values']
        if data:
            self.name_entry.delete(0, END)
            self.contact_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.salary_entry.delete(0, END)
            self.Role_box.delete(0, END)

            self.name_entry.insert(0, data[0])
            self.contact_entry.insert(0, data[1])
            self.email_entry.insert(0, data[2])
            self.salary_entry.insert(0, data[3])
            self.Role_box.insert(0, data[4])

        try:
            con = sqlite3.connect("ims.db")
            cur = con.cursor()
            cur.execute("SELECT photo FROM employee WHERE email = ?", (data[2],))
            result = cur.fetchone()
            con.close()

            if result and result[0]:
                image_data = BytesIO(result[0])
                img = Image.open(image_data).resize((100, 100))
                self.tk_img = ImageTk.PhotoImage(img)  # 🔐 Keep a reference!
                self.photo_preview.config(image=self.tk_img)
            else:
                self.photo_preview.config(image='')
                self.tk_img = None
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {str(e)}")
    
    def update(self):
        name = self.name_entry.get()
        contact = self.contact_entry.get()
        email = self.email_entry.get()
        salary = self.salary_entry.get()
        role = self.Role_box.get()

        if not email:
            self.show_error(message="Email is required to update employee", code = "EMP1002")
            return
        try:
            con = sqlite3.connect("ims.db")
            cur = con.cursor()

            photo_data = None
            if self.selected_photo_path:
                with open(self.selected_photo_path, 'rb') as file:
                    photo_data = file.read()
            
            if photo_data:
                cur.execute("""
                UPDATE employee 
                SET name=?, contact=?, salary=?, role=?, photo=? 
                WHERE email=?
                """, (name, contact, salary, role, photo_data, email))
            else:
                cur.execute("""
                UPDATE employee 
                SET name=?, contact=?, salary=?, role=? 
                WHERE email=?
                """, (name, contact, salary, role, email))

            
            con.commit()
            con.close()

            messagebox.showinfo("Success","Employee record updated successfully!")
            self.show()
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Error",f"Failed to update:{str(e)}")


    def delete(self):
        email = self.email_entry.get()

        if not email:
            self.show_error(message="Email is required to delete employee", code="EMP1003")
            return

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this employee?")

        if confirm:
            try:
                con = sqlite3.connect("ims.db")
                cur = con.cursor()
                cur.execute("DELETE FROM employee WHERE email = ?", (email,))
                con.commit()
                con.close()

                messagebox.showinfo("Success", "Employee deleted successfully!")
                self.show()
                self.clear_fields()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete: {str(e)}")


if __name__ == "__main__":
    root = Tk()
    root.title("Inventory Management System")
    root.geometry("1200x600+100+100")
    obj = employee_Class(root)
    root.mainloop()

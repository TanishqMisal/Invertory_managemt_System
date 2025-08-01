import sqlite3

def create_db():
    con = sqlite3.connect(database = r'ims.db')

    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS employee(Name text,Contact No text,Email text,Salary text,Role text)")
    con.commit()

create_db()
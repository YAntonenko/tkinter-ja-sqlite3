import tkinter as tk
from tkinter import messagebox
import sqlite3

#Funkt
# validate_data funktsioon, mis kontrollib kas sisestatud andmed on korrektsed
def validate_data():
    enimi = entries["Eesinimi"].get()
    pnimi = entries["Perenimi"].get()
    email= entries["email"].get()
    telefon= entries["telefon"].get()
    pilt= entries["pilt"].get()

    if not enimi:
        tk.messagebox.showerror("Viga", "Eesinimi on kohustuslik!")
        return False
    if not pnimi.isdigit():
        tk.messagebox.showerror("Viga", "Perenimi on kohustuslik")
        return False
    if not email.isdigit():
        tk.messagebox.showerror("Viga", "Email on kohustuslik")
        return False
    if not telefon.isdigit():
        tk.messagebox.showerror("Viga", "Telefon on kohustuslik")
        return False
    if not pilt.isdigit():
        tk.messagebox.showerror("Viga", "Pilt on kohustuslik")
        return False

    #tk.messagebox.showinfo("Edu", "Andmed on kehtivad!")
    return True



def insert_data():
    if validate_data():
        connection = sqlite3.connect("yantonenko.db")
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO movies (first_name, last_name, email, phone, image)
            VALUES (?, ?, ?, ?, ?)
        """, (
            entries["Eesinimi"].get(),
            entries["Perenimi"].get(),
            entries["Email"].get(),
            entries["Telefon"].get(),
            entries["Pilt"].get()
        ))

        connection.commit()
        connection.close()

        messagebox.showinfo("Edu", "Andmed sisestati edukalt!")


# Loo Tkinteri aken
root = tk.Tk()
root.title("Kasutaja liisamine")



# Loo sildid ja sisestusväljad
labels = ["eesinimi", "perenimi", "email", "telefon", "pilt"]
entries = {}

for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(root, width=40)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries[label] = entry



# Loo nupp andmete sisestamiseks
submit_button = tk.Button(root, text="Sisesta kasutaja", command=insert_data)
submit_button.grid(row=len(labels), column=0, columnspan=2, pady=20)




# Näita Tkinteri akent
root.mainloop()
import tkinter as tk
from tkinter import ttk
import sqlite3

# Funktsioon, mis laadib andmed SQLite andmebaasist ja sisestab need Treeview tabelisse
def load_data_from_db(tree):
    # Loo ühendus SQLite andmebaasiga
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    # Tee päring andmebaasist andmete toомiseks
    cursor.execute("SELECT first_name, last_name, email, phone, image FROM users")
    rows = cursor.fetchall()

    # Lisa andmed tabelisse
    for row in rows:
        tree.insert("", "end", values=row)

    # Sulge ühendus andmebaasiga
    conn.close()

# Loo põhiaken
root = tk.Tk()
root.title("movies.db")

# Loo raam kerimistriibaga
frame = tk.Frame(root)
frame.pack(padx=20, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Loo tabel (Treeview) andmete kuvamiseks
tree = ttk.Treeview(frame, yscrollcommand=scrollbar.set, columns=("first_name", "last_name", "email", "phone", "image"), show="headings")
tree.pack(fill=tk.BOTH, expand=True)

# Seosta kerimistriba tabeliga
scrollbar.config(command=tree.yview)

# Määra veergude pealkirjad ja laius
tree.heading("first_name", text="Eesnimi")
tree.heading("last_name", text="Perekonnanimi")
tree.heading("email", text="E-post")
tree.heading("phone", text="Telefon")
tree.heading("image", text="Pilt")

tree.column("first_name", width=150)
tree.column("last_name", width=100)
tree.column("email", width=60)
tree.column("phone", width=100)
tree.column("image", width=60)


root.mainloop()
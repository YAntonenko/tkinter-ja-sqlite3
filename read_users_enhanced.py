import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os

# Funktsioon, mis laadib andmed SQLite andmebaasist ja sisestab need Treeview tabelisse
def load_data_from_db(tree):
        # Kustuta kõik olemasolevad read treeview'st
    for item in tree.get_children():
        tree.delete(item)

        # Kontrolli, kas andmebaasi fail eksisteerib
    if not os.path.exists('movies.db'):
        messagebox.showerror("Viga", "Andmebaasi fail 'movies.db' ei leitud!")
        return

    try:
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

        print(f"Laaditud {len(rows)} kasutajat andmebaasist")

    except sqlite3.Error as e:
        messagebox.showerror("Andmebaasi viga", f"Viga andmete laadimisel: {e}")
    except Exception as e:
        messagebox.showerror("Viga", f"Ootamatu viga: {e}")

        # Funktsioon, mis kuvab valitud kasutaja andmed
def show_selected_user(event):
    selected_item = tree.selection()
    if selected_item:
        values = tree.item(selected_item[0])['values']
        print(f"Valitud kasutaja: {values[0]} {values[1]}")

# Loo põhiaken
root = tk.Tk()
root.title("Kasutajate andmebaas - movies.db")
root.geometry("800x500")

# Pealkiri
title_label = tk.Label(root, text="Kasutajate nimekiri", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Loo raam kerimistriibaga
frame = tk.Frame(root)
frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

# Kerimistriba
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Loo tabel (Treeview) andmete kuvamiseks
tree = ttk.Treeview(
    frame,
    yscrollcommand=scrollbar.set,
    columns=("first_name", "last_name", "email", "phone", "image"),
    show="headings"
)
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
tree.column("last_name", width=150)
tree.column("email", width=200)
tree.column("phone", text=120)
tree.column("image", width=80)

# Lisa sündmus valitud rea kuvamiseks
tree.bind('<<TreeviewSelect>>', show_selected_user)

# Nuppude raam
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Värskenda nupp
refresh_button = tk.Button(
    button_frame,
    text="Värskenda",
    command=lambda: load_data_from_db(tree),
    bg="#4CAF50",
    fg="white",
    padx=20,
    pady=5
)
refresh_button.pack(side=tk.LEFT, padx=5)

# Välju nupp
exit_button = tk.Button(
    button_frame,
    text="Välju",
    command=root.quit,
    bg="#f44336",
    fg="white",
    padx=20,
    pady=5
)
exit_button.pack(side=tk.LEFT, padx=5)

# Lisa andmed tabelisse esmakordsel laadimisel
load_data_from_db(tree)

# Käivita rakendus
root.mainloop()
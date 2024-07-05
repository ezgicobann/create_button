import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import *

window = tk.Tk() # bu ifade Tkinter kütüphanesinin Tk sınıfından bir nesne oluşturulmasını sağlar.
window.geometry("600x450")

window.title("Welcome to main page of my project")

def import_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        print(f'Selected file: {file_path}')
        label.config(
            text="Your file has been imported",
            bg="lightgreen",
            font=12)
    else:
        print("You did not select a file")
        label.config(
            text="Your file failed to import",
            bg="red",
            font=12)



login_btn = PhotoImage(file=r"C:\Users\Ezgi\OneDrive\Resimler\Film Rulosu\icons8-import-file-48.png")

img_label = Label(image=login_btn)


import_button = tk.Button(
    window,
    image=login_btn,
    bg="white",
    fg="blue",
    activebackground="red",
    activeforeground="white",
    #font=24,
    height=0,
    width=0,
    cursor="hand2",
    command=import_file)

import_button.pack(pady=40)


label = tk.Label(
    window,
    text = "Please press the button for import file",
    bg="lightblue",
    fg="black",
    font="12",
    wraplength=200
)


label.pack()
window.mainloop()






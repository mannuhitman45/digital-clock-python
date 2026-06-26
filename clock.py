from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    
    
    current_time = strftime("%X")
    current_day = strftime("%A")
    current_date = strftime("%x")

    label.config(
        text=f"{current_time}\n{current_day}\n{current_date}"
    )

    label.after(1000, time)

label = Label(root, font=("ds-digital", 80), background = "black", foreground = "white")
label.pack(anchor = "center")

time()

mainloop()

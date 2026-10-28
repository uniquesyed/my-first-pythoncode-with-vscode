import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
clock = tk.Label(root, font=("Arial", 40), padx=20, pady=10)
clock.pack()

def update_clock():
    clock.config(text=strftime("%H:%M:%S"))
    root.after(1000, update_clock)

update_clock()
root.mainloop()
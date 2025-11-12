import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *

root = tk.Tk()
root.title("Đăng ký học")
root.geometry("600x400")

# label
label = ttk.Label(text="Chọn cơ sở:").grid(row=3, column=0)
# create a combobox
co_so = tk.StringVar()
cbo_co_so = ttk.Combobox(root, textvariable=co_so)
cbo_co_so['values'] = ['ADV', 'LVS', 'LLQ', 'LYR']
cbo_co_so['state'] = 'readonly'




cbo_co_so.grid(row=3, column=1)


root.mainloop()
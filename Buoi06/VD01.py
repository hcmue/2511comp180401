from tkinter import *
from tkinter.messagebox import *

root = Tk()
# setting cho màn hình chính
root.title("DEMO HCMUE")
root.geometry("500x300")

ho_ten = StringVar()

def xu_ly_click():
    showinfo("Info", "Xin chào bạn: " + ho_ten.get())

# Thêm widget và gắn vào widget cha
Label(root, text="DEMO CHƠI").pack()
Label(root, text="Họ tên").pack()
Entry(root, textvariable=ho_ten).pack()
Button(root, text="Click tui đi", command=xu_ly_click).pack()
# Thêm xử lý sự kiện

root.mainloop()
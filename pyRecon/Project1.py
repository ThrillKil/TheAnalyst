from main import *
from tkinter import *
from tkinter.ttk import Combobox
from tkinter.font import Font
from tkinter import font
from tkinter import simpledialog
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

win = Tk()
win.geometry("900x600+100+50")
win.configure(background='black')
canvas1 = Canvas(win, width=450, highlightbackground='black', height=350, bg='black')
label = Label(canvas1, text="THE ANALYST", font='Times 24 bold', bg='black', fg='white').place(x=110, y=25)
photo1 = PhotoImage(file='/root/Desktop/pyRecon/Nik.png')
canvas1.create_image(10, 10, image=photo1, anchor=NW)

photo = PhotoImage(file='/root/Desktop/pyRecon/final.png')
canvas1.create_image(45, 60, image=photo, anchor=NW)
canvas1.place(x=0, y=0)

canvas2 = Canvas(win, width=450, highlightbackground='black', height=300, bg='black')
canvas2.place(x=0, y=350)

ft = Font(family='Courier', size=25, weight='bold', slant='italic')


web = Label(canvas2, text="WEBSITE SCANNER", bg='black',
            fg='yellow', font=ft).place(x=40, y=35)

l2 = Label(canvas2, text="NAME", font='Courier 18 bold',
           bg='black', fg='white').place(x=20, y=80)

e2 = Entry(canvas2, width=30, bg='#e6e6fa', bd=10).place(x=90, y=80)

l3 = Label(canvas2, text=" URL", font='Courier 18 bold',
           bg='black', fg='white').place(x=20, y=130)

e3 = Entry(canvas2, width=30, bg='#e6e6fa', bd=10).place(x=90, y=130)


def fun():
    gather_info(e2.get(), e3.get())


submit = Button(canvas2, text='Submit', font='Courier 15 bold', bd='5', fg='yellow', bg='blue', command=fun).place(x=130, y=190)


canvas3 = Canvas(win, width=444, height=300, highlightbackground='black', bg='black')

ft = Font(family='Courier', size=25, weight='bold', slant='italic')


def fun1():
       s1 = simpledialog.askstring("input", "Enter the Website name")
       s2 = simpledialog.askstring("input", "Enter the Domain name")
       t = Text(win, undo=True, background='yellow', width=60, height=20)
       t.place(x=405, y=50)


def fun2():
       s1 = simpledialog.askstring("input", "Enter the URL")
       m1 = messagebox.askquestion("exit", "do you want to check the connection")


link = Label(canvas3, text="LINK IDENTIFIER", bg='black',
            fg ='yellow', font=ft).place(x=40, y=80)

l2 = Button(canvas3, text="Generate", width=20, font='Courier 18 bold',
           fg ='red', bg='blue', command=fun1).place(x=40, y=130)


l3 = Button(canvas3, text=" Detect", width=20, font='Courier 18 bold',
           fg='red', bg='blue', command=fun2).place(x=40, y=190)

canvas3.place(x=453, y=350)

win.mainloop()

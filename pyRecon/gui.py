from main import *
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
root =Tk()
root.geometry('375x450+220+100')
root.resizable(FALSE, FALSE)


class text:
       
       pt="no file"

       def new(self):
              ans=messagebox.askquestion("save","do you want to save this file")
              if ans=="yes":
                     self.save()
              f1=self.t.delete(1.0,END)
              self.pt="no file"

       def open(self):
              res=filedialog.askopenfile(initialdir='E:\\',title="open file",filetypes=(("text files","*.txt*"),("all files","*.*")))
              if res!=None:
                     self.t.delete(1.0,END)
                     for i in res:
                            self.t.insert(END,i)
              self.pt=res.name
              res.close()
                            
       def saveas(self):
              res=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
              if res is None:
                     return
              t2=self.t.get(1.0,END)
              res.write(t2)
              res.close()

       def save(self):
              if self.pt=="no file":
                     self.saveas()
              else:
                     file=open(self.pt,'w')
                     file.write(self.t.get(1.0,END))
                     file.close()

       def copy(self):
              self.t.clipboard_clear()
              self.t.clipboard_append(self.t.selection_get())

       def cut(self):
              self.copy()
              self.t.delete("sel.first","sel.last")

       def paste(self):
              self.t.insert(INSERT,self.t.clipboard_get())

       def __init__(self,mas):
              self.mas=mas
              mas.title("new app")
              mas.config(background='#000040')
              self.t=Text(self.mas,undo=True)
              self.t.pack(fill=BOTH,expand=1)
              
              self.main_menu=Menu()
              self.mas.config(menu=self.main_menu)
              
              self.file_menu=Menu(self.main_menu,tearoff=False)
              self.main_menu.add_cascade(label='file',font='verdana 10 bold',menu=self.file_menu)
              self.file_menu.add_command(label='new',font='verana 10 bold',command=self.new)
              self.file_menu.add_command(label='open',font='verana 10 bold',command=self.open)
              self.file_menu.add_separator()
              self.file_menu.add_command(label='save',font='verana 10 bold',command=self.save)
              self.file_menu.add_command(label='save as',font='verana 10 bold',command=self.saveas)
              self.file_menu.add_separator()
           
              
              self.edit_menu=Menu(self.main_menu,tearoff=False)
              self.main_menu.add_cascade(label='edit',font='verana 10 bold',menu=self.edit_menu)
              self.edit_menu.add_command(label='copy',font='verana 10 bold',command=self.copy)
              self.edit_menu.add_command(label='cut',font='verana 10 bold',command=self.cut)
              self.edit_menu.add_command(label='paste',font='verana 10 bold',command=self.paste)
              self.edit_menu.add_separator()
              self.edit_menu.add_command(label='undo',font='verana 10 bold',command=self.t.edit_undo)
              self.edit_menu.add_command(label='redu',font='verana 10 bold',command=self.t.edit_redo)

              self.exit_menu=Menu(self.main_menu,tearoff=False)
              self.main_menu.add_cascade(label='help',font='verana 10 bold',menu=self.exit_menu)
              self.exit_menu.add_command(label='about us',font='verana 10 bold')


m = text(root)


def link():
    top = Toplevel()
    top.geometry('375x470+220+100')
    top.resizable(FALSE,FALSE)
    l1 = Label(top, text="URL",font='Times 10 bold')
    l1.place(x=100,y=100)
    e1 = Entry(top, width=25,bg='#e6e6fa',bd=10)
    e1.place(x=150,y=100)
    c=Button(top,text='Submit',width=8,bd=8,font='Times 10 bold',bg='skyblue',fg='red').place(x=200,y=150)


def webscan():
    top = Toplevel()
    top.geometry('375x470+220+100')
    l2 = Label(top, text="Name",font='Times 10 bold')
    l2.place(x=10,y=100)
    e2 = Entry(top, width=20,bg='#e6e6fa',bd=10)
    e2.place(x=50,y=100)
    l3 = Label(top, text="URL",font='Times 10 bold')
    l3.place(x=200,y=100)
    e3 = Entry(top, width=20,bg='#e6e6fa',bd=10)
    e3.place(x=230,y=100)

    def fun():
        gather_info(e2.get(), e3.get())
        # tkinter.messageboxmessagebox.showinfo("Web", "Task Completed Successfully")

    c = Button(top, text='Submit', width=8, bd=8, font='Times 10 bold', bg='skyblue', fg='red', command=fun).place(x=180, y=170)


A = Button(root, text="Link Identifier",width='20', bd=20, bg='skyblue', fg='red', font='Times 18 bold', command=link)
B = Button(root, text="Website Scanner",width='20', bd=20, bg='skyblue', fg='red', font='Times 18 bold', command=webscan)
A.place(x=20, y=80)
B.place(x=20, y=180)
root.mainloop()

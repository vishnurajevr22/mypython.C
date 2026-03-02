from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image,ImageTk

root=Tk()
root.title("submission form")
Label(root,text="name").grid(row=0)
Label(root,text="father'sname").grid(row=1)
Label(root,text="age").grid(row=2)
Label(root,text="education").grid(row=3)
Label(root,text="phno").grid(row=4)
Label(root,text="address").grid(row=5)
e1=Entry(root).grid(row=0,column=1)
e2=Entry(root).grid(row=1,column=1)
e3=Entry(root).grid(row=2,column=1)
var1=IntVar
Checkbutton(root,text=10,variable=var1).grid(row=3,column=1)
var2=IntVar
Checkbutton(root,text=12,variable=var2).grid(row=3,column=2)
var3=IntVar
Checkbutton(root,text="ug",variable=var3).grid(row=3,column=3)
var4=IntVar
Radiobutton(root,text="mobile",variable=var4,value=1).grid(row=4,column=1)
Radiobutton(root,text="landline",variable=var4,value=2).grid(row=4,column=2)
#combobox
Label(root,text="select adderss").grid(row=5,column=1)
ttk.Combobox(root,values=["home","office"],state="readonly").grid(row=5,column=2)
#ttk.Combobox.set("home")
#image
image1=PhotoImage(file="Screenshot (4).png")
Label(root,image=image1).grid(row=6,column=1)
#image button
image=Image.open("Screenshot (4).png")
image=ImageTk.PhotoImage(image)
imagebutton=Button(root,image=image).grid(row=15,column=1)
#scroolbar
Scrollbar=Scrollbar(root)
Scrollbar.grid(row=17,column=8)
Scrollbar.config(command=HORIZONTAL)

#menu
menu=Menu(root)
root.config(menu=menu)
Filemenu=Menu(menu)
menu.add_cascade(label="File",menu=Filemenu)
Filemenu.add_command(label='new')
Filemenu.add_command(label='open')
Filemenu.add_separator()
Filemenu.add_command(label="exit",command=root.quit)
mainloop()

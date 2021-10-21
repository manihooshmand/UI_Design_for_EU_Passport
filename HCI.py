from tkinter import *
from tkinter import messagebox

window = Tk(className='--EU Verification--')
window.geometry("900x1200")
window.config(bg='#2a388f')

canvas1= Canvas(window, width= 525, height= 90, bg="#2a388f", highlightthickness=0)
canvas1.create_text(0, 10 , anchor=NW, text="Welcome to EU Verification", fill="white", font=('Helvetica 15 bold'))
canvas1.pack()

canvas2 = Canvas(window , width=374 , height=218)      
canvas2.pack()
img = PhotoImage (file='4320.png')
canvas2.create_image(0,0, anchor=NW, image=img)

L0 = Label(window, text="   " , bg='#2a388f' , fg='white', highlightthickness=0)
L0.pack()

L1 = Label(window, text="First Name :" , bg='#2a388f' , fg='white', highlightthickness=0)
L1.pack(side='top')
E1 = Entry(window, bd =5)
E1.pack(side= 'top')

L2 = Label(window, text="Middle Name :" , bg='#2a388f' , fg='white', highlightthickness=0)
L2.pack(side='top')
E2 = Entry(window, bd =5)
E2.pack(side= 'top')

L3 = Label(window, text="Last Name :" , bg='#2a388f' , fg='white', highlightthickness=0)
L3.pack(side='top')
E3 = Entry(window, bd =5)
E3.pack(side= 'top')

L4 = Label(window, text="Gender :" , bg='#2a388f' , fg='white', highlightthickness=0)
L4.pack()
var = StringVar()
opt1 = Radiobutton(window, text="MALE    ", bg='white' , fg='black', highlightthickness=0, variable=var, value="MALE")
opt1.pack()
opt2 = Radiobutton(window, text="FEMALE", bg='white' , fg='black', highlightthickness=0, variable=var, value="FEMALE")
opt2.pack()

L5 = Label(window, text="   " , bg='#2a388f' , fg='white', highlightthickness=0)
L5.pack()

mb =  Menubutton ( window, text="Nationality :",bg='white' , fg='black')
mb.pack()
mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu
German = StringVar()
French = StringVar()
Italian = StringVar()
mb.menu.add_checkbutton ( label="German", variable= German )
mb.menu.add_checkbutton ( label="French", variable= French )
mb.menu.add_checkbutton ( label="Italian", variable= Italian )
mb.pack()

L7 = Label(window, text="   " , bg='#2a388f' , fg='white', highlightthickness=0)
L7.pack()

L6 = Label(window, text="Passport Code :" , bg='#2a388f' , fg='white', highlightthickness=0)
L6.pack(side='top')
E6 = Entry(window, bd =5)
E6.pack(side= 'top')

L8 = Label(window, text="   " , bg='#2a388f' , fg='white', highlightthickness=0)
L8.pack()

def hello():
    messagebox.showinfo("Success !", "Your request for EU Verification Succeeded")
B = Button(window, text ="SUBMIT", bg='#1AB9D9' ,fg='white' , command=hello)
B.pack()

window.mainloop()
from tkinter import *
from tkinter import messagebox
import ast

win=Tk()
win.title('Login')
win.geometry('925x500+300+200')
win.configure(bg="#fff")
win.resizable(False,False)
icon = PhotoImage(file="icon.png")
win.iconphoto(False, icon)

def signup():
    username=user.get() 
    password=code.get()
    confirm_password=confirm_code.get()
    if password==confirm_password:
        try:
            file=open('datasheet.txt','r+')
            d=file.read()
            r=ast.literal_eval(d)

            dict2={username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file=open('datasheet.txt','w')
            w=file.write(str(r))
        except:
            file=open('datasheet.txt','w')
            pp=str({'Username':'password'})
            file.write(pp)
            file.close()
        else:
            messagebox.showerror('Invalid',"Both Password should match")

# def sign():
#     win.
        
        


img=PhotoImage(file='signup.png')
Label(win,image=img,bg='white').place(x=50,y=90)
frame=Frame(win,width=400,height=400,bg="white")
frame.place(x=480,y=70)


heading=Label(frame,text='Sign up ',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=100,y=5)

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
user =Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username/Email')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)


def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password') 
code =Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)


def on_enter(e):
    confirm_code.delete(0,'end')

def on_leave(e):
    name=confirm_code.get()
    if name=='':
        confirm_code.insert(0,'Confirm Password') 
confirm_code =Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
confirm_code.place(x=30,y=220)
confirm_code.insert(0,'Confirm Password')
confirm_code.bind('<FocusIn>',on_enter)
confirm_code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)


Button(frame,width=39,pady=7,text='Sign up',bg='blue',fg='white',border=0,command=signup).place(x=35,y=280)
label=Label(frame,text="I have an account ",fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
label.place(x=90,y=340)
signin=Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8').place(x=200,y=340)


















win.mainloop()
from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox


GUI = Tk() #นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #นี่คือชชื่อโปรแกรม
GUI.geometry('600x500') #นี่คือขนาดโปรแกรม

L1 = Label(GUI,text='โปรแกรมบันทึกความรู้' ,font=('Angsana New',45),fg='red')
L1.place(x=30,y=20)
#####################
def Button2():
    text = 'การทำปุ่มบันทึกข้อมูล'
    messagebox.showinfo('เรียนเรื่องอะไร',text)
FB1 = Frame(GUI)#คล้ายกระดาน
FB1.place(x=100,y=100)
B2 = ttk.Button(FB1,text='เวันนี้เรียนเรืองอะไร',command=Button2)
B2.pack(ipadx=20,ipady=20)

##################3##
def Button3():
    text3 = 'Python 101, Math'
    messagebox.showinfo('เรียนวิชาอะไร',text3)
FB1 = Frame(GUI)#คล้ายกระดาน
FB1.place(x=100,y=250)
B2 = ttk.Button(FB1,text='เรียนวิชาอะไร',command=Button3)
B2.pack(ipadx=20,ipady=20)

####################
def Button4():
    text4 = 'เรียนวันอังคารกับวันศุกร์'
    messagebox.showinfo('เรียนวันไหน',text4)
FB1 = Frame(GUI)#คล้ายกระดาน
FB1.place(x=300,y=100)
B2 = ttk.Button(FB1,text='เรียนวันไหน',command=Button4)
B2.pack(ipadx=20,ipady=20)

####################
def Button5():
    text5 = 'Uncle Engineer'
    messagebox.showinfo('เรียนกับใคร',text5)
FB1 = Frame(GUI)#คล้ายกระดาน
FB1.place(x=300,y=250)
B2 = ttk.Button(FB1,text='เรียนกับใคร',command=Button5)
B2.pack(ipadx=20,ipady=20)

####################

GUI.mainloop()

import mysql.connector
import tkinter
from tkinter import *
gui = tkinter.Tk()
con = mysql.connector.connect(
    host='localhost', user='root', password='', database='onlineexam')
cur = con.cursor()


qid=StringVar()
qname=StringVar()
op1=StringVar()
op2=StringVar()
op3=StringVar()
op4=StringVar()


def start():
    q="SELECT * FROM onlineexam WHERE  QID=1 "
    cur.execute(q)
    for row in cur:
        qid.set(row[0])
        qname.set(row[1])
        op1.set(row[2])
        op2.set(row[3])
        op3.set(row[4])
        op4.set(row[5])
        
        
def nxt():
    id=int(qid.get())
    id=id+1
    q="SELECT * FROM onlineexam WHERE  QID= "+str(id)
    cur.execute(q)
    for row in cur:
        qid.set(row[0])
        qname.set(row[1])
        op1.set(row[2])
        op2.set(row[3])
        op3.set(row[4])
        op4.set(row[5])
    

def pre():
    id=int(qid.get())
    id=id-1
    q="SELECT * FROM onlineexam WHERE  QID= "+str(id)
    cur.execute(q)
    for row in cur:
        qid.set(row[0])
        qname.set(row[1])
        op1.set(row[2])
        op2.set(row[3])
        op3.set(row[4])
        op4.set(row[5])


gui.geometry("400x500")
gui.minsize(200, 300)
gui.config(bg="#799096")
gui.title("ONLINE-EXAM")

l=Label(text="ONLINE-EXAM",bg="SILVER",fg="red",font="lucida 13 bold",border=4,relief=SUNKEN)
l.pack(pady=10,fill="y")


b=Button(gui,text="<Start Exam>",font="lucida 13 bold",command=start).place(x=20,y=70)
l1=Label( textvariable=qid,fg="red").place(x=30,y=120)
qn=Label( textvariable=qname,fg="red").place(x=130,y=120)


r1=Radiobutton(gui,value="1",text="",fg="red",textvariable=op1).place(x=20,y=185)
r2=Radiobutton(gui,value="2",text="",fg="red",textvariable=op2).place(x=20,y=220) 
r3=Radiobutton(gui,value="3",text="",fg="red",textvariable=op3).place(x=20,y=255)
r4=Radiobutton(gui,value="4",text="",fg="red",textvariable=op4).place(x=20,y=290)

b3=Button(gui,text="CONFERM",fg="red",bg="Aqua",font="lucida 13 bold").place(x=150,y=330)

b1=Button(gui,text="<Pre",fg="red",bg="Aqua",font="lucida 13 bold",command=pre).place(x=20,y=400)
b2=Button(gui,text="Next>",fg="red",bg="Aqua",font="lucida 13 bold",command=nxt).place(x=220,y=400)


gui.mainloop()
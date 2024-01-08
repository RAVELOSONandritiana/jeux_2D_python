from tkinter import *
from itertools import *
def active_processus():
    global mot
    for j in count(1):
        if j%2==0:mot = mot
        else:mot = mot[::-1]
        for i in str(list(permutations(mot))):
            l = []
            l.append(i)

mot = "RAVELOSON ANDRITIANA MICHEL RAVELOSON ANDRITIANA MICHEL RAVELOSON ANDRITIANA MICHEL RAVELOSON ANDRITIANA MICHELRAVELOSON ANDRITIANA MICHEL RAVELOSON ANDRITIANA MICHEL RAVELOSON ANDRITIANA MICHEL RAVELOSON ANDRITIANA MICHEL"*1000000
fen = Tk()
fen.geometry("500x500")
fen.resizable(False,False)
fen.title("Ram Pc")

can = Canvas(fen,height=500,width=500,bg="grey")
can.pack()

but = Button(can,text="ACTIVE",font=("Helvetica",20,"italic"),bg="green",fg="red",height=2,width=20,command=active_processus)
but.place(x=80,y=220)


fen.mainloop()

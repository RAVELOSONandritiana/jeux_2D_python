from tkinter import*
from math import*
def dessiner_oscillation():
    global l_coord
    f = lambda x:sin(x)
    for i in range(0,360,20):
        pos = f(i)
        x1=20+i
        y1=200-pos*100
        x2=20+i+5
        y2=200-pos*100+5
        x_milieu=(x2+x1)//2
        y_milieu=(y2+y1)//2
        l_coord.append([x_milieu,y_milieu])
        can.create_oval(x1,y1,x2,y2,outline="blue",fill="blue")
def tracer_ligne():
    global l_coord
    print(len(l_coord))
    for i in range(0,len(l_coord)):
        if i < len(l_coord)-1:can.create_line(l_coord[i][0],l_coord[i][1],l_coord[i+1][0],l_coord[i+1][1],fill="red")
l_coord = []
fen = Tk()
fen.geometry("400x400")
fen.resizable(False,False)
can = Canvas(fen,height=400,width=400,bg="grey")
can.pack()
can.create_line(20,200,380,200,fill="black",arrow=LAST)
can.create_line(20,20,20,380,fill="black",arrow=FIRST)
for i in range(1,9):
    can.create_line(40*(i)+20,200-5,40*(i)+20,200+5,fill="black")
dessiner_oscillation()
tracer_ligne()
fen.mainloop()

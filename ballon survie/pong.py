from tkinter import *
from random import *
from math import sqrt
pas = randint(2,4)
p = 2
niveau = 10
autorisation = 1
def change_y():
    global pas,p
    pas = randint(2,4)
    p = randint(1,3)
def descend():
	global pas
	can.move(boule,0,p)
def monter():
	global pas
	can.move(boule,0,-p)
def gauche():
	global pas
	can.move(boule,-pas,0)
def droite():
	global pas
	can.move(boule,pas,0)

def des_g():
	descend()
	gauche()
def des_d():
	descend()
	droite()
def mon_g():
	monter()
	gauche()
def mon_d():
	monter()
	droite()

def verify_coords():
	global chemin,deplacer,autorisation,vie,score
	distance = collide_circle(rak,boule,20,20)
	if distance < 0 and vie > 0:
		vie-=100
		if vie <= 0:
			can.create_text(w//2,h//2,text="GAME OVER",fill="grey",font=("bold",40))
			autorisation = 0
			chemin = "pause"
			with open ("score.txt","a") as fichier:
				fichier.write(str(score))
				fichier.write("\n")
            
def move_():
    global chemin,cpt,autorisation,condition
    dep()
    if cpt == condition and autorisation == 1:create_bonus()
    
    norme()
    c = can.coords(boule)
    verify_coords()
    if autorisation == 1:
        if c[0]<=0:chemin = 0;change_y()
        if c[1]<=0:chemin = 1;change_y()
        if c[2]>=w:chemin = 2;change_y()
        if c[3]>=h-10:chemin = 3;change_y()
        
        if chemin == 0:mon_d()
        if chemin == 1:des_d()
        if chemin == 2:des_g()
        if chemin == 3:mon_g()
    cpt+=1
    can.after(niveau,move_)
def norme():
    if autorisation == 1:
        c = can.coords(rak)
        if c[3]<h-10:
            can.move(rak,0,5)
def sauter(event):
    if autorisation == 1:
        c = can.coords(rak)
        can.move(rak,0,-100)

def rak_g(event):
    if autorisation == 1:
        c = can.coords(rak)
        if c[0] >= 20:
            can.move(rak,-20,0)
def rak_d(event):
    if autorisation == 1:
        c = can.coords(rak)
        if c[2] <= w-20:
            can.move(rak,20,0)

def create_bonus():
    global cpt,condition
    for i in range(1,randint(1,5)):
        p = can.create_oval(0,0,10,10,fill=choice(["blue","black","green"]),tag="bonus")
        can.move(p,randint(10,w-9),0)
    cpt = 0
    condition = randint(200,300)
def dep():
    global score,autorisation,vie
    for i in can.find_withtag("bonus"):
        distance = collide_circle(i,rak,20,5)
        col = can.itemcget(i,'fill')
        if autorisation == 1:
            can.move(i,0,3)
            c = can.coords(i)
            if c[1] >= h and col == 'blue':
                score+=1
                can.delete(i)
        if distance < 0 and col == 'blue':
            if vie == 0:
                chemin = "pause"
            autorisation = 0 if vie <= 0 else 1
            vie-=50
        elif distance < 0 and col == 'black':
            vie+=1000
            can.delete(i)
        elif distance < 0 and col == 'green':
            score+=20
            can.delete(i)
    can.itemconfig(aff_score,text=str(score))
    can.itemconfig(life,text=str(vie))
def collide_circle(rak,boule,rayon1,rayon2):
    s_1 = can.coords(rak)
    s_2 = can.coords(boule)
    centre_x_s_1 = (s_1[2]+s_1[0])/2
    centre_y_s_1 = (s_1[3]+s_1[1])/2
    centre_x_s_2 = (s_2[2]+s_2[0])/2
    centre_y_s_2 = (s_2[3]+s_2[1])/2
    distance = sqrt((centre_x_s_2-centre_x_s_1)**2+(centre_y_s_2-centre_y_s_1)**2)-(rayon1+rayon2)
    return distance
w=400
h=400
cpt = 150
condition = 200
chemin=0
score = 0
vie = 2000
fen = Tk()
fen.geometry(f"{w}x{h}")
fen.resizable(False,False)

can = Canvas(fen,height=h,width=w,bg="grey")
can.pack()

im = PhotoImage(file="back.png")
im = im.subsample(2)
can.create_image(0,0,image=im,anchor="center")

rak = can.create_oval(0,0,40,40,fill="red")
can.move(rak,(w//2)-20,h-50)

aff_score = can.create_text(20,20,text=str(score),fill="green",font=("Helvetica",15))
life = can.create_text(w-40,20,text=str(vie),fill="black",font=("Helvetica",15))

boule = can.create_oval(40,40,80,80,fill="blue")
move_()

can.create_rectangle(0,h-10,w,h,fill="black")

can.bind_all("<Left>",rak_g)
can.bind_all("<Right>",rak_d)
can.bind_all("<Up>",sauter)


fen.mainloop()


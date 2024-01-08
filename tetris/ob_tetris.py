from tkinter import *
from random import *
from math import *
class Tetris(object):
    def __init__(self,HEIGHT=600,WIDTH=400):
        self.fen = Tk()
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.rayon = 20
        self.tourne_zed = 0
        self.tourne_vertical = 0
        self.tourne_tri = 0
        self.objet = 0
        self.dir = ""
        self.tag_move = ""
        self.color = ["#FF0900","#D718BE","#1A7ADC","#929FAD","#D0CE18","#2ECA2D"]
        self.fen.title("tetris game python")
        self.fen.resizable(False,False)
        self.fen.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.can = Canvas(self.fen,height=self.HEIGHT,width=self.WIDTH,bg="grey")
        self.can.pack()
#la base du jeu tout entier , la methode dep
        self.dep()
        self.can.bind_all("<Left>",self.direction)
        self.can.bind_all("<Right>",self.direction)
        self.fen.mainloop()

    def destroy_bas(self):
        if len(list(self.can.find_withtag("stop")))>=20 and len(list(filter(lambda x:self.can.coords(x)[3]==self.HEIGHT,list(self.can.find_withtag("stop")))))>=18:
            for i in self.can.find_withtag("stop"):
                if self.can.coords(i)[3] == self.HEIGHT:
                    self.can.delete(i)
            for j in self.can.find_withtag("stop"):
                self.can.move(j,0,self.rayon)


    def create_objet(self):
        randFonc = randint(0,3)
        if randFonc == 0:self.carre()
        if randFonc == 1:self.vertical()
        if randFonc == 2:self.tri()
        if randFonc == 3:self.zed()

    def carre(self):
        self.tag_move = "carre"
        c=choice(self.color)
        for i in range(2):
            for j in range(2):
                x1 = i*self.rayon
                y1 = j*self.rayon
                x2 = x1+self.rayon
                y2 = y1+self.rayon
                self.can.create_rectangle(x1,y1,x2,y2,fill=c,tag="carre")
        for i in self.can.find_withtag("carre"):
            self.can.move(i,180,0)
    
    def vertical(self):
        self.tourne_vertical = 0
        c=choice(self.color)
        self.tag_move = "vertical"
        for i in range(1):
            for j in range(4):
                x1 = i*self.rayon
                y1 = j*self.rayon
                x2 = x1+self.rayon
                y2 = y1+self.rayon
                self.can.create_rectangle(x1,y1,x2,y2,fill=c,tag="vertical")
        for i in self.can.find_withtag("vertical"):
            self.can.move(i,180,0)

    def tri(self):
        self.tag_move = "tri"
        c=choice(self.color)
        self.can.create_rectangle(20,0,40,20,fill=c,tag="tri")
        for i in range(3):
            for j in range(1):
                x1 = i*self.rayon
                y1 = j*self.rayon+self.rayon
                x2 = x1+self.rayon
                y2 = y1+self.rayon
                self.can.create_rectangle(x1,y1,x2,y2,fill=c,tag="tri")
        for i in self.can.find_withtag("tri"):
            self.can.move(i,180,0)

    def zed(self):
        self.tourne_zed = 0
        self.tag_move = "zed"
        c=choice(self.color)
        for i in range(2):
            for j in range(3):
                #i = 1 and j = 0
                #i = 0 and j = 2
                if i == 1 and j == 0:
                    continue
                if i == 0 and j == 2:
                    continue
                x1 = i*self.rayon
                y1 = j*self.rayon
                x2 = x1+self.rayon
                y2 = y1+self.rayon
                self.can.create_rectangle(x1,y1,x2,y2,fill=c,tag="zed")
        for i in self.can.find_withtag("zed"):
            self.can.move(i,180,0)

    def collision(self,tete,bonus):
        distance = 0
        x1=self.can.coords(tete)[0]
        y1=self.can.coords(tete)[1]
        x2=self.can.coords(tete)[2]
        y2=self.can.coords(tete)[3]

        x_milieu = x2-x1//2
        y_milieu = y2-y1//2

        #pour le bonus
        x1=self.can.coords(bonus)[0]
        y1=self.can.coords(bonus)[1]
        x2=self.can.coords(bonus)[2]
        y2=self.can.coords(bonus)[3]

        x2_milieu = x2-x1//2
        y2_milieu = y2-y1//2

        distance = sqrt((x2_milieu-x_milieu)**2+(y2_milieu-y_milieu)**2)-self.rayon

        return distance

    def distY(self,objet1,objet2):
        y1 = self.can.coords(objet1)[1]
        y2 = self.can.coords(objet2)[3]
        return y2-y1

    def dep(self):
        self.test_bas = 1
        self.test_gauche = 1
        self.test_droite = 1
        self.destroy_bas()
        if self.tag_move == "zed":self.can.bind_all("<Up>",self.turn_zed)
        if self.tag_move == "vertical":self.can.bind_all("<Up>",self.turn_vertical)
        if self.tag_move == "tri":self.can.bind_all("<Up>",self.turn_tri)

        if self.objet == 0:
            self.create_objet()
            self.objet = 1
        if self.objet == 1:
            for i in self.can.find_withtag(self.tag_move):
                if self.can.coords(i)[3] == self.HEIGHT:
                    self.test_bas = 0
                    for el in self.can.find_withtag(self.tag_move):
                        self.can.itemconfig(el,tag="stop")
                        self.objet = 0

            if len(list(self.can.find_withtag("stop")))>0:
                for j in self.can.find_withtag("stop"):
                    for el in self.can.find_withtag(self.tag_move):
                        if self.collision(el,j)==-self.rayon//2 and self.distY(j,el)==0:
                            for k in self.can.find_withtag(self.tag_move):
                                self.can.itemconfig(k,tag="stop")
                                self.objet = 0
            for i in self.can.find_withtag(self.tag_move):
                if self.can.coords(i)[0] == 0:
                    self.test_gauche = 0
                    self.test_droite = 1

                if self.can.coords(i)[2] == self.WIDTH:
                    self.test_droite = 0
                    self.test_gauche = 1
        
            if self.test_bas == 1:
                if self.dir == "Left" and self.test_gauche > 0:
                    for i in self.can.find_withtag(self.tag_move):
                        self.can.move(i,-self.rayon,0)
                if self.dir == "Right" and self.test_droite > 0:
                    for i in self.can.find_withtag(self.tag_move):
                        self.can.move(i,self.rayon,0)
                for i in self.can.find_withtag(self.tag_move):
                        self.can.move(i,0,1)
                self.dir = ""
        self.can.after(5,self.dep)

    def direction(self,event):
        if event.keysym == "Left":
            self.dir = "Left"
        if event.keysym == "Right":
            self.dir = "Right"

    def turn_zed(self,event):
        self.tourne_zed += 1
        top = 0
        if self.tourne_zed%2:
            for i in self.can.find_withtag("zed"):
                value = self.can.coords(i)
                if top != 1:
                    if top == 0:
                        x1 = value[0]-self.rayon
                        y1 = value[1]+self.rayon
                        x2 = value[2]-self.rayon
                        y2 = value[3]+self.rayon
                    if top == 2:
                        x1 = value[0]-self.rayon
                        y1 = value[1]-self.rayon
                        x2 = value[2]-self.rayon
                        y2 = value[3]-self.rayon
                    if top == 3:
                        x1 = value[0]
                        y1 = value[1]-self.rayon*2
                        x2 = value[2]
                        y2 = value[3]-self.rayon*2
                    self.can.coords(i,x1,y1,x2,y2)
                top+=1
        else:
            for i in self.can.find_withtag("zed"):
                value = self.can.coords(i)
                if top != 1:
                    if top == 0:
                        x1 = value[0]+self.rayon
                        y1 = value[1]-self.rayon
                        x2 = value[2]+self.rayon
                        y2 = value[3]-self.rayon
                    if top == 2:
                        x1 = value[0]+self.rayon
                        y1 = value[1]+self.rayon
                        x2 = value[2]+self.rayon
                        y2 = value[3]+self.rayon
                    if top == 3:
                        x1 = value[0]
                        y1 = value[1]+self.rayon*2
                        x2 = value[2]
                        y2 = value[3]+self.rayon*2
                    self.can.coords(i,x1,y1,x2,y2)
                top+=1

    def turn_vertical(self,event):
        self.tourne_vertical += 1
        degre = 2
        manisa = 0
        if self.tourne_vertical%2==1:
            for i in self.can.find_withtag("vertical"):
                if manisa == 2:
                    manisa+=1
                    continue
                value = self.can.coords(i)
                if manisa == 0 or manisa == 1:
                    x1 = value[0]-self.rayon*degre
                    y1 = value[1]+self.rayon*degre
                    x2 = value[2]-self.rayon*degre
                    y2 = value[3]+self.rayon*degre
                    degre-=1
                if manisa == 3:
                    x1 = value[0]+self.rayon
                    y1 = value[1]-self.rayon
                    x2 = value[2]+self.rayon
                    y2 = value[3]-self.rayon
                manisa += 1
                self.can.coords(i,x1,y1,x2,y2)
        else:
            for i in self.can.find_withtag("vertical"):
                if manisa == 2:
                    manisa+=1
                    continue
                value = self.can.coords(i)
                if manisa == 0 or manisa == 1:
                    x1 = value[0]+self.rayon*degre
                    y1 = value[1]-self.rayon*degre
                    x2 = value[2]+self.rayon*degre
                    y2 = value[3]-self.rayon*degre
                    degre-=1
                if manisa == 3:
                    x1 = value[0]-self.rayon
                    y1 = value[1]+self.rayon
                    x2 = value[2]-self.rayon
                    y2 = value[3]+self.rayon
                manisa += 1
                self.can.coords(i,x1,y1,x2,y2)

    def turn_tri(self,event):
        self.tourne_tri += 1
        if self.tag_move == "tri":
            if self.tourne_tri == 1:
                pos = 0
                for element in self.can.find_withtag("tri"):
                    value = self.can.coords(element)
                    if pos == 0:
                        x1 = value[0]-self.rayon
                        y1 = value[1]+self.rayon
                        x2 = value[2]-self.rayon
                        y2 = value[3]+self.rayon
                    if pos == 1:
                        x1 = value[0]+self.rayon
                        y1 = value[1]+self.rayon
                        x2 = value[2]+self.rayon
                        y2 = value[3]+self.rayon
                    #LA POSITION 2 NE BOUGE JAMAIS
                    if pos == 2:
                        x1 = value[0]
                        y1 = value[1]
                        x2 = value[2]
                        y2 = value[3]
                    if pos == 3:
                        x1 = value[0]-self.rayon
                        y1 = value[1]-self.rayon
                        x2 = value[2]-self.rayon
                        y2 = value[3]-self.rayon
                    self.can.coords(element,x1,y1,x2,y2)
                    pos+=1
            ######################pour la deuxieme position
            
            if self.tourne_tri == 2:
                pos = 0
                for element in self.can.find_withtag("tri"):
                    value = self.can.coords(element)
                    if pos == 0:
                        x1 = value[0]+self.rayon
                        y1 = value[1]+self.rayon
                        x2 = value[2]+self.rayon
                        y2 = value[3]+self.rayon
                    if pos == 1:
                        x1 = value[0]+self.rayon
                        y1 = value[1]-self.rayon
                        x2 = value[2]+self.rayon
                        y2 = value[3]-self.rayon
                    #LA POSITION 2 NE BOUGE JAMAIS
                    if pos == 2:
                        x1 = value[0]
                        y1 = value[1]
                        x2 = value[2]
                        y2 = value[3]
                    if pos == 3:
                        x1 = value[0]-self.rayon
                        y1 = value[1]+self.rayon
                        x2 = value[2]-self.rayon
                        y2 = value[3]+self.rayon
                    self.can.coords(element,x1,y1,x2,y2)
                    pos+=1

            if self.tourne_tri == 3:
                pos = 0
                for element in self.can.find_withtag("tri"):
                    value = self.can.coords(element)
                    if pos == 0:
                        x1 = value[0]+self.rayon
                        y1 = value[1]-self.rayon
                        x2 = value[2]+self.rayon
                        y2 = value[3]-self.rayon
                    if pos == 1:
                        x1 = value[0]-self.rayon
                        y1 = value[1]-self.rayon
                        x2 = value[2]-self.rayon
                        y2 = value[3]-self.rayon
                    #LA POSITION 2 NE BOUGE JAMAIS
                    if pos == 2:
                        x1 = value[0]
                        y1 = value[1]
                        x2 = value[2]
                        y2 = value[3]
                    if pos == 3:
                        x1 = value[0]+self.rayon
                        y1 = value[1]+self.rayon
                        x2 = value[2]+self.rayon
                        y2 = value[3]+self.rayon
                    self.can.coords(element,x1,y1,x2,y2)
                    pos+=1

            if self.tourne_tri == 4:
                pos = 0
                for element in self.can.find_withtag("tri"):
                    value = self.can.coords(element)
                    if pos == 0:
                        x1 = value[0]-self.rayon
                        y1 = value[1]-self.rayon
                        x2 = value[2]-self.rayon
                        y2 = value[3]-self.rayon
                    if pos == 1:
                        x1 = value[0]-self.rayon
                        y1 = value[1]+self.rayon
                        x2 = value[2]-self.rayon
                        y2 = value[3]+self.rayon
                    #LA POSITION 2 NE BOUGE JAMAIS
                    if pos == 2:
                        x1 = value[0]
                        y1 = value[1]
                        x2 = value[2]
                        y2 = value[3]
                    if pos == 3:
                        x1 = value[0]+self.rayon
                        y1 = value[1]-self.rayon
                        x2 = value[2]+self.rayon
                        y2 = value[3]-self.rayon
                    self.can.coords(element,x1,y1,x2,y2)
                    pos+=1
                self.tourne_tri = 0

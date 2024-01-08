from tkinter import *
class Fanorona(object):
    """Objet de creation du jeux fanorona 3x3"""
    def __init__(self):
        self.mv = 0
        self.coord_base = [
                                [0,0,50,50,"A00"],
                                [175,0,225,50,"A10"],
                                [350,0,400,50,"A20"],
                                [0,175,50,225,"B00"],
                                [175,175,225,225,"B10"],
                                [350,175,400,225,"B20"],
                                [0,350,50,400,"C00"],
                                [175,350,225,400,"C10"],
                                [350,350,400,400,"C20"]
                            ]
        self.objet = 1
        self.fen = Tk()
        self.tmp_color = ""
        self.fen.title("FANORONA")
        self.fen.geometry("400x400")
        self.can = Canvas(self.fen,height=400,width=400,bg="black")
        self.can.pack()
        self.can.create_rectangle(20,20,380,380,fill="grey")
        self.create_line_fanorona()
        self.can.bind_all("<Button-1>",self.change)
        self.fen.mainloop()

    def create_line_fanorona(self):
        self.can.create_line(0,0,400,400,fill="black",width=20)
        self.can.create_line(0,400,400,0,fill="black",width=20)
        self.can.create_line(200,0,200,400,fill="black",width=20)
        self.can.create_line(0,200,400,200,fill="black",width=20)
        cpt = 0
        rayon = 20
        for i in self.coord_base:
            x1,y1,x2,y2 = i[0:-1]
            x_milieu = (x1+x2)//2 
            y_milieu = (y1+y2)//2
            if cpt == 0 or cpt == 1 or cpt == 2:
                self.can.create_oval(x_milieu-rayon,y_milieu-rayon,x_milieu+rayon,y_milieu+rayon,fill="red",tag=self.coord_base[cpt][4])
            if cpt == 6 or cpt == 7 or cpt == 8:
                self.can.create_oval(x_milieu-rayon,y_milieu-rayon,x_milieu+rayon,y_milieu+rayon,fill="blue",tag=self.coord_base[cpt][4])
            cpt += 1

    def change(self,event):
        self.mv += 1
        if self.mv == 1:
            for element in self.can.find_closest(event.x,event.y):
                if self.can.itemcget(element,"fill") != "black" and self.can.itemcget(element,"fill") != "grey":
                    self.objet = element
                    self.tmp_color = self.can.itemcget(self.objet,"fill")
                    self.can.itemconfig(self.objet,fill="green")
                    break
        index = 0
        if self.mv == 2:
            x,y = event.x,event.y
            if 0<x<50 and 0<y<50:index = 0
            if 175<x<225 and 0<y<50:index = 1
            if 350<x<400 and 0<y<50:index = 2
            if 0<x<50 and 175<y<225:index = 3
            if 175<x<225 and 175<y<225:index = 4
            if 350<x<400 and 175<y<225:index = 5
            if 0<x<50 and 350<y<400:index = 6
            if 175<x<225 and 350<y<400:index = 7
            if 350<x<400 and 350<y<400:index = 8
            rayon = 20
            x1,y1,x2,y2 = self.coord_base[index][:-1]
            x_milieu = (x1+x2)//2
            y_milieu = (y1+y2)//2
            self.can.coords(self.objet,x_milieu-rayon,y_milieu-rayon,x_milieu+rayon,y_milieu+rayon)
            new_tag = self.can.itemcget(self.objet,"tag")
            new_tag = new_tag[:-1]
            self.can.itemconfig(self.objet,fill=self.tmp_color,tag=new_tag)
            print(new_tag)
            self.objet = 0
            self.tmp_color = ""
            self.mv = 0

    def verification(self):
        for i in self.coord_base:
            self.can.create_rectangle(i[0],i[1],i[2],i[3],fill="green")

fanorona3 = Fanorona()
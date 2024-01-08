from tkinter import*
from random import randint,choice
from math import *
import os
def game_over():
    global situation,HEIGHT,WIDTH
    for i in liste_corps:
        x1,y1,x2,y2=can.coords(i)
        if x1 < 0 or y1 < 0 or x2 > WIDTH or y2 > HEIGHT:
            can.create_text(WIDTH//2,HEIGHT//2,text="GAME OVER",font=("Helvetica",40))
            situation = "mort"
def collision(bonus,tete):
    global rayon
    #pour la tete du serpent
    x1=can.coords(tete)[0]
    y1=can.coords(tete)[1]
    x2=can.coords(tete)[2]
    y2=can.coords(tete)[3]

    x_milieu = x2-x1//2
    y_milieu = y2-y1//2

    #pour le bonus
    x1=can.coords(bonus)[0]
    y1=can.coords(bonus)[1]
    x2=can.coords(bonus)[2]
    y2=can.coords(bonus)[3]

    x2_milieu = x2-x1//2
    y2_milieu = y2-y1//2

    distance = sqrt((x2_milieu-x_milieu)**2+(y2_milieu-y_milieu)**2)-rayon

    return distance

def create_bonus():
    global rayon,liste_corps
    diametre = rayon*2
    x = choice(list(range(rayon,WIDTH,diametre)))
    y = choice(list(range(rayon,HEIGHT,diametre)))
    can.create_oval(x-rayon,y-rayon,x+rayon,y+rayon,fill="orange",tag="bonus")
    print("mifandona22222222222222222222222".replace('2',''))
    for i in liste_corps[1:]:
        for bonus in can.find_withtag("bonus"):
            if collision(bonus,i)<0:
                print("mifandona22222222222222222222222")
                can.delete(bonus)
                create_bonus_carre()

def move_snake():
    global liste_corps,sens,situation,score,time_after,rayon,HEIGHT,WIDTH,jeux_situation
    diametre = rayon*2
    game_over()
    tete = liste_corps[0]
    list_coords = [can.coords(i) for i in liste_corps]
    for i in liste_corps[1:]:
        if collision(i,tete)<0:
            can.create_text(HEIGHT//2,WIDTH//2,text="GAME OVER",font=("Helvetica",40))
            situation = "mort"
    if situation == "vivant" and jeux_situation%2:
        if sens == "gauche":
            can.move(tete,-diametre,0)
        if sens == "droite":
            can.move(tete,diametre,0)
        if sens == "bas":
            can.move(tete,0,diametre)
        if sens == "haut":
            can.move(tete,0,-diametre)

        habituel = 0
        for i in liste_corps[1:]:
            can.coords(i,list_coords[habituel])
            habituel+=1
        for i in can.find_withtag("bonus"):
            if collision(i,tete)<0:
                can.delete(i)
                score+=1
                fen.title(f"{score}")
                create_bonus()
                liste_corps.append(can.create_oval(list_coords[-1],fill="red",tag="corps"))
    can.after(time_after,move_snake)

def modif_sens(event):
    global sens,jeux_situation
    if event.keysym == "Left" and sens != "droite":
        sens = "gauche"
    if event.keysym == "Right" and sens != "gauche":
        sens = "droite"
    if event.keysym == "Up" and sens != "bas":
        sens = "haut"
    if event.keysym == "Down" and sens != "haut":
        sens = "bas"
    if event.keysym == "space":
        jeux_situation += 1
rayon = 10
jeux_situation = 0
score = 0
situation = "vivant"
sens = "droite"
taille_debut = 4
time_after = 200
HEIGHT = 600
WIDTH = 600
fen = Tk()
fen.geometry(f"{WIDTH}x{HEIGHT}+1000+0")
fen.title("Snake python")
fen.resizable(False,False)

liste_corps = []

can = Canvas(fen,height=HEIGHT,width=WIDTH,bg="grey")
can.pack()
p=HEIGHT//3-rayon
#####################################################################
for i in range(taille_debut):
    if i == 0:
        tete = can.create_oval(p-rayon-(i*rayon*2),p-rayon,p+rayon-(i*rayon*2),p+rayon,fill="blue",tag="tete")
        liste_corps.append(tete)
    else:
        corps = can.create_oval(p-rayon-(i*rayon*2),p-rayon,p+rayon-(i*rayon*2),p+rayon,fill="red",tag="corps")
        liste_corps.append(corps)
move_snake()
create_bonus()
#####################################################################
can.bind_all("<Up>",modif_sens)
can.bind_all("<Left>",modif_sens)
can.bind_all("<Right>",modif_sens)
can.bind_all("<Down>",modif_sens)
can.bind_all("<space>",modif_sens)
fen.mainloop()
with open("data_snake.andry","a") as fichier:
    fichier.write(f"{str(len(liste_corps)-taille_debut)}\n")
with open("data_snake.andry","r") as fichier:
    liste_score = fichier.readlines()
    score_max_save = max(map(int,liste_score))
    print(f"score max      : {score_max_save}")
    print(f"score manquant : {score_max_save-(len(liste_corps)-taille_debut)}")

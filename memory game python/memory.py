from tkinter import*
import os
from random import*
import time
def create_plateau(color):
    global distance,NB_PLATEAU,TAILLE_CARREAU
    for i in range(NB_PLATEAU):
        for j in range(NB_PLATEAU):
            x1=i*TAILLE_CARREAU+distance
            y1=j*TAILLE_CARREAU+distance
            x2=x1+TAILLE_CARREAU-distance
            y2=y1+TAILLE_CARREAU-distance
            can.create_rectangle(x1,y1,x2,y2,fill=color,tag=f"{j+1} {i+1} cacheur")

def prepare_image():
    liste_image = []
    tout_image = []
    for file in os.listdir("image_memory"):
        tout_image.append(file)
    while(len(liste_image)<100):
        element = choice(tout_image)
        big = 2
        zoom = 1
        if element == "wpcatltoast.png" or element == "SmallLogo.png" or element == "vlc-48.png" or element == "SmallLogo_google.png":
            big = 4
        if element == "num_5.png":
            zoom = 2
        if element == "SquareTile44x44.targetsize-256_altform-unplated_devicefamily-colorfulunplated.png" or element == "StoreAppList.targetsize-256_altform-lightunplated.png":
            big = 7
        if element == "Title.png":
            big = 14
        if element == "GamesXboxHubAppList.targetsize-96_contrast-high.png":
            big = 3
        photo = PhotoImage(file=f"./image_memory/{element}")
        photo = photo.subsample(big)
        photo = photo.zoom(zoom)
        liste_image.append([photo,element])
        liste_image.append([photo,element])
    for i in range(100):
        shuffle(liste_image)
    
    return liste_image

def place_image(index_image = 0):
    global NB_PLATEAU,TAILLE_CARREAU,distance,liste_image
    for i in range(NB_PLATEAU):
        for j in range(NB_PLATEAU):
            x1=i*TAILLE_CARREAU+distance
            y1=j*TAILLE_CARREAU+distance
            x2=x1+TAILLE_CARREAU-distance
            y2=y1+TAILLE_CARREAU-distance
            can.create_image(x1+distance*3-5,y1+distance*3-5,image=liste_image[index_image][0],tag=f"{j+1} {i+1} {liste_image[index_image][1]}")
            index_image+=1
def clear_with_tag(titre_tag):
    for i in can.find_withtag(titre_tag):
        can.delete(i)
def clic_gauche(event):
    global liste_temporaire , liste_cacheur , score_joueur , courrant, coup_leo , liste_back_tagCacheur
    if courrant==1:
        objet_clique = can.find_closest(event.x,event.y)

        if(len(liste_temporaire)==2):
            if len(list(set(liste_temporaire)))==2:
                for i in liste_cacheur:
                    can.itemconfig(i,fill="blue")
            elif len(list(set(liste_temporaire)))==1:
                for i in liste_cacheur:
                    for element in can.find_all():
                        if can.itemcget(element,"tag") == can.itemcget(i,"tag") and can.itemcget(element,"fill") == "grey":
                            liste_back_tagCacheur.append(element)
                    can.delete(i)
                    score_joueur+=1
            if score_joueur == 100:
                    can.create_text(305,305,text="VOUS AVEZ GAGNE",font=("Helvetica",30),fill="green")
                    courrant = 0
            liste_cacheur.clear()
            liste_temporaire.clear()

        if "cacheur" in can.itemcget(objet_clique,"tag") and can.itemcget(objet_clique,"fill")=="blue":
        #j i pour ligne colonne
            ligne , colonne , _ = can.itemcget(objet_clique,"tag").replace("current","").split()
            print(ligne,colonne)
            can.itemconfig(objet_clique,fill="")
            liste_cacheur.append(objet_clique[0])
            for i in can.find_all():
                if f"{ligne} {colonne}" in can.itemcget(i,"tag") and ".png" in can.itemcget(i,"tag"):
                    print("Trouve")
                    print(can.itemcget(i,"tag"))
                    liste_temporaire.append(str(can.itemcget(i,"tag").split()[2]))
                    print(liste_temporaire)
                    can2.itemconfig(sc,text=str(score_joueur))
                    break
    coup_leo+=1
    if coup_leo%2==0:
        can.after(400,clic_gauche,(event))
def code_triche(event):
    global triche,liste_cacheur,liste_back_tagCacheur
    triche+=1
    for element in can.find_all():
        if "cacheur" in can.itemcget(element,"tag") and element not in liste_cacheur:
            if triche%2==1 and can.itemcget(element,"fill")=="blue":
                can.itemconfig(element,fill="")
            elif triche%2==0 and can.itemcget(element,"fill")=="":
                can.itemconfig(element,fill="blue")
        if triche%2==1:
            if element in liste_back_tagCacheur:
                can.itemconfig(element,fill="green")
        if triche%2==0:
            if element in liste_back_tagCacheur:
                can.itemconfig(element,fill="grey")
    print("mmmmmmmmmmm",liste_back_tagCacheur)

liste_temporaire = []#pour les photos caches
liste_cacheur = []#pour les objets cacheurs des photos
liste_back_tagCacheur = []
triche = 0
ecran = 0
coup_leo = 0
courrant = 1
score_joueur = 0#2 a chaque reussite pour que les
test_clic = 0
distance = 10
WIDTH = 600+distance
HEIGHT = 600+distance
NB_PLATEAU = 10
TAILLE_CARREAU = (HEIGHT-distance)//NB_PLATEAU
fen = Tk()
fen.geometry(f"{HEIGHT+100}x{WIDTH}")
fen.resizable(False,False)
fen.title("memory game")
can = Canvas(fen,height=HEIGHT,width=WIDTH,bg="grey")
can.pack(side=LEFT)
#creation du back de chaque photo
create_plateau("grey")

liste_image = prepare_image()
liste_image = prepare_image()
liste_image = prepare_image()
place_image(0)
clear_with_tag("photo_cache")
place_image()
#creation des cacheurs
create_plateau("blue")

can.bind_all("<Button-1>",clic_gauche)
can.bind_all("<Key-h>",code_triche)
can2 = Canvas(fen,height=WIDTH,width=100,bg="black")
can2.pack(side=LEFT,padx=2)
sc = can2.create_text(45,155,fill="green",text="0",font=("arial",25))

fen.mainloop()

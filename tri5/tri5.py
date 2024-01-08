from tkinter import *
#victoire si 4 boules sont alignes peu importe la direction
###########################################################################################
def create_plateau():
	global x_large,taille
	li = co = 20
	taille = x_large//li
	for ligne in range(li):
		for colonne in range(co):
			x1 = ligne*taille
			y1 = colonne*taille
			x2 = x1+taille
			y2 = y1+taille
			couleur = "blue"if(ligne+colonne)%2 else "black"
			tag_de_reconnaissance = f"{colonne+1} {ligne+1}" #pour un resultat ligne->colonne
			can.create_rectangle(x1,y1,x2,y2,fill=couleur,tag=tag_de_reconnaissance)
###########################################################################################
def test_coords(liste_une):
	global victoire
	for i in liste_une:
		print(i,end="\n\n")
	#premier cas , on creer les cas possibles pour le horizontal
	#[ligne colonne couleur]
	for i in liste_une:
		p,d,t=i
		c1=[p,str(int(d)+1),t]
		c2=[p,str(int(d)+2),t]
		c3=[p,str(int(d)+3),t]
		c4=[p,str(int(d)+4),t]
		if c1 in liste_une and c2 in liste_une and c3 in liste_une and c4 in liste_une:
			can.create_text(300,300,text="FIN DE LA PARTIE",fill="grey",font=("",50))
			victoire=1
	#deuxieme cas , on creer les cas possibles pour le vertical
	for i in liste_une:
		p,d,t=i
		c1=[str(int(p)+1),d,t]
		c2=[str(int(p)+2),d,t]
		c3=[str(int(p)+3),d,t]
		c4=[str(int(p)+4),d,t]
		if c1 in liste_une and c2 in liste_une and c3 in liste_une and c4 in liste_une:
			can.create_text(300,300,text="FIN DE LA PARTIE",fill="grey",font=("",50))
			victoire=1
	#troisieme cas , pour l oblique
	for i in liste_une:
		p,d,t=i
		c1=[str(int(p)+1),str(int(d)+1),t]
		c2=[str(int(p)+2),str(int(d)+2),t]
		c3=[str(int(p)+3),str(int(d)+3),t]
		c4=[str(int(p)+4),str(int(d)+4),t]
		if c1 in liste_une and c2 in liste_une and c3 in liste_une and c4 in liste_une:
			can.create_text(300,300,text="FIN DE LA PARTIE",fill="grey",font=("",50))
			victoire=1
	#cas pour l'oblique de sens oppose
	for i in liste_une:
		p,d,t=i
		c1=[str(int(p)-1),str(int(d)+1),t]
		c2=[str(int(p)-2),str(int(d)+2),t]
		c3=[str(int(p)-3),str(int(d)+3),t]
		c4=[str(int(p)-4),str(int(d)+4),t]
		if c1 in liste_une and c2 in liste_une and c3 in liste_une and c4 in liste_une:
			can.create_text(300,300,text="FIN DE LA PARTIE",fill="grey",font=("",50))
			victoire=1
###########################################################################################
def toucher(event):
	global cp,taille,victoire
	taille = 2
	if victoire==0:
		donne = event.widget.find_closest(event.x,event.y)
		c = can.coords(donne)
		couleur_instant= "red" if cp%2==0 else "green"
	#couleur rouge quand cp%2 else couleur vert 
		if can.itemcget(donne,"fill")=="blue" or can.itemcget(donne,"fill")=="black":
			can.create_oval(c[0]+taille,c[1]+taille,c[2]-taille,c[3]-taille,fill=couleur_instant)
			cp+=1
			tag_donne = can.itemcget(donne,"tag").replace("current",couleur_instant)
			if cp%2==0:
				liste_red.append(tag_donne.split())
			else:
				liste_green.append(tag_donne.split())
			print(tag_donne)
			test_coords(liste_red)
			test_coords(liste_green)
###########################################################################################
fen = Tk()
cp = 0
victoire = 0
taille = 0
liste_red=[]
liste_green=[]
x_large = y_large = 600
taille_fenetre = f"{x_large}x{y_large}"
fen.geometry(taille_fenetre)
fen.resizable(False,False)
can = Canvas(fen,height=x_large,width=x_large)
can.pack()
can.bind_all("<Button-1>",toucher)
create_plateau()
fen.mainloop()
###########################################################################################

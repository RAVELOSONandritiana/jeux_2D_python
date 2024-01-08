from tkinter import *
from random import *
#fonction pour l'utilisateur
#but comme button
def pi_but():
	global choix_j1
	choix_j1="pierre"
def pa_but():
	global choix_j1
	choix_j1="papier"
def si_but():
	global choix_j1
	choix_j1="sciscors"
#faut remplacer les vides par les correspondant
def envoyer():
	global choix_ia,choix_j1,score_ia,score_j,max_point,victoire_ia,victoire_joueur,nomFichier,coups
	var1=var2=""
	element=["pierre","papier","sciscors"]
	index_element = 0
	if len(choix_j1)>4:
		for i in range(10):
			index_element = randint(0,101)%3
		shuffle(element)
		choix_ia=element[index_element]
	else:
		var2=var1="VIDE"
	vict=55	#variable pour dire que aucune condition en s'est passe
	if choix_ia=="pierre":
		if choix_j1=="pierre":
			vict=0
			var2="PI"
		elif choix_j1=="papier":
			vict=1
			var2="PA"
		elif choix_j1=="sciscors":
			vict=-1
			var2="SC"
		var1="PI"
		coups+=1
	elif choix_ia=="papier":
		if choix_j1=="pierre":
			vict=-1
			var2="PI"
		elif choix_j1=="papier":
			vict=0
			var2="PA"
		elif choix_j1=="sciscors":
			vict=1
			var2="SC"
		var1="PA"
		coups+=1
	elif choix_ia=="sciscors":
		if choix_j1=="pierre":
			vict=1
			var2="PI"
		elif choix_j1=="papier":
			vict=-1
			var2="PA"
		elif choix_j1=="sciscors":
			vict=0
			var2="SC"
		var1="SC"
		coups+=1
	else:pass
	
	if vict==1:score_j+=1#;score_ia-=1
	elif vict==-1:score_ia+=1#;score_j-=1
	elif vict == 0:
		score_ia-=1
		score_j-=1
	else:pass
	can.itemconfig(vide1,text=str(var1))
	can.itemconfig(vide2,text=str(var2))
	can_ia.itemconfig(s_ia,text=str(score_ia))
	can_ia.itemconfig(s_j1,text=str(score_j))
	choix_ia=choix_j1="VIDE"
	can.itemconfig(nb_coups,text=f"{coups}")
	if score_ia==-(max_point*2) and score_j==-(max_point*2):
		score_ia=score_j=0
		can.itemconfig(vide1,text="NULL")
		can.itemconfig(vide2,text="NULL")
		coups=0
	elif score_ia==max_point or score_j==-(max_point*2):
		can.itemconfig(vide1,text="WIN")
		can.itemconfig(vide2,text="LOSE")
		victoire_ia+=1
		score_ia=score_j=0
		coups=0
	elif score_j==max_point or score_ia==-(max_point*2):
		can.itemconfig(vide2,text="WIN")
		can.itemconfig(vide1,text="LOSE")
		victoire_joueur+=1
		score_ia=score_j=0
		coups=0
	can.itemconfig(txt_max1,text=f"victoire ia : {victoire_ia}")
	can.itemconfig(txt_max2,text=f"victoire joueur : {victoire_joueur}")
	
	
def en():
	envoyer()
	
def en_clavier(event):
	envoyer()
	
def pi_but_clavier(event):
	global choix_j1
	choix_j1="pierre"
def pa_but_clavier(event):
	global choix_j1
	choix_j1="papier"
def si_but_clavier(event):
	global choix_j1
	choix_j1="sciscors"
coups = 0
victoire_ia=victoire_joueur=0
nom = input      ("Your name    : ")
if len(nom)==0:nom="PL"
max_point = int(input("Point de fin : "))
if max_point==0:max_point=10
choix_j1=""
choix_ia=""
score_ia=score_j=0
fen = Tk()
fen.title("Essai")
fen.geometry("500x400")
fen.resizable(False,False)
#################################################################
si = PhotoImage(file = "Photos/edit-cut-symbolic.symbolic.png")
pi = PhotoImage(file = "Photos/emoji-body-symbolic.symbolic.png")
pa = PhotoImage(file = "Photos/mail-send-symbolic.symbolic.png")#preferences-system-privacy-symbolic.symbolic
vide = PhotoImage(file = "Photos/MicrosoftAccount.scale-180.png")
fo = PhotoImage(file = "Photos/StoreLogo.scale-400.png")#face-angel
#################################################################
can = Canvas(fen,height=400,width=400,bg="black")
can.pack(side="left")
fo = fo.subsample(2)
f = can.create_image(150,200,image=fo)

pierre = Button(can,height=100,width=100,image=pi)
pierre.place(x = 0,y = 5)
papier = Button(can,height=100,width=100,image=pa)
papier.place(x = 100,y = 5)
sisceau = Button(can,height=100,width=100,image=si)
sisceau.place(x = 200,y = 5)
#image=vide
"""
vide1 = can.create_text(350,60,text="",fill="green",font=("",40))
vide2 = can.create_text(350,340,text="",fill="green",font=("",40))
"""
vide1 = can.create_text(350,60,text="VIDE",fill="blue",font=("",20))
vide2 = can.create_text(350,340,text="VIDE",fill="blue",font=("",20))
#Boutton qui se trouve en bas
pierre2 = Button(can,height=100,width=100,image=pi,command=pi_but)
pierre2.place(x = 0,y = 290)
papier2 = Button(can,height=100,width=100,image=pa,command=pa_but)
papier2.place(x = 100,y = 290)
sisceau2 = Button(can,height=100,width=100,image=si,command=si_but)
sisceau2.place(x = 200,y = 290)

#vide2 = Button(can,height=100,width=100,image=vide)
#vide2.place(x = 300,y = 290)

#le sisiny droite
can2 = Canvas(fen,height=400,width=150)
can2.pack(side="right")
#Barre de score
can_ia=Canvas(can2,height=400,width=100,bg="purple")
can_ia.place(x=0,y=0)

s_ia = can_ia.create_text(50,60,font=("",50,"bold"),text=str(score_ia),fill="#FFffff")
s_j1 = can_ia.create_text(50,350,font=("",50,"bold"),text=str(score_j),fill="#FFffff")

i = PhotoImage(file = "Photos/fprojectjumpforward.png")
soumettre = Button(can2,width=100,height=180,image=i,command=en)
soumettre.place(x = 0,y = 110)

txt_max = can.create_text(60,130,font=("",10,"italic"),text=f"Point maximale : {max_point}",fill="red")
txt_max = can.create_text(250,130,font=("",10,"italic"),text=f"Point minimale : {-max_point*2}",fill="red")
txt_max1 = can.create_text(50,265,font=("",10,"italic"),text=f"victoire ia : {victoire_ia}",fill="red")
txt_max2 = can.create_text(250,265,font=("",10,"italic"),text=f"victoire joueur : {victoire_joueur}",fill="red")
nb_coups = can.create_text(350,200,font=("",50,"italic"),text=f"{coups}",fill="green",width=10)

textVs = can.create_text(150,200,text="VS",font=("",20),fill="green")
textIA = can.create_text(50,200,text="IA",font=("",40),fill="red")
textJ = can.create_text(250,200,text=nom,font=("",40),fill="red")

can.bind_all("<Up>",en_clavier)
can.bind_all("<Left>",pi_but_clavier)
can.bind_all("<Down>",pa_but_clavier)
can.bind_all("<Right>",si_but_clavier)
nomFichier = f"{nom}.csv"
fen.mainloop()

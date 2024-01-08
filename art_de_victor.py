from tkinter import *
from random import *
class Plateau(object):
	"""class pour creer l art de Vinsley"""
	def __init__(self,height=430,width=400):
		self.fen = Tk()
		self.couleur = ["green","yellow","black","red","pink","purple","#36E23D","#2E64ED"]
		self.fen.geometry(f"{width}x{height}")
		self.fen.resizable(False,False)
		self.can = Canvas(self.fen,height=400,width=400,bg="grey")
		self.can.pack()
		self.dessine_pl()
		self.but = Button(self.fen,text="reinit",command=self.dessine_pl,width=25)
		self.but.place(x=0,y=400)
		self.quit = Button(self.fen,text="quitter",command=self.fen.destroy,width=25)
		self.quit.place(x=200,y=400)
		self.can.bind_all("<Return>",self.dessine_plateau)
		self.fen.mainloop()

	def dessine_plateau(self,event):
		self.can.delete(ALL)
		rayon = 40
		dist = 5
		for i in range(10):
			for j in range(10):
				x1 = i*rayon
				y1 = j*rayon
				x2 = x1+rayon
				y2 = y1+rayon
				self.dessine_rectangle(x1,y1,x2,y2,choice(self.couleur))
				k = randint(1,2)
				if k==1:
					self.dessine_rectangle(x1+dist,y1+dist,x2-dist,y2-dist,choice(self.couleur))
				elif k == 2:
					self.dessine_cercle(x1+dist,y1+dist,x2-dist,y2-dist,choice(self.couleur))

	def dessine_pl(self):
		self.can.delete(ALL)
		rayon = 40
		dist = 5
		for i in range(10):
			for j in range(10):
				x1 = i*rayon
				y1 = j*rayon
				x2 = x1+rayon
				y2 = y1+rayon
				self.dessine_rectangle(x1,y1,x2,y2,choice(self.couleur))
				k = randint(1,2)
				if k==1:
					self.dessine_rectangle(x1+dist,y1+dist,x2-dist,y2-dist,choice(self.couleur))
				elif k == 2:
					self.dessine_cercle(x1+dist,y1+dist,x2-dist,y2-dist,choice(self.couleur))

	def dessine_rectangle(self,x1,y1,x2,y2,couleur):
		self.can.create_rectangle(x1,y1,x2,y2,fill=couleur)

	def dessine_cercle(self,x1,y1,x2,y2,couleur):
		self.can.create_oval(x1,y1,x2,y2,fill=couleur)

pl = Plateau()

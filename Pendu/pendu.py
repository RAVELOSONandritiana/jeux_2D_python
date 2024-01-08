from random import choice
def unique():
	with open ("base.txt") as file:
		return choice(file.readlines())
while True:
	mot = unique()[:-1].upper()
	test = "*"*(len(mot))
	trouve = 0
	t=""
	coup = len(mot)+len(mot)//2
	while len(set(mot)) != len(t) and coup > 0:
		for i in mot:
			print(i if i in t else "*",end='')
		print(f"\nNombre de coups restant -> {coup}")
		c = input("caractere : ").upper()
		for i in range(len(mot)):
			if c == mot[i] and c not in t:
				trouve+=1
				t+=c
				coup+=1
		coup-=1
	if coup > -1 and len(set(mot)) == len(t):
		print(f"{mot}\nVous avez gagne , le mot etait bien {mot}")
	else:
		print(f"Vous avez perdu , le mot est {mot}")
	print("\n\n")

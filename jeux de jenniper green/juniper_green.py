max = int(input("entrer Nmax : "))+1
range_nombre = list(range(0,max))
l_tmp = list(range(0,max))
game = 1
deja_choisi = [0]
coup = 0
while game != 0:
    for i in deja_choisi:
        if i in l_tmp:
            l_tmp.remove(i)
    if len(l_tmp)==0:
        game = 0
        print("Bravo !")
        break
    print(l_tmp)
    
    if coup == 0:
        nombre_choisi = int(input("Choix joueur : "))
        while nombre_choisi not in l_tmp or nombre_choisi%2==1:
            print(f"Veuillez choisir dans l intervalle [{l_tmp[0]};{l_tmp[-1]}] et que ce soit pair pour le premier coup")
            nombre_choisi = int(input("Choix joueur : "))
    else:
        nombre_choisi = int(input("Choix joueur : "))
        while nombre_choisi not in l_tmp:
            print(f"Veuillez choisir dans l intervalle [{l_tmp[0]};{l_tmp[-1]}]")
            nombre_choisi = int(input("Choix joueur : "))
    deja_choisi.append(nombre_choisi)
    l_tmp.clear()
    for i in range_nombre:
        if i%nombre_choisi==0 or nombre_choisi%i==0:
            l_tmp.append(i)
    l_tmp.sort()
    coup = 1

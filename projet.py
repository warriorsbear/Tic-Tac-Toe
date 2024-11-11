# importation

# Variables globales

# choix possible par l'utilisateur pour choisir une grille
nums_choix = ["0","1","2","3","4","5","6","7","8"]
# choix possible par l'utilisateur pour choisir une ligne et une colonne
nums = ["0","1","2"]

# variable qui permet de savoir dans quel case l'utilisateur doit jouer
# dans le cas de None, l'utilisateur decide ou il veut jouer
# (exemple: debut de partie ou case gaggante)
choix_grille=None

#creation d'un tableau de 9 emplacement
grille =['','','',
        '','','',
        '','','']

#remplir le tableau de 9 grille
for k in range(0,9):
    grille[k]= [[" "," "," "],
                [" "," "," "],
                [" "," "," "]]







# Sous-programme
#affichage de la zone de jeu
def affJeu ():
    print( )
    print("   0   1   2   3   4   5   6   7   8")
    aff3case(grille,0)
    print("------------------------------------")
    aff3case(grille,1)
    print("------------------------------------")
    aff3case(grille,2)
    print("------------------------------------")


#affiche 3 case de la grille
def aff3case(gr,ligne):
    case = gr[ligne*3]
    case1 = gr[ligne*3 + 1]
    case2 = gr[ligne*3 + 2]
    print(ligne*3 , " " + case[0][0] + " | " + case[0][1] + " | " + case[0][2]
           + " | " + case1[0][0] + " | " + case1[0][1] + " | " + case1[0][2]
           + " | " + case2[0][0] + " | " + case2[0][1] + " | " + case2[0][2])
    print(ligne*3+1 , " " + case[1][0] + " | " + case[1][1] + " | " + case[1][2]
          + " | " + case1[1][0] + " | " + case1[1][1] + " | " + case1[1][2]
           + " | " + case2[1][0] + " | " + case2[1][1] + " | " + case2[1][2])
    print(ligne*3+2 , " " + case[2][0] + " | " + case[2][1] + " | " + case[2][2]
          + " | " + case1[2][0] + " | " + case1[2][1] + " | " + case1[2][2]
           + " | " + case2[2][0] + " | " + case2[2][1] + " | " + case2[2][2])

# vérifie si le coup est possible
def verif(l,c,choix_grille):
    if grille[int(choix_grille)][l][c] == ' ':
        return True
    else:
        return False



# sous programme qui vérifie si une case est terminé
# 2 - on détecte un gagant
# 3 - on détecte une égalité

def verifcase(joueur,case):
    # verification verticales
    ttt = grille[case]
    if ttt[0][0] == ttt[0][1] == ttt[0][2] == joueur or ttt[1][0] == ttt[1][1] == ttt[1][2] == joueur or ttt[2][0] == ttt[2][1] == ttt[2][2] == joueur:
       return joueur
    # verification horizontales
    if ttt[0][0] == ttt[1][0] == ttt[2][0] == joueur or ttt[0][1] == ttt[1][1] == ttt[2][1] == joueur or ttt[0][2] == ttt[1][2] == ttt[2][2] == joueur:
        return joueur
    # verification en diagonale
    if ttt[0][0] == ttt[1][1] == ttt[2][2] == joueur or ttt[2][0] == ttt[1][1] == ttt[0][2] == joueur:
        return joueur
    else:
        return ' '

# sous programme qui vérifie si le jeu est terminé
# 2 - on détecte un gagant
# 3 - on détecte une égalité

def verifFinDeJeu(joueur):
    if verifcase(joueur,0) == verifcase(joueur,1) == verifcase(joueur,2) == joueur or verifcase(joueur,3) == verifcase(joueur,4) == verifcase(joueur,5) == joueur or verifcase(joueur,6) == verifcase(joueur,7) == verifcase(joueur,8) == joueur :
        return True
    if verifcase(joueur,0) == verifcase(joueur,3) == verifcase(joueur,6) == joueur or verifcase(joueur,2) == verifcase(joueur,5) == verifcase(joueur,8) == joueur or verifcase(joueur,6) == verifcase(joueur,7) == verifcase(joueur,8) == joueur :
        return True
    if verifcase(joueur,0) == verifcase(joueur,4) == verifcase(joueur,8) == joueur or verifcase(joueur,2) == verifcase(joueur,4) == verifcase(joueur,6) == joueur :
        return True
    else:
        return False

    

#renvoi la case ou doit jouer le prochain joueur a partir d'une ligne et d'une colonne
def ligneetcolonneversgrille(lig,col):
    if lig == 0 :
        return col
    if lig == 1 :
        return 3+col
    if lig ==2:
        return 6+col


    







#Sous programme qui permet de jouer au jeu
# fin boucle de jeu
# 1 - plus de places
# 2 - on détecte un gagant
# 3 - on détecte une égalité

def jouer():

    joueur = "X"
    choix_grille=None

    while not verifFinDeJeu("X") and not verifFinDeJeu("O"):
        affJeu()


        #___ le joueur choisit la case de la grille ou il veut jouer s'il a le choix
        if choix_grille == None:
            choix_grille = input("dans quelle grille voulez vous jouez ? (0,8)")
            while choix_grille not in nums_choix :
                choix_grille = input("dans quelle grille voulez vous jouez ? (0,8)")
        print("vous jouez dans la grille ",choix_grille)

        #verifie que l'entree du joueur est valide
        choix = input("Joueur " + joueur + ", où voulez vous jouer? \n")
        while len(choix) != 2 or choix[0] not in nums or choix[1] not in nums:
            choix = input("Joueur " + joueur + ", ou voulez vous jouer?")

        # ajoute le coup dans la grille
        lig = int(choix[0])
        col = int(choix[1])





        if verif(lig,col,int(choix_grille)):
            grille[int(choix_grille)][lig][col] = joueur
                
            # changement de joueur + grille ou jouera le prochain joueur
            choix_grille=ligneetcolonneversgrille(lig,col)
            if verifcase('X',choix_grille) == 'X' or verifcase('O',choix_grille) == 'O' :
                choix_grille=None


            if joueur == "X":
                joueur = "O"
            else:
                joueur = "X"             
        else:
            print("case occupée")


    affJeu()
    if verifFinDeJeu("X"):
        print ("le joueur X a gagné")

    if verifFinDeJeu("O"):
        print ("le joueur O a gagné")
    print("terminé")






#lancer le jeu
jouer()

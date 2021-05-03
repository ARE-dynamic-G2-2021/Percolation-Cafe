from random import sample, randrange
from tkinter import Tk, Canvas, Scale, Button, Label, N

#Dimensions (changer pour le volume)
nb_cellules = 40 #prendre entre 40 et 80
taille_cellule = 20 #prendre entre 10 et 20
canvas_w = taille_cellule * nb_cellules - 2 #taille des canvas(notre environnement)
canvas_h = taille_cellule * nb_cellules - 2

'''
Remarques: 0 correspond aux graines de cafe, 1 correspond aux pores 2 correspond a l'eau et 3 correspond au cafe liquide extrait
Un 2 cherche un 1 dans so voisinnage; si c'est le cas le 1 devient un 2 et le 2 devient un 3; on repete le cycle
'''
#couleurs |graines de cafe|pores   |eau liquide      |cafe liquide
COLORS = ["saddle brown", "tan2", "cornflowerblue", "#49230A"]

def generate_random_world(densite, nb_cellules): #creer une liste 2D de 0 et 1    (2)
    unites = [(ligne, colonne) for colonne in range(nb_cellules) for ligne in range(nb_cellules)]
    nb_pores = int( nb_cellules ** 2 * densite) #calcule le nb de pores qu'il faut
    
    pores = sample(unites, nb_pores) #fonction aleatoire sample pour placer les pores
    world = [[0] * nb_cellules for x in range(nb_cellules)] 
    
    for j1 in range(nb_cellules): #liberer la premiere ligne
        world[0][j1]= 1
    for (i,j) in pores: #placer les pores
        world[i][j] = 1
    return world


def neighborhood(nb_cellules, i, j): #fonction similaire aux voisins de schelling (8)
    return [(a, b) for (a, b) in 
            [(i, j + 1), (i, j - 1), ( i + 1, j)] #3 voisins: sud-ouest-est
            if a in range(nb_cellules) and b in range(nb_cellules)]


def dessiner_une_cellule(world, ligne, colonne): #dessiner une seule cellule   (4)
        A = (taille_cellule * colonne, taille_cellule * ligne) #point A pour une cellule
        B = (taille_cellule * (colonne + 1), taille_cellule * (ligne + 1)) #point B pour une cellule
        
        categorie = world[ligne][colonne] #determiner les couleurs
        color = COLORS[categorie]
        cnv.create_rectangle(A, B, fill=color, outline='') #creer un carreau(cellule)


def dessiner_cellules(world): #desinner l'ensemble des cellules, fait appel chaque fois a la fonction precedante  (3)
    nb_cellules = len(world)
    for ligne in range(nb_cellules):
        for colonne in range(nb_cellules):
            dessiner_une_cellule(world, ligne, colonne)


def update_world(world): #permet de passer a l'etat suivant de notre environnement  (7)
    nb_cellules = len(world)
    pores_voisins = [] #une liste qui sauvegarde la position des pores voisins
    for ligne in range(nb_cellules):
        for colonne in range(nb_cellules):
            if world[ligne][colonne] == 2: #on change tout ce qui est eau en cafe liquide extrait
                world[ligne][colonne] = 3
                for (i, j) in neighborhood(nb_cellules, ligne, colonne): #verifie les voisins
                    if world[i][j] == 1:
                        pores_voisins.append((i, j))
                        
    for (ligne,colonne) in pores_voisins: #a la fin de l'execution on change tout ce qui est pore en eau
        world[ligne][colonne] = 2


def initialisation(): #generer/regenerer notre environnement; boutton Reset relié a initialisation  (1)
    global world, cpt, nb_pores, running, sec, doTick
    densite = float(slider.get()) / 100 #prendre la valeur du slider actuel (en cas de reset aussi)
    running = False #l'animation n'est pas en cours
    doTick = False #ni le chrono
    cpt = 0
    sec = 0.0
    
    lbl_timer.config(text = str(sec) + "s")
    lbl_rendement.config(text = "0%")
    slider["state"] = "normal" #on peut toujours changer le slider

    world = generate_random_world(densite, nb_cellules) #on appelle notre 1ere fonction
    nb_pores = int(nb_cellules * nb_cellules * densite)
    lbl_percolation.config(text="")
    lbl_gout.config(text="")
    dessiner_cellules(world)


def clock(): #notre chronometre Rq: commence a bugger + on augmente le nb de cellules
    global sec, doTick
    if not doTick:
        return  
    sec += 0.1
    sec = round(sec,1)
    lbl_timer.config(text = str(sec) + "s")
    if doTick:
        cnv.after(100, clock)


def change_slider(percent):  #cette fonction est reliee au slider et appelle init
    cnv.delete("all") #effacer tout car on change la densite
    initialisation()


def propagation(): #permet de lancer/faire progresser l'animation  (6)
    global world, cpt, nb_pores, running
    update_world(world) #la mise a jour de l'etat
    
    nb_eau = sum(world[i][j] == 2 for i in range(nb_cellules) for j in range(nb_cellules))
    cpt += nb_eau  #incrementer par le nb d'eau
    rendement = int(cpt / nb_pores * 100) #on trouve le rendement du cafe extrait 
    
    cnv.delete("all") #effacer tout
    dessiner_cellules(world) #redessiner 
    lbl_rendement.config(text = str(rendement) + "%")
    test_percolation(world, nb_cellules)  
    
    if nb_eau == 0: #si arret de propagation, arreter l'animation et sortir de la fonction
        running = False
        return 
    
    cnv.after(100, propagation) #propagation est appelee toute les 100ms (100ms de delai entre les images)


def ajouter_eau(event): #ajouter de l'eau  (5)
    global world, running, cpt, doTick
    i, j = event.y // taille_cellule, event.x // taille_cellule #reperer la position du click
    if world[0][j] == 1: #permet d'ajouter de l'eau QUE SI on a un pore
        world[0][j]= 2
        cpt += 1 #incrementer le cpt car on ajoute de l'eau
        if not running:
            running = True
            slider["state"] = "disabled" #interdit de changer le slider apres avoir clicke
            propagation() #on lance l'animation
            doTick = True #lancer le chrono
            clock()


def test_percolation(world, nb_cellules): #verifier si une percolation a eu lieu ou pas (8)
    global sec, doTick
    for j1 in range(nb_cellules):
        if world[1][j1] == 3: 
            for j2 in range(nb_cellules):
                if world[nb_cellules - 1][j2] == 3:  #si on trouve du cafe en bas, il y a eu percolation
                    lbl_percolation.config(text = "Percolation")
                    doTick = False #arreter le chrono
                    if taille_cellule > 15: #conditions de l'afficheur de gout
                        if sec >= 6.5:
                            lbl_gout.config(text ="saveurs -\narômes -\n+ concentré")
                        else:
                            lbl_gout.config(text ="saveurs -\narômes -\n- concentré")
                    elif taille_cellule <= 15:
                        if sec >= 10.0:
                            lbl_gout.config(text ="saveurs +\narômes +\n+ concentré")
                        else:
                            lbl_gout.config(text ="saveurs +\narômes +\n- concentré")


#Section configuration de Tkinter                  
window = Tk()
window.title("Percolateur de Café - CLICKER POUR COMMENCER")
window.resizable(width = True, height = True)
screen_x = int(window.winfo_screenwidth())
window_x = taille_cellule * nb_cellules + 110  #taille du window tkinter(X)
window_y = taille_cellule * nb_cellules + 4   #taille du windows tkinter (Y)
posX = (screen_x // 2) - (window_x // 2)
geo = "{}x{}+{}+{}".format(window_x, window_y, posX, 0)
window.geometry(geo)

cnv = Canvas(window, width = canvas_w, height = canvas_h, background = "black") #options canvas
cnv.grid(row = 0, column = 0, rowspan = 15)  

btn = Button(window, text = "Reset", font = 10, command = initialisation, width = 9, height = 2) #boutton reset
btn.grid(row = 0, column = 1, sticky = N)

lbl_rendement = Label(window, text = "0%", font = 9,  bg = "cornflowerblue", width = 9, height = 2 ) #afficheur rendement
lbl_rendement.grid(row = 2, column = 1, sticky = N)

lbl_percolation = Label(window, text = "", font = 9, bg = "lawn green", width = 9, height = 2) #afficheur percolation
lbl_percolation.grid(row=4, column = 1, sticky = N)

lbl_gout = Label(window, text = "", font = 9, bg = "orange red", width = 9, height = 3) #afficheur gout du cafe
lbl_gout.grid(row=5, column =1, sticky=N)

lbl_timer = Label(window, font = 10, bg = "medium orchid", width = 9, height = 2) #timer
lbl_timer.grid(row = 3, column = 1, sticky = N)

cnv.bind("<Button-1>", ajouter_eau) #click de la souris qui relie nous relie a la fonction ajouter_eau

slider = Scale(window, orient = "vertical", command = change_slider, from_ = 100, to = 0, length = 230, width = 35 , font = 2) #slider
slider.set(randrange(60, 80)) #pour commencer, choisir une valeur entre 50 et 75
slider.grid(row = 1, column = 1)

initialisation() #creer l'environnement

window.mainloop()
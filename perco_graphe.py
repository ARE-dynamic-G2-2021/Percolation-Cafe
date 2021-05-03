from random import sample, randrange
from matplotlib.pyplot import figure
import numpy as np
import matplotlib.pyplot as plt
#Paramètres
nb_cellules= 40 #150
repetitions= 20 #Attention: l'experience prend deja beaucoup de temps avec 100 repetitions!

def generate_random_world(densite, nb_cellules):
  unites = [(ligne, colonne) for colonne in range(nb_cellules) for ligne in range(nb_cellules)]
  nb_pores = int( nb_cellules ** 2 * densite)
  pores = sample(unites, nb_pores) 
  world = [[0] * nb_cellules for x in range(nb_cellules)]
  for j1 in range(nb_cellules):
    world[0][j1]= 1
  for (i,j) in pores:
    world[i][j] = 1
  return world, pores

def neighborhood(nb_cellules, i, j):
  return [(a, b) for (a, b) in
    [(i, j+1), (i, j-1), (i-1, j), (i+1, j)]
    if a in range(nb_cellules) and b in range(nb_cellules)]

def ajouter_eau(world):
  j = (randrange(nb_cellules))
  world[0][j] = 2
  return j

def update_world(world, pos_eau): #ici on retourne le nb de pores voisins
  nb_cellules = len(world)
  pores_voisins = []
  for (ligne, colonne) in pos_eau:
    for (i, j) in neighborhood(nb_cellules, ligne, colonne):
      if world[i][j] == 1:
        pores_voisins.append((i, j))
  for (ligne, colonne) in pores_voisins:
    world[ligne][colonne] = 2
  return list(set(pores_voisins))

def test(nb_cellules, densite, repetitions): #ici on calcule le rapport cafe extrait/totalité des pores pour le nb de repetitions donné
  rendement = []
  for r in range(repetitions):
    world, pores = generate_random_world(densite, nb_cellules)
    j = ajouter_eau(world)
    nb_pores = len(pores)
    cpt = 1
    pos_eau = [(0, j)]
    while True: #jusqu'a ce qu'on ait plus d'eau qui peut circuler
      pos_eau = update_world(world, pos_eau)
      nb_eau = len(pos_eau)
      cpt += nb_eau
      if nb_eau == 0:
        break
    rendement.append(cpt / nb_pores)
  return sum(rendement) / repetitions #retourne le rendement moyen pour la densite donnee

#Courbe
f=lambda densite:test(nb_cellules,densite,repetitions)
X = [0.4+k/1000 for k in range(0, 400, 5)] #sauter a des intervales de 5 entre 0 et 400, 80 densites differentes
Y = list(map(f, X))
x = np.array(X)
y = np.array(Y)
figure(figsize=(8, 6))
plt.plot(x, y, markersize = 3, color='red')
plt.xlabel('Totalité des Pores')
plt.ylabel('Rendement du Café extrait')
plt.show()
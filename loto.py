import numpy as np
from numpy import random
from matplotlib import pyplot as plt
import csv
import h5py
import pickle
derniere_liste = []
random.seed(int(input("quelle seed utilisée :")))
tab = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0]
tab2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
        30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
i = 0


def fichiercsv(x):
    with open('bianchi_mathieu.csv', 'a', newline='') as fichier:
        writer = csv.writer(fichier, delimiter=' ')
        writer.writerow(x)


def fichierhdf5(x):
    with h5py.File('bianchi_mathieu.hdf5', 'w') as f:
        dset = f.create_dataset("tirage", data=tirages)


def fichierbinaire(x):
    with open("bianchi_mathieu.bin", "ab") as fb:
        pickle.dump(x, fb)


# Tri fusion fonction de division du tableau
def tri_fusion(tableau):
    if len(tableau) <= 1:
        return tableau
    pivot = len(tableau)//2
    tableau1 = tableau[:pivot]
    tableau2 = tableau[pivot:]
    gauche = tri_fusion(tableau1)
    droite = tri_fusion(tableau2)
    fusionne = fusion(gauche, droite)
    return fusionne


# Tri fusion fonction de fusion de 2 listes
def fusion(tableau1, tableau2):
    indice_tableau1 = 0
    indice_tableau2 = 0
    taille_tableau1 = len(tableau1)
    taille_tableau2 = len(tableau2)
    tableau_fusionne = []
    while indice_tableau1 < taille_tableau1 and indice_tableau2 < taille_tableau2:
        if tableau1[indice_tableau1] < tableau2[indice_tableau2]:
            tableau_fusionne.append(tableau1[indice_tableau1])
            indice_tableau1 += 1
        else:
            tableau_fusionne.append(tableau2[indice_tableau2])
            indice_tableau2 += 1
    while indice_tableau1 < taille_tableau1:
        tableau_fusionne.append(tableau1[indice_tableau1])
        indice_tableau1 += 1
    while indice_tableau2 < taille_tableau2:
        tableau_fusionne.append(tableau2[indice_tableau2])
        indice_tableau2 += 1
    return tableau_fusionne


def tri_cocktail(ligne):
    n = len(ligne)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if ligne[i] > ligne[i + 1]:
                ligne[i], ligne[i + 1] = ligne[i + 1], ligne[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if ligne[i] > ligne[i + 1]:
                ligne[i], ligne[i + 1] = ligne[i + 1], ligne[i]
                swapped = True
        start = start + 1
    return ligne


def tri_insertion(okay):
    # Parcour de 1 à la taille du tab
    for i in range(1, len(okay)):
        k = okay[i]
        j = i - 1
        while j >= 0 and k < okay[j]:
            okay[j + 1] = okay[j]
            j -= 1
        okay[j + 1] = k
    return okay


def recherche_dichotomique_iteratif(lst, item):
    for i in range(len(lst)):
        if lst[i] == item:
            return i
    return -1


def recherche_dichotomique_recursive(element, liste_triee):
    if len(liste_triee) == 1:
        return 0
    m = len(liste_triee)//2
    if liste_triee[m] == element:
        return m
    elif liste_triee[m] > element:
        return recherche_dichotomique_recursive(element, liste_triee[:m])
    else:
        return m + recherche_dichotomique_recursive(element, liste_triee[m:])


# Nombre de tirages à effectuer
nombre_tirage = int(input("choisissez le nombre de tirages :"))
for i in range(nombre_tirage):
    # Tirage des nombres
    premier_tirage = np.random.choice(range(1, 45), size=5, replace=False)
    tirages = list(premier_tirage)

    for j in range(45):
        nbr = tirages.count(j)
        tab[j] = (tab[j] + nbr)
        nbr = 0

    print(premier_tirage)
    fichiercsv(tirages)
    fichierhdf5(tirages)
    fichierbinaire(tirages)


plt.hist(tab2, bins=45, weights=tab, edgecolor="red")
plt.title("histogramme des tirages")
plt.show()

tri = int(input("quelle liste trier :"))
monfichier = open("bianchi_mathieu.csv", "r")
for i in range(tri):
    ligne = monfichier.readline()
print(ligne)
res = ligne.split(" ")
for i in range(5):
    derniere_liste.append(int(res[i]))
methode = int(input("quelle methode pour trier entre 1, 2 ou 3:"))
if methode == 1:
    print(tri_cocktail(derniere_liste))
elif methode == 2:
    print(tri_insertion(derniere_liste))
elif methode == 3:
    print(tri_fusion(derniere_liste))
recherche = int(input("quelle methode pout chercher le nombre 1(itératif) ou 2(récursif)  :"))
if recherche == 1:
    search_item = int(input("quelle nombre je cherche dans ma liste ?"))
    result = recherche_dichotomique_iteratif(derniere_liste, search_item)
    if result != -1:
        print(f"L'élément {search_item} a été trouvé.")
    else:
        print(f"L'élément {search_item} n'a pas été trouvé dans la liste.")
elif recherche == 2:
    search_item = int(input("quelle nombre je cherche dans ma liste ?"))
    result = recherche_dichotomique_recursive(search_item, derniere_liste)
    if result != -1:
        print(f"L'élément {search_item} a été trouvé.")
    else:
        print(f"L'élément {search_item} n'a pas été trouvé dans la liste.")

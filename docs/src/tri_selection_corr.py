#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

''' Implémentation du tri par sélection du minimum. 
Les exemples ci-dessous sont automatiquement exécutés par le module doctest lors de
l'exécution de ce programme. S'il ne se passe rien, cela signifie que les tests fonctionnent.

:Exemples:

>>> l = [9, 1, 7, 3, 5, 2, 6]
>>> est_triee(l)
False
>>> tri_selection(l)
>>> est_triee(l)
True
>>> l = [randint(0, 100) for _ in range(20)]
>>> tri_selection(l)
>>> est_triee(l)
True
'''

# ==> QUESTION 1 <==

def minimum(tableau: list[int], debut: int) -> int:
    ''' Renvoie l'indice de la valeur minimale du tableau dans l'intervalle [debut, len(tableau) - 1].
    :param tableau: (list[int]) un tableau d'entiers
    :param debut: (int) l'indice à partir duquel on recherche le minimum
    :return: (int) l'indice du minimum '''

    indice_min = debut  # Initialiser l'indice du minimum à debut
    for i in range(debut + 1, len(tableau)):  # Parcourir tous les éléments du tableau à partir de debut + 1
        if tableau[i] < tableau[indice_min]:  # Si l'élément d'indice i est inférieur à celui d'indice indice_min
            indice_min = i  # Le nouvel indice du minimum est i
    return indice_min  # Renvoyer l'indice du minimum

def echanger(tableau: list[int], i: int, j: int) -> None:
    ''' Echanger deux éléments d'un tableau
    :param tableau: (list[int]) un tableau d'entiers
    :param i: (int) l'indice d'un élément du tableau
    :param j: (int) l'indice d'un élément du tableau '''

    temp = tableau[i]
    tableau[i] = tableau[j]
    tableau[j] = temp

def tri_selection(tableau: list[int]) -> None:
    ''' Effectue le tri par sélection en place des éléments d'un tableau donné.
    :param tableau: (list[int]) un tableau d'entiers à trier '''

    n = len(tableau)  # Récupérer la longueur du tableau
    for debut in range(0, n - 1):  # Parcourir tous les éléments jusqu'à l'avant dernier (*)
        indice_min = minimum(tableau, debut)  # Récupérer l'indice du minimum
        echanger(tableau, debut, indice_min)  # Echanger les éléments d'indices debut et indice_min

# (*) On ne parcourt pas jusqu'au dernier élément car si les éléments du tableau dans l'intervalle
# [0, len(tableau) - 2] sont triés, l'élément d'indice len(tableau) - 1 est à sa bonne position.

# ==> QUESTION 2 <==

def tri_selection_tout_en_un(tableau: list[int]) -> None:
    ''' Effectue le tri par sélection en place des éléments d'un tableau donné.
    
    :param tableau: (list[int]) un tableau d'entiers à trier '''

    n = len(tableau)  # Récupérer la longueur du tableau
    for debut in range(0, n - 1):  # Parcourir tous les éléments jusqu'à l'avant dernier (*)
        indice_min = debut  # Initialiser l'indice du minimum à debut
        for i in range(debut + 1, len(tableau)):  # Parcourir tous les éléments du tableau à partir de debut + 1
            if tableau[i] < tableau[indice_min]:  # Si l'élément d'indice i est inférieur à celui d'indice indice_min
                indice_min = i  # Le nouvel indice du minimum est i
        # On effectue une permutation
        temp = tableau[debut]
        tableau[debut] = tableau[indice_min]
        tableau[indice_min] = temp

# ==> QUESTION 3 <==

def tri_selection_decroissant(tableau: list[int]) -> None:
    ''' Effectue le tri par sélection dans l'ordre décroissant des éléments d'un tableau donné.
    :param tableau: (list[int]) un tableau d'entiers à trier '''

    n = len(tableau)  # Récupérer la longueur du tableau
    for debut in range(0, n - 1):  # Parcourir tous les éléments jusqu'à l'avant dernier (*)
        indice_max = debut  # Initialiser l'indice du maximum à debut
        for i in range(debut + 1, len(tableau)):  # Parcourir tous les éléments du tableau à partir de debut + 1
            if tableau[i] > tableau[indice_max]:  # Si l'élément d'indice i est inférieur à celui d'indice indice_max
                indice_max = i  # Le nouvel indice du minimum est i
        # On effectue une permutation
        temp = tableau[debut]
        tableau[debut] = tableau[indice_max]
        tableau[indice_max] = temp

# Fonctions utiles (pas à modifier)

def est_triee(tableau: list[int]) -> bool:
    ''' Renvoie True si le tableau donnée est triée, False sinon. 
    :param tableau: (list[int]) tableau d'entiers à vérifier 
    :return: (bool) True ou False selon si le tableau est triée ou non. '''

    return all(tableau[i - 1] <= tableau[i] for i in range(1, len(tableau)))

if __name__ == '__main__':
    ''' Instructions exécutées si l'on exécute ce fichier directement '''
    
    import doctest
    doctest.testmod(verbose=False)
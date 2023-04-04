#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Implémentation du tri par sélection du minimum. 

:Exemples:

>>> l = [9, 1, 7, 3, 5, 2, 6]
>>> est_triee(l)
False
>>> tri_selection(l)
>>> est_triee(l)
True
'''

# ==> QUESTION 1 <==

def minimum(liste, debut):
    ''' Renvoie l'indice de la valeur minimale de la liste dans l'intervalle [debut, len(liste) - 1].
    :param liste: (list[int]) Une liste d'entiers
    :param debut: (int) L'indice à partir duquel on recherche le minimum
    :return: (int) L'indice du minimum '''

    indice_min = debut  # Initialiser l'indice du minimum à debut
    for i in range(debut + 1, len(liste)):  # Parcourir tous les éléments de la liste à partir de debut + 1
        if liste[i] < liste[indice_min]:  # Si l'élément d'indice i est inférieur à celui d'indice indice_min
            indice_min = i  # Le nouvel indice du minimum est i
    return indice_min  # Renvoyer l'indice du minimum

def echanger(liste: list[int], i: int, j: int) -> None:
    ''' Echanger deux éléments d'une liste
    :param liste: (list[int]) Une liste d'entiers
    :param i: (int) L'indice d'un élément de la liste
    :param j: (int) L'indice d'un élément de la liste '''

    temp = liste[i]
    liste[i] = liste[j]
    liste[j] = temp

def tri_selection(liste: list[int]) -> None:
    ''' Effectue le tri par sélection en place des éléments d'une liste donnée.
    :param liste: (list[int]) Une liste d'entiers à trier '''

    n = len(liste)  # Récupérer la longueur de la liste
    for debut in range(0, n - 1):  # Parcourir tous les éléments jusqu'à l'avant dernier (*)
        indice_min = minimum(liste, debut)  # Récupérer l'indice du minimum
        if indice_min != debut:  # Si l'élément de valeur minimale n'est pas déjà à sa place
            echanger(liste, debut, indice_min)  # Echanger les éléments d'indices debut et indice_min

# (*) On ne parcourt pas jusqu'au dernier élément car si les éléments de la liste dans l'intervalle
# [0, len(liste) - 2] sont triés, l'élément d'indice len(liste) - 1 est à sa bonne position.

# ==> QUESTION 2 <==

def tri_selection_tout_en_un(liste: list[int]) -> None:
    ''' Effectue le tri par sélection en place des éléments d'une liste donnée.
    
    :param liste: (list[int]) Une liste d'entiers à trier '''

    n = len(liste)  # Récupérer la longueur de la liste
    for debut in range(0, n - 1):  # Parcourir tous les éléments jusqu'à l'avant dernier (*)
        indice_min = debut  # Initialiser l'indice du minimum à debut
        for i in range(debut + 1, len(liste)):  # Parcourir tous les éléments de la liste à partir de debut + 1
            if liste[i] < liste[indice_min]:  # Si l'élément d'indice i est inférieur à celui d'indice indice_min
                indice_min = i  # Le nouvel indice du minimum est i
        if indice_min != debut:  # Si l'élément de valeur minimale n'est pas déjà à sa place
                temp = liste[debut]
                liste[debut] = liste[indice_min]
                liste[indice_min] = temp

# ==> QUESTION 3 <==

def tri_selection_decroissant(liste: list[int]) -> None:
    ''' Effectue le tri par sélection dans l'ordre décroissant des éléments d'une liste donnée.
    :param liste: (list[int]) Une liste d'entiers à trier '''

    n = len(liste)  # Récupérer la longueur de la liste
    for debut in range(0, n - 1):  # Parcourir tous les éléments jusqu'à l'avant dernier (*)
        indice_max = debut  # Initialiser l'indice du maximum à debut
        for i in range(debut + 1, len(liste)):  # Parcourir tous les éléments de la liste à partir de debut + 1
            if liste[i] > liste[indice_max]:  # Si l'élément d'indice i est inférieur à celui d'indice indice_max
                indice_max = i  # Le nouvel indice du minimum est i
        if indice_max != debut:  # Si l'élément de valeur minimale n'est pas déjà à sa place
                temp = liste[debut]
                liste[debut] = liste[indice_max]
                liste[indice_max] = temp

# Fonctions utiles (pas à modifier)

def est_triee(liste: list[int]) -> bool:
    ''' Renvoie True si la liste donnée est triée, False sinon. 
    :param liste: (list[int]) Liste d'entiers à vérifier 
    :return: (bool) True ou False selon si la liste est triée ou non. '''

    return all(liste[i - 1] <= liste[i] for i in range(1, len(liste)))

if __name__ == '__main__':
    ''' Instructions exécutées si l'on exécute ce fichier directement '''
    
    import doctest
    doctest.testmod(verbose=False)
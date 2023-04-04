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

    pass

def echanger(liste: list[int], i: int, j: int) -> None:
    ''' Echanger deux éléments d'une liste
    :param liste: (list[int]) Une liste d'entiers
    :param i: (int) L'indice d'un élément de la liste
    :param j: (int) L'indice d'un élément de la liste '''

    pass

def tri_selection(liste: list[int]) -> None:
    ''' Effectue le tri par sélection en place des éléments d'une liste donnée.
    :param liste: (list[int]) Une liste d'entiers à trier '''

    pass

# ==> QUESTION 2 <==

def tri_selection_tout_en_un(liste: list[int]) -> None:
    ''' Effectue le tri par sélection en place des éléments d'une liste donnée.
    
    :param liste: (list[int]) Une liste d'entiers à trier '''

    pass

# ==> QUESTION 3 <==

def tri_selection_decroissant(liste: list[int]) -> None:
    ''' Effectue le tri par sélection dans l'ordre décroissant des éléments d'une liste donnée.
    :param liste: (list[int]) Une liste d'entiers à trier '''

    pass

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
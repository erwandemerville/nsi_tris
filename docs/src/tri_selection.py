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

def minimum(tableau, debut):
    ''' Renvoie l'indice de la valeur minimale du tableau dans l'intervalle [debut, len(tableau) - 1].
    :param tableau: (list[int]) un tableau d'entiers
    :param debut: (int) l'indice à partir duquel on recherche le minimum
    :return: (int) l'indice du minimum '''

    pass

def echanger(tableau: list[int], i: int, j: int) -> None:
    ''' Echanger deux éléments d'un tableau
    :param tableau: (list[int]) un tableau d'entiers
    :param i: (int) l'indice d'un élément du tableau
    :param j: (int) l'indice d'un élément du tableau '''

    pass

def tri_selection(tableau: list[int]) -> None:
    ''' Effectue le tri par sélection en place des éléments d'un tableau donné.
    :param tableau: (list[int]) un tableau d'entiers à trier '''

    pass

# ==> QUESTION 2 <==

def tri_selection_tout_en_un(tableau: list[int]) -> None:
    ''' Effectue le tri par sélection en place des éléments d'un tableau donné.
    
    :param tableau: (list[int]) un tableau d'entiers à trier '''

    pass

# ==> QUESTION 3 <==

def tri_selection_decroissant(tableau: list[int]) -> None:
    ''' Effectue le tri par sélection dans l'ordre décroissant des éléments d'un tableau donné.
    :param tableau: (list[int]) un tableau d'entiers à trier '''

    pass

# Fonctions utiles (pas à modifier)

def est_triee(tableau: list[int]) -> bool:
    ''' Renvoie True si le tableau donné est triée, False sinon. 
    :param tableau: (list[int]) tableau d'entiers à vérifier 
    :return: (bool) True ou False selon si le tableau est triée ou non. '''

    return all(tableau[i - 1] <= tableau[i] for i in range(1, len(tableau)))

if __name__ == '__main__':
    ''' Instructions exécutées si l'on exécute ce fichier directement '''
    
    import doctest
    doctest.testmod(verbose=False)
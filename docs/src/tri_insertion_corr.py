#!/usr/bin/env python
# -*- coding: utf-8 -*-

def tri_selection(tableau: 'list[int]') -> None:
    ''' Effectue le tri par insertion en place des éléments d'un tableau donné.
    :param tableau: (list[int]) un tableau d'entiers à trier 
    
    :Exemples:
    
    '''

    for i in range(1, len(tableau)):
        valeur_courante = tableau[i]
        j = i - 1
        while j >= 0 and tableau[j] > valeur_courante:
            tableau[j + 1] = tableau[j]
            j = j - 1
        tableau[j + 1] = valeur_courante

def est_trie(tableau: 'list[int]', fin: int = None) -> bool:
    ''' Renvoie True si les éléments du tableau dans [0, fin] sont triés, False sinon.
    Si pas d'indice de fin donné, vérifier tout le tableau.
    :param tableau: (list[int]) tableau d'entiers à vérifier
    :param debut: (int) indice jusqu'auquel vérifier les éléments
    :return: (bool) True ou False selon si les éléments sont triés ou non. '''

    if fin == None: 
        fin = len(tableau) - 1
    for i in range(1, fin + 1):
        if tableau[i - 1] > tableau[i]:
            return False
    return True

if __name__ == '__main__':
    ''' Instructions exécutées si l'on exécute ce fichier directement '''
    
    import doctest
    doctest.testmod(verbose=False)
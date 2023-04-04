#!/usr/bin/env python
# -*- coding: utf-8 -*-

CNT = 0

def tri_selection(liste: list[int]) -> None:
    ''' Effectue le tri par sélection en place des éléments d'une liste donnée.
    
    :param liste: (list[int]) Une liste d'entiers à trier '''

    global CNT

    n = len(liste)  # Récupérer la longueur de la liste
    for debut in range(0, n - 1):  # Parcourir tous les éléments jusqu'à l'avant dernier (*)
        indice_min = debut  # Initialiser l'indice du minimum à debut
        for i in range(debut + 1, len(liste)):  # Parcourir tous les éléments de la liste à partir de debut + 1
            CNT += 1  # AJOUTER UNE COMPARAISON
            if liste[i] < liste[indice_min]:  # Si l'élément d'indice i est inférieur à celui d'indice indice_min
                indice_min = i  # Le nouvel indice du minimum est i
        if indice_min != debut:  # Si l'élément de valeur minimale n'est pas déjà à sa place
                temp = liste[debut]
                liste[debut] = liste[indice_min]
                liste[indice_min] = temp

if __name__ == '__main__':
    ''' Instructions exécutées si l'on exécute ce fichier directement '''
    
    liste = [2, 5, 7, 9, 12, 59, 94]

    tri_selection(liste)
    print(f'Nombre de comparaisons : {CNT}')

# Le tri par sélection

Le **tri par sélection** (du **minimum** ou du **maximum**) est un algorithme de tri par **comparaisons**.  
Il s'agit d'un algorithme simple mais qui est, comme on le verra, **inefficace**.

## Présentation du tri

### Avec un jeu de cartes

Pour comprendre le fonctionnement de ce tri, voici une petite activité à réaliser avec un **jeu de cartes** traditionnel.

On souhaite trier **une suite de 7 cartes** arbitrairement choisies.  
Par exemple :

![Une suite de 6 cartes](images/suite_cartes.png)

On ne se souciera ici que des **valeurs** des cartes et non de leurs **couleurs**.  
Voici l'**ordre** des valeurs des cartes, de la **moins forte** à la **plus forte**, que l'on utilisera :

![Ordre des cartes](images/ordre_cartes.png)

*Note* : Si la carte *Joker* existe dans votre jeu, on considèrera qu'elle est plus forte que toutes les autres cartes.

!!! abstract "Principe du tri par sélection"
    Le principe du **tri par sélection** du **minimum** est le suivant :

    1. Chercher l'**indice** de la **plus faible carte** de la suite (à partir de l'indice **0**) et **échanger** cette carte avec celle qui est placée en **premier**. La première carte est maintenant **la plus faible**.
    2. Chercher l'**indice** de la **plus faible carte** de la suite en partant du **2ème élément** (indice **1**) et **échanger** cette carte avec celle qui est placée en **deuxième**. Les **deux premières cartes** sont les plus faibles et sont maintenant **triées**.
    3. Poursuivre ainsi jusqu’à l’**avant dernière carte** de la liste.

<figure markdown>
  ![Exemple de déroulement du tri sélection](images/tri_selection.png)
  <figcaption>Exemple de déroulement du tri par sélection</figcaption>
</figure>

### Simulation avec des barres

Voici une simulation du **tri par sélection** en utilisant des barres de différentes tailles comme éléments.  
Le but est de trier les barres de la **plus petite** à **la plus grande**.

!!! success "Simulation du tri par sélection du minimum"
    <div id="controls">
        <button id="run-button" class="md-button">Exécuter</button>
        <button id="reinit-button" class="md-button">Réinitialiser</button>
        <button id="speed-up-button" class="md-button">Accélérer</button>
        <button id="speed-down-button" class="md-button">Ralentir</button>
    </div>
    <div id="bars-container"></div>

## L'algorithme

L'algorithme du **tri par sélection** peut être écrit de plusieurs manières différentes :

- en **itératif** ou en **récursif**,
- **en place** ou non.

!!! info "Tri en place"
    Un tri est dit *en place* s'il modifie directement la structure qu’il est en train de trier, plutôt que de créer et de renvoyer une nouvelle structure.

L'algorithme présenté ici sera écrit de manière **itérative** et **en place**.  
Le tri s'effectuera par sélection **du minimum**.

Pour simplifier les choses, on commence par séparer l'algorithme de tri en **3 sous-algorithmes** :

- l'algorithme principal `tri_selection(tableau)` permettant de trier un **tableau d'éléments** avec le **tri par sélection**,
- l'algorithme `minimum(tableau, debut)` permettant la recherche de l'indice de l'**élément minimal** du tableau à partir de l'indice `debut` donné,
- l'algorithme `echanger(tableau, i, j)` permettant d'échanger **deux éléments** d'indices `i` et `j` donnés.


!!! abstract "Algorithme du tri par sélection"
    **ALGORITHME** : tri_selection  
    **ENTRÉES** :  
    &nbsp;&nbsp;&nbsp;&nbsp;`tableau` : un **tableau** d'éléments pouvant être **comparés**  
    **SORTIE** : aucune (tri *en place*)

    **DÉBUT**  
    &emsp;&emsp;n ← longueur(tableau)  
    &emsp;&emsp;**POUR** debut **ALLANT DE** 0 **À** n - 2  
    &emsp;&emsp;&emsp;&emsp;indice_min ← minimum(tableau, debut)  
    &emsp;&emsp;&emsp;&emsp;**SI** indice_min **≠** debut, **ALORS**  
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;echanger(tableau, debut, indice_min)  
    &emsp;&emsp;**FIN POUR**   
    &emsp;&emsp;Renvoyer **∅**  
    **FIN ALGORITHME**

!!! abstract "Algorithme de recherche du minimum"
    **ALGORITHME** : minimum  
    **ENTRÉES** :  
    &nbsp;&nbsp;&nbsp;&nbsp;`tableau` : un **tableau** d'éléments  
    &nbsp;&nbsp;&nbsp;&nbsp;`debut` : l'**indice** à partir duquel effectuer la recherche  
    **SORTIE** : l'**indice** de l'élément minimal dans l'intervalle `[debut, longueur(tableau) - 1]` du tableau

    **DÉBUT**  
    &emsp;&emsp;indice_min ← debut  
    &emsp;&emsp;**POUR** i **ALLANT DE** debut + 1 **À** longueur(tableau) - 1  
    &emsp;&emsp;&emsp;**SI** tableau[i] < tableau[indice_min], **ALORS**  
    &emsp;&emsp;&emsp;&emsp;indice_min ← i  
    &emsp;&emsp;**FIN POUR**  
    &emsp;&emsp;Renvoyer indice_min  
    **FIN ALGORITHME**

!!! abstract "Algorithme d'échange d'éléments"
    **ALGORITHME** : echanger  
    **ENTRÉES** :  
    &nbsp;&nbsp;&nbsp;&nbsp;`tableau` : un **tableau** d'éléments  
    &nbsp;&nbsp;&nbsp;&nbsp;`i` : l'**indice** d'un élément du tableau  
    &nbsp;&nbsp;&nbsp;&nbsp;`j` : l'**indice** d'un autre élément du tableau  
    **SORTIE** : aucune (tri en place)

    **DÉBUT**  
    &emsp;&emsp;temp ← tableau[i]  
    &emsp;&emsp;tableau[i] ← tableau[j]  
    &emsp;&emsp;tableau[j] ← temp  
    &emsp;&emsp;Renvoyer **∅**  
    **FIN ALGORITHME**

Voici enfin une version en **un seul** algorithme :

!!! abstract "Algorithme du tri par sélection"
    **ALGORITHME** : tri_selection  
    **ENTRÉES** :  
    &nbsp;&nbsp;&nbsp;&nbsp;`tableau` : un **tableau** d'éléments pouvant être **comparés**.  
    **SORTIE** : aucune (tri *en place*)

    **DÉBUT**  
    &emsp;&emsp;n ← longueur(tableau)  
    &emsp;&emsp;**POUR** debut **ALLANT DE** 0 **À** n - 2  
    &emsp;&emsp;&emsp;&emsp;indice_min ← debut  
    &emsp;&emsp;&emsp;&emsp;**POUR** i **ALLANT DE** debut + 1 **À** n - 1  
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;**SI** tableau[i] < tableau[indice_min], **ALORS**  
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;indice_min ← i  
    &emsp;&emsp;&emsp;&emsp;**FIN POUR**  
    &emsp;&emsp;&emsp;&emsp;**SI** indice_min ≠ debut, **ALORS**  
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;temp ← tableau[debut]  
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;tableau[debut] ← tableau[indice_min]  
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;tableau[indice_min] ← temp  
    &emsp;&emsp;**FIN POUR**   
    &emsp;&emsp;Renvoyer **∅**  
    **FIN ALGORITHME**

!!! note "Notes"
    - La première boucle **POUR** s'arrête à `n - 2` car si tous les éléments de l'intervalle `[0, longueur(tableau) - 2]` sont **triés**, l'élément d'**indice** `longueur(tableau) - 1` est obligatoirement déjà à la **bonne position**.
    - La condition `SI indice_min ≠ i, ALORS` permet d'éviter d'effectuer une permutation si l'élément d'indice `i` correspond à l'élément **minimal**.

!!! note "Stabilité du tri"
    Un **tri** est dit **stable** s'il préserve l’**ordonnancement initial des éléments** que l'ordre considère comme égaux.  
    Le tri par sélection est, dans le cas de notre algorithme, **instable** car en cas de valeurs identiques dans le tableau initial, leur ordre relatif peut être modifié.

!!! note "Sélection du maximum"
    Si l'on souhait écrire cet algorithme en sélectionnant le **maximum** plutôt que le minimum, le principe serait le même, mais le parcours s'effectuerait du **dernier élément** au **premier élément** du tableau. Le tableau serait dans ce cas d'abord composé de la **partie non triée**, puis de la **partie triée**.

!!! note "À vous de jouer"
    **Question 1** : Déroulez le **tri par sélection** du minimum sur le tableau `[7, 1, 5, 3, 8, 5]` en vous aidant du tableau suivant :

    ![Tableau exo tri sélection](images/tableau_exo_triselect.png)
    
    **Question 2** : Faites de même sur le tableau `[5, 3, 1, 4, 6, 2]`.

## Implémentation du tri par sélection

On va maintenant implémenter l'algorithme du **tri par sélection** en **Python**.  
Les **tableaux** seront représentés par des **listes Python**. (On parlera donc ici de listes plutôt que de tableaux.)

*Note* : Pour simplifier, on parlera de *listes triées* pour parler de *listes triées dans l'ordre croissant*.

!!! success "À télécharger"
    Récupérer le fichier [tri_selection.py](src/tri_selection.py) à compléter.

!!! note "Question 1"
    1. Compléter les fonctions : 
        - `minimum(liste, debut)` : renvoie l'**indice** de l'élément de **valeur minimale** dans l'intervalle `[debut, len(liste) - 1]`.
        - `echanger(liste, i, j)` : échange les éléments d'indices `i` et `j` de la liste `liste`.
    2. Compléter la fonction `tri_selection(liste)` qui effectue le **tri par sélection** d'une liste `liste` donnée, en réutilisant les deux fonctions précédentes.

    Le programme est muni de **tests** (lignes `8` à `13`).  
    Vous pouvez donc **tester vos fonctions** en exécutant simplement le programme. Si rien ne se passe, c'est que tout est bon. Sinon, l'interpréteur indiquera les tests qui ont échoué.

!!! note "Question 2"
    Compléter la fonction `tri_selection_tout_en_un(liste)` en ré-écrivant le **tri par sélection** sans appeler d'autres fonctions (les **recherches du minimum** et les **échanges** sont effectués **directement dans cette fonction**).

!!! note "Question 3"
    Écrire la fonction `tri_selection_decroissant(liste)` qui effectue le **tri par sélection** des éléments d'une liste dans l'**ordre décroissant**.

## Complexité du tri par sélection

??? tip "Calcul de la complexité du tri par sélection"
    $$
    C(n) = 1 + 2 + [...] + (n - 2) + (n - 1) = \frac{(n - 1)n}{2}
    $$

    $$
    C(n) = \sum_{x=1}^{n-1}x = \frac{(n - 1)n}{2}
    $$

!!! success "À télécharger"
    Récupérer le fichier [analyse_tri_selection.py](src/analyse_tri_selection.py) à compléter.

## Terminaison du tri par sélection

...

## Preuve de correction du tri par sélection

...
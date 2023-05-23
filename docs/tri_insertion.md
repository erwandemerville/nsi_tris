# Le tri par insertion

Nous avons vu la méthode de **tri par sélection**, qui a l'avantage d'être facile à appréhender, mais qui s'avère être fortement coûteuse (coût **quadratique** dans **tous les cas**).  
Voyons s'il n'existe pas d'autres algorithmes de tri plus intéressants.

## Présentation du tri par insertion

### Avec un jeu de cartes

Le **tri par insertion** est un autre algorithme de tri par **comparaisons**, dont le principe est un peu différent, mais plus "naturel".

Dans cette partie, on verra comment trier une **suite de cartes** en utilisant la méthode de **tri par insertion**. On utilisera l'**ordre** suivant (de la carte la plus *faible* à la plus *forte*) :

![Ordre des cartes](images/ordre_cartes.png)

*Note* : Si vous avez une carte *Joker* dans votre jeu, on considèrera qu'elle est plus forte que toutes les autres cartes.

!!! success "Activité préliminaire"
    Munissez-vous d'un paquet de carte, **mélangez-le**, et placez-le en **face cachée**.  
    Vous disposez d'une **zone de jeu** dans laquelle vous ajouterez les cartes **une par une**, de manière à **toujours** avoir une **suite de cartes triée**.  
    L'objectif est de **trier les 7 premières cartes** du paquet.

    - Prenez la **première carte** du paquet et posez-la (face visible) dans votre zone de jeu.  
    La suite de cartes de votre zone de jeu (composée pour le moment d'une seule carte) est-elle triée ?
    - Prenez la **deuxième carte** du paquet, et intégrez-la à votre **suite de cartes** de manière à ce que celle-ci **reste triée**.
    - Prenez la **troisième carte** du paquet et faites de même. Répétez cela jusqu'à avoir une **suite** de **7 cartes triées** dans votre zone de jeu.

    **Question** : **Décrivez la méthode** que vous avez suivi pour intégrer chaque nouvelle carte à votre suite de cartes triée.

---

Voici le **déroulement** de la **méthode de tri par insertion** sur une **suite de cartes**.  
On souhaite trier la suite de cartes suivantes :

<figure markdown>
<center>
![Suite de 5 cartes](images/cartes_insertion/01.png){ width="80%" }
<figcaption>Une suite de 5 cartes.</figcaption>
</center>
</figure>

!!! info "Composition du tableau"
    On distingue **deux parties** dans le tableau :

    - une **partie triée** (en <span style="color:green">vert</span>), initialement composée **de la première carte**.
    - une **partie non-triée** (en <span style="color:gray">gris</span>), initialement composée du **reste des cartes**.

    On dispose également d'une **zone mémoire** dans laquelle peut **placer une carte temporairement**.

<center>
![Suite de 5 cartes](images/cartes_insertion/02.png){ width="60%" }
</center>

On commence donc par traiter la **deuxième carte du tableau**, qui est la **première carte** de la **partie non-triée**. On place cette carte dans la zone **mémoire**.

<center>
![Suite de 5 cartes](images/cartes_insertion/02b.png){ width="60%" }
</center>

Ensuite, on procède comme suit :

!!! tip "Placer la carte à sa bonne position"
    - En partant de la carte positionnée **juste à gauche** de celle que l'on cherche à trier (c'est-à-dire la dernière carte de la **partie triée** du tableau), et en allant jusqu'à la **première carte** du tableau :
        - On **décale d'une position à droite chaque carte** dont la **valeur** est **strictement supérieure** à la carte que l'on cherche à replacer.
        - On s'arrête **uniquement** si la **carte** n'a **pas** une valeur **supérieure**, ou si l'on a parcouru **toutes les cartes**.
    - On **replace** la **carte** (actuellement en *mémoire*) à **sa bonne position**.

Ici, la carte qui précède celle à replacer (qui se trouve en mémoire) est **inférieure** à la carte à replacer. Cela signifie que notre carte est **déjà à sa bonne position**.

Il n'y a donc **pas de décalage à faire**, et on **replace** la **carte** à sa **position initiale**.

<center>
![Suite de 5 cartes](images/cartes_insertion/02c.png){ width="60%" }
</center>

La **partie triée** de notre tableau est maintenant composée des **deux premières cartes**.

<center>
![Suite de 5 cartes](images/cartes_insertion/03.png){ width="60%" }
</center>

On fait de même avec la **troisième carte** du tableau (première carte de la **partie non-triée**).

<center>
![Suite de 5 cartes](images/cartes_insertion/03b.png){ width="60%" }
</center>

Ici encore, la carte était déjà à sa bonne position.

<center>
![Suite de 5 cartes](images/cartes_insertion/03c.png){ width="60%" }
</center>

On a maintenant **3 cartes** dans la **partie triée** du tableau.  
On met la **quatrième carte** (de *valeur 3*) en **mémoire**.

<center>
![Suite de 5 cartes](images/cartes_insertion/05.png){ width="60%" }
</center>

On constate que les **deux cartes précédentes** (de *valeurs 8* et *4*) ont une valeur **supérieure** à celle de la carte que l'on souhaite trier. Il faut donc **déplacer à droite** ces deux cartes.

<center>
![Suite de 5 cartes](images/cartes_insertion/06.png){ width="60%" }
</center>

<center>
![Suite de 5 cartes](images/cartes_insertion/07.png){ width="60%" }
</center>

On peut maintenant **repositionner** notre carte.

<center>
![Suite de 5 cartes](images/cartes_insertion/08.png){ width="60%" }
</center>

<center>
![Suite de 5 cartes](images/cartes_insertion/09.png){ width="60%" }
</center>

Il ne reste ainsi **plus qu'une seule carte** dans la **partie non-triée** de notre tableau.

On répète le même principe, on place cette **carte** en **mémoire**.

<center>
![Suite de 5 cartes](images/cartes_insertion/10.png){ width="60%" }
</center>

Ici, il n'y a que la **carte précédente** à déplacer.

<center>
![Suite de 5 cartes](images/cartes_insertion/11.png){ width="60%" }
</center>

Puis on repositionne notre carte.

<center>
![Suite de 5 cartes](images/cartes_insertion/12.png){ width="60%" }
</center>

Et voilà, on vient de **trier** une **suite de 5 cartes** par la **méthode de tri par insertion** !

!!! note "À vous de jouer"
    Disposez une **suite de 7 cartes** choisies **au hasard** dans un paquet de cartes.  
    Votre **zone de jeu** est composée de votre **suite de cartes** et d'un **emplacement mémoire**.  
    Effectuez le tri de votre suite de cartes en utilisant la méthode de **tri par insertion** présentée ci-dessus.

### Trier un tableau

On a donc vu que la méthode de **tri par insertion** avait l'avantage d'être assez **naturelle**, raison pour laquelle elle est souvent utilisée pour trier des **cartes à jouer**.

Appliquons à présent ce **tri** sur des **tableaux d'entiers**.

On rappelle le **principe** du **tri par insertion** :

- on fait comme si les **éléments** de la **partie non-triée** du tableau étaient donnés **un par un**, le **premier élément du tableau** constituant, **à lui seul**, un **tableau triée** de *longueur 1*,
- on y **range** ensuite le **deuxième élément du tableau** pour constituer un **tableau trié** de *longueur 2*,
- puis on y range le **troisième élément** pour obtenir un **tableau trié** *longueur 3*,
- et ainsi de suite jusqu’à avoir traité le dernier élément...

On insère donc à la **n<sup>ième</sup> itération** le **n<sup>ième</sup> élément** à sa **bonne position** en décalant à droite tous les éléments de la **partie triée** du tableau qui lui sont supérieurs.

!!! note "Exercice - Trier un tableau"

    On souhaite trier le tableau suivant avec le **tri par insertion** : `[5, 3, 1, 4, 6, 2]`.  
    Indiquez quel est l'**état du tableau** après chaque **insertion d'élément**.

    <figure markdown>
    <center>
    ![Tableau exercice tri insertion](images/exo_tri_insertion.png)
    <figcaption>Source : [http://fractale.gecif.net/nsi/pdf/cours/algorithmes/algo_tri.pdf](http://fractale.gecif.net/nsi/pdf/cours/algorithmes/algo_tri.pdf){ target="_blank" }</figcaption>
    </center>
    </figure>

    Faites de même avec le tableau `[2,8,1,5,2,3]`.
    

## L'algorithme

### Présentation de l'algorithme

!!! info "Note"
    Dans la partie précédente, on a souvent parlé de "déplacements" de cartes. En machine, ces déplacements seront implémentés sous la forme de **copies d'éléments**, en réalisant des affectations.

!!! abstract "Algorithme du tri par insertion"
    <div style="font-size:1.1em">
    **ALGORITHME** : tri_insertion  
    **ENTRÉE** :  
    &emsp;&emsp;`tableau` : un **tableau** d'éléments  
    **SORTIE** : aucune (tri en place)

    **DÉBUT**  
    &emsp;&emsp;**POUR** i **ALLANT DE** 1 **À** longueur(tableau) - 1  
    &emsp;&emsp;&emsp;&emsp;valeur_courante ← tableau[i]  
    &emsp;&emsp;&emsp;&emsp;j ← i $-$ 1  
    &emsp;&emsp;&emsp;&emsp;**TANT QUE** j ≥ 0 **ET QUE** tableau[j] > valeur_courante  
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;tableau[j + 1] ← tableau[j]  
    &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;j ← j $-$ 1  
    &emsp;&emsp;&emsp;&emsp;**FIN TANT QUE**  
    &emsp;&emsp;&emsp;&emsp;tableau[j + 1] ← valeur_courante  
    &emsp;&emsp;**FIN POUR**  
    &emsp;&emsp;Renvoyer **∅**  
    **FIN ALGORITHME**
    </div>

!!! note "Exercice 1"
    **Déroulez** l'algorithme sur le tableau `[5, 3, 1, 4, 6, 2]`.

!!! note "Exercice 2"
    1. Pourquoi commence t-on la boucle **POUR** à partir de **1** ?
    2. **Expliquez** à quoi sert la 3<sup>ème</sup> **ligne** de l'**algorithme** : `j ← i - 1`.
    3. Dans le **TANT QUE**, à quoi sert la première condition `j ≥ 0` ? La deuxième condition `tableau[j] > valeur_courante` ? Pourrait t-on inverser les deux conditions ?
    4. À quoi sert la ligne `tableau[j + 1] ← tableau[j] ` dans le **TANT QUE** ?
    5. Pourquoi **décrémente t-on** (c'est-à-dire que l'on diminue de 1) la valeur de `j` à chaque tour de la boucle **TANT QUE** ?
    6. Expliquez l'**affectation** `tableau[j + 1] ← valeur_courante ` après la boucle **TANT QUE**.

!!! info "Tri stable"
    Le **tri par insertion**, écrit comme ci-dessus, est dit "**stable**" car, en cas de **valeurs identiques** dans le tableau initial, leur **ordre** relatif n’est **pas modifié**.

### Une petite animation

!!! success "Simulation du tri par insertion"
    <span style="color:green">En vert</span> : éléments déjà triés<br />
    <span style="color:#a3a3a3">En gris</span> : éléments à trier
    <div class="container-trii">
        <div class="array-trii-wrapper">
            <ul id="array-trii"></ul>
        </div>
        <div class="memory">
            <label for="memory-value">Espace mémoire:</label>
            <input id="memory-value" type="text" readonly>
        </div>
        <div class="buttons-trii">
            <button id="start-sort" class="md-button">Lancer le tri</button>
            <button id="step-sort" class="md-button">Pas à pas</button>
        </div>        
    </div>

## Implémentation en Python

Maintenant que l'on a déterminé l'**algorithme** du **tri par insertion**, on peut l'**implémenter en Python**.

**Téléchargez** le programme squelette (à compléter) ci-dessous.

!!! success "<span id="fichiers_python">Fichiers Python</span>"
    - [tri_insertion.py](src/tri_insertion.py){ target="_blank" } : programme **Python** avec les fonctions à compléter.
    - (à venir) : programme **Python** corrigé.

!!! tip "Module *doctest*"
    Dans la **docstring** de la fonction `tri_insertion`, des **tests** sont présents. Ces tests sont exécutés par le module natif *doctest*. Lorsque vous **exécutez** le programme, si les tests réussissent, **rien ne se passera**. Sinon, vous obtiendrez des informations sur les tests qui ont échoué.

    La fonction `testmod` (qui exécute les **tests**) est appelée dans la **dernière ligne** du programme. Pour obtenir davantage d'informations sur les erreurs liées aux tests, vous pouvez activer le mode *verbeux* en remplaçant le paramètre `verbose=False` par `verbose=True`.

!!! note "Exercice préliminaire"
    Dans les **tests** présents dans la docstring de la fonction `tri_insertion`, la première instruction est la suivante :  
    `>>> l = [randint(0, 99) for _ in range(10)]`  
    **Expliquez** ce que fait cette instruction.

!!! note "Exercice 1"
    **Écrivez** la fonction `tri_insertion`. Exécutez le programme pour vous assurer que votre fonction soit correcte (il ne doit rien se passer).

!!! note "Exercice 2"
    **Écrivez** la fonction `tri_insertion_decroissant` permettant de **trier un tableau dans l'ordre décroissant**. Que faut-il changer par rapport à la fonction `tri_insertion` ?

## Coût de l'algorithme

Comme pour le tri par sélection, on analysera le **coût algorithmique** du **tri par insertion** en comptant le **nombre de comparaisons** effectuées entre deux éléments du tableau.

!!! success "<span id="fichiers_python">Fichier Python</span>"
    - [tri_insertion_comp.py](src/tri_insertion_comp.py){ target="_blank" } : programme **Python** permettant de visualiser le déroulement du tri et le nombre de comparaisons effectuées.

    Vous n'avez pas besoin de modifier ce fichier en dehors du contenu des deux **variables globales** :

    - `TABLEAU` : Tableau donné en **entrée** à la fonction effectuant le **tri par insertion**.
    - `MODE_SLEEP` : Permet d'activer le mode "pas à pas". En activant ce mode, vous devrez appuyer sur la touche "Entrer" lorsque demandé afin de passer à l'étape suivante. Affectez la variable à `True` activer ce mode, ou à `False` sinon.

!!! note "Exercice 1"
    Téléchargez le **fichier Python** ci-dessus.

    1. Exécutez ce programme avec un **tableau** de **5 éléments triés dans l'ordre décroissant**. Combien y a t-il de comparaisons :
        - à la **première** itération ($i = 1$) ?
        - à la **deuxième** itération ($i = 2$) ?
        - à la **troisième** itération ($i = 3$) ?
        - à la **quatrième** itération ($i = 4$) ?
        - au **total** ?
    2. Faites la même chose que précédemment avec un **tableau** de **5 éléments triés dans l'ordre croissant**.
    3. Selon vous, quel est le **meilleur des cas** et le **pire des cas** concernant le tableau donné en entrée de la fonction de **tri par insertion** ?

!!! tip "Rappel sur les complexités"
    Voici un rappel sur les différentes complexités :
    
    - Logarithmique $Θ(log~n)$ : la complexité évolue **moins vite** que le nombre **n** de données (par exemple : si on multiplie le nombre de données **n** par **2**, on ne rajoute qu'**une seule** opération).
    - Linéaire $Θ(n)$ : la complexité évolue **comme** le nombre **n** de données (par exemple : si on multiplie le nombre de données **n** par **2**, le temps d'exécution est multiplié par **2**).
    - Quasi-linéaire $O(n~log~n)$ : Intermédiaire entre linéaire et quadratique. En pratique, un algorithme de complexité quasi-linéaire a un comportement très proche d’un algorithme de complexité linéaire.
    - Quadratique $Θ(n^2)$ : la complexité évolue **comme le carré** du nombre **n** de données (par exemple : si on multiplie le nombres de données **n** par **2**, le temps d'exécution est multiplié par **4**).
    - Exponentielle $Θ(2^n)$ : la complexité évolue à terme **beaucoup plus vite** que n'importe quelle fonction polynomiale du nombre **n** de données (par exemple : si on multiplie le nombre de données **n** par **100**, le temps d'exécution est multiplié par $2^{100}$, soit **1267650600228229401496703205376**).

    <figure markdown>
    <center>
    ![Graphe des complexités algorithmiques](images/graphique_complexites.png)
    <figcaption>Courbes d'évolution des différentes complexités algorithmiques.<br />(généré avec [ce programme](src/graphique_complexites.py){ target="_blank" })</figcaption>
    </center>
    </figure>

!!! note "Exercice 2"
    Exécutez le programme avec des **tableaux triés dans l'ordre croissant** de différentes **longueurs**. Pour une longueur $n$ donnée, quel sera le nombre $C(n)$ de **comparaisons** obtenu dans le cas où le **tableau** est **trié dans l'ordre croissant** ?

    En déduire le **coût du tri par insertion** dans le **meilleur des cas** (logarithmique ? linéaire ? quasi-linéaire ? quadratique ? exponentiel ?).

!!! note "Exercice 3"
    Exécutez le programme avec des **tableaux triés dans l'ordre décroissant** :

    - de longueur $5$,
    - de longueur $6$,
    - de longueur $7$.

    On notera le nombre de comparaisons sous la forme $C(n) = C_i(1) + C_i(2) + [...] + C_i(n-2) + C_i(n - 1)$ avec $n$ la **longueur du tableau** et $C_i(i)$ le **nombre de comparaisons** effectuées à l'**itération** $i$.
    
    Pour une longueur $n$ donnée, quel sera donc le nombre $C(n)$ de **comparaisons** obtenu dans le cas où le **tableau** est **trié dans l'ordre décroissant** ?

    En déduire le **coût du tri par insertion** dans le **meilleur des cas** (logarithmique ? linéaire ? quasi-linéaire ? quadratique ? exponentiel ?).
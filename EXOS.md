# Exercice 1


On veut faire un logiciel de géométrie. 


Une classe Square (Carré) munie de la propriété `edge_size` (taille d'un bord).

Une classe Rectangle munie des propriétés `width` et `height` (largeur et hauteur).

Une classe Circle (Cercle) munie de la propriété `radius` (rayon).

Pour chacune de ces classes, une méthode `get_area() -> float` (aire), une méthode `get_perimeter() -> float` (périmètre).

Un objet ShapeManager muni des méthodes `add_shape(forme)` (ajout d'une forme), `remove_shape(forme)` (retrait d'une instance de forme), `get_all_shapes()` (renvoie la liste de toutes les formes gérées), `get_total_area()` (renvoie la somme de toutes les aires de toutes les formes ajoutées).

1/ Écrire les tests unitaires pour Square, Rectangle et Circle et les exécuter.

Rappels:

- pour Square, périmètre = `edge_size * 4`, aire = `edge_size ** 2`.
- pour Circle, périmètre = `2 * pi * radius`, aire = `pi * radius ** 2`

2/ Écrire les tests unitaires pour ShapeManager, suggérer une approche pour tester chacune des méthodes.

3/ Publier dans Git.

# Exercice 2

On veut faire un logiciel de to-do list (gestionnaire de tâches).

0/ Forker ce dépôt pour vos travaux

1/ Définir les fonctionnalités de base d'une to-do list et proposer une technique pour tester chaque fonctionnalité listée. Rédiger un fichier SPECS.md (au format texte ou Markdown) avec ces informations.

2/ Écrire les tests unitaires correspondant à la fonctionnalité Créer une tâche. Exécuter les tests pour vérifier qu'ils sont bien en échec pour le moment car le code n'est pas prêt. Faire un commit dans Git de votre code + docs.

3/ Implémenter le code minimal pour faire passer un test. Constater. Commit dans Git.

4/ Ajouter les autres fonctionnalités au fur et à mesure en itérant. D'abord, le test, puis le test doit échouer à l'exécution puis on progresse jusqu'à ce que tout marche. Une fois que c'est bon, commit dans Git.

5/ Identifier dans le code d'éventuelles redondances, refactorer, vérifier que les tests passent toujours. Commit dans Git.

6/ Ajouter une fonctionnalité de sauvegarde permanente dans une base de données texte ou SQlite par exemple. Écrire les tests et ajouter la fonctionnalité. Créer une branche `persistance` dans Git et commit.

7/ Push la branche principale et la branche `persistance`.

8/ Merge persistance dans la branche principale et push encore.

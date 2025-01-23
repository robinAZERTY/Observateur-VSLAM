# Introduction aux observateurs
## Qu'est-ce qu'un observateur ?
En robotique, les observateurs permettent d'estimer des grandeurs qui ne sont pas forcement mesurable directement. Ils ont de nombreux autres buts, comme la réduction du bruit de mesure, ou la fusion de plusieurs capteurs pour fiabiliser ou rendre plus précis une estimation. Un observateur est aussi un estimateur d'états, les filtres bayésiens sont des observateurs.
![manimations\media\videos\1080p60\Observateurs.mp4.png](manimations\media\videos\1080p60\Observateurs.mp4.png)

## Filtrage bayésien
Dans la logique du filtrage bayésien, aucune grandeurs n'est considérée comme parfaitement connue. On ne cherche donc pas à estimer une valeur exacte, mais plutôt une distribution de probabilité. Cependant, par soucis de simplicité dans ce cours, sachez que lorsque l'on parle d'estimation, on parle en réalité d'estimation de la distribution de probabilité de la grandeur à estimer.
![a](manimations\media\videos\1080p60\DensiteProb.mp4.gif)

Le filtrage suis la logique des chaines de Markov : pour estimer l'état du système, nous n'avons besoins que de l'estimation précédente et de la mesure actuelle.
<!-- graphique de chaîne de Markov pour le filtrage bayésien-->
![b](manimations\media\videos\1080p60\Markov.mp4.gif)

### Notations
- $X$ : ***vecteur d'état du système*** (contient les grandeurs à estimer)
- $U$ : ***vecteur de commande*** (contient les grandeurs de commande)
- $f(X,U)$ : ***modèle de prédiction*** (décrit l'évolution du système en fonction de la commande)
- $Z$ : ***vecteur de mesure*** (contient les grandeurs mesurées)
- $h(X)$ : ***modèle de mesure*** (décrit la relation entre l'état du système et la mesure)
- Les estimations sont notées $\hat{X}$ et leur densité de probabilité $p(\hat{X})$

### Méthode
Pour mettre en place un filtrage bayésien, deux informations sont nécessaires :
- Le modèle de prédiction $f(X,U)$ qui permet de décrire l'évolution du système en fonction de la commande.
- Le modèle de mesure $h(X)$ qui permet de décrire la relation entre l'état du système et la mesure.
<!-- graphique des étapes de filtrage bayésien -->

### Étapes
1. **Prédiction de l'état du système**. On sait comment le système est sensé évoluer. On peut alors propage la distribution de probabilité de l'état du système estimé à l'instant précédent en utilisant le modèle de prédiction, en fonction de la commande.

<!-- graphique de la densité de probabilité de l'état du système avant prédiction -->
<!-- graphique de la densité de probabilité de l'état du système après prédiction -->

2. **Mise à jour de l'état du système**. Lorsqu'une nouvelle mesure de capteur est disponible, on peut effectuer cette étape. On calcule les mesure qu'on s'attend à obtenir en fonction de l'état du système prédit, puis on compare avec la mesure réelle. On peut alors mettre à jour la distribution de probabilité de l'état du système "par procédé d'éliminations des hypothèses les moins probables".

<!-- graphique de calcul de mesure selon l'état du système -->
<!-- graphique de la densité de probabilité de la mesure effectuée -->
<!-- graphique de la densité de probabilité de l'état du système après mise à jour -->
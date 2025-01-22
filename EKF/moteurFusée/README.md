# Cas n°1 : moteur fusée
### Structure du système
![Animation Manim](media/videos/1080p60/Engine.mp4.gif)
### Énoncé
On souhaite controller la température dans la chambre de combustion d'un moteur de fusée car si elle est trop élevée, le moteur peut exploser. On dispose d'un capteur de température, mais il est déporté car autrement il ne résisterait pas très longtemps à la chaleur. On souhaite donc estimer la température dans la chambre de combustion, sachant qu'on ne peut pas la mesurer directement.

### Dynamique du système
Le carburant en combustion fait chauffer la chambre de combustion. Ensuite, la chambre de combustion évacue sa chaleur par rayonnement vers le vide ou par conduction vert d'autres éléments. Pour finir, une infime partie de la chaleur est transmise au compartiment du capteur, par conduction.
<!-- diagramme des échanges thermiques-->

- ```math
X = \begin{bmatrix} T_{com} \\ T_{cap} \end{bmatrix}```
 : vecteur d'état du système, avec $T_{com}$ la température dans la chambre de combustion, et $T_{cap}$ la température au niveau du compartiment capteur.
- $U = \begin{bmatrix} P\end{bmatrix}$ : vecteur de commande, avec $P$ la puissance injectée dans le moteur.
- $f(X,U) = \begin{bmatrix} T_{com} + \Delta t*\frac{P}{C} * (1 - T_{cap} - T_{ext}) \\ T_{cap} + \Delta t*\alpha * (T_{com} - T_{cap}) \end{bmatrix}$ : modèle de prédiction, avec $\Delta t$ le pas de temps, $C$ la capacité thermique de la chambre de combustion, $T_{ext}$ la température extérieure, et $\alpha$ le coefficient de conduction entre la chambre de combustion et le compartiment capteur.


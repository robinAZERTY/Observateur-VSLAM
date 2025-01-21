# Filtre de Kalman Étendu (EKF)
C'est un type de filtre bayésien largement utilisé pour les système embarqué. Il est relativement simple à mettre en place et est utilisable pour un grand nombre de cas concrets. Il est basé sur le filtre de Kalman, mais est plus général car il peut être utilisé pour des systèmes non-linéaires.

## Quand l'utiliser ?
- Lorsque les distributions de probabilité sont gaussiennes ou presque.
- Lorsque les modèles de prédiction et de mesure sont linéaires ou presque à l’échelle des distributions de probabilité.
<!-- graphique avec distribution ok, et pas ok pour l'étape de prédiction -->








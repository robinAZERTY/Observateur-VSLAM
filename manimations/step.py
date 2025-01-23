from manim import *
import os
import numpy as np

# Définir le chemin d'exportation dans le même répertoire que le script
current_directory = os.path.dirname(os.path.abspath(__file__))
config.media_dir = os.path.join(current_directory, "media")


'''
Dans le filtrage bayésien ont distingue deux étapes :
- Prédiction : on estime l'état futur du système en fonction de l'état actuel et de la commande.
- Mise à jour : on corrige l'estimation en fonction de la mesure actuelle.
'''


class Step(MovingCameraScene):
    def construct(self):
        step = VGroup(
            Text("Prédiction").scale(1.5).set_color(ORANGE),
            Text("Mise à jour").scale(1.5).set_color(RED)
        ).arrange(DOWN)
            
        
if __name__ == "__main__":
    config.format = "mp4"
    Step().render()
    config.format = "gif"
    Step().render()
    
        
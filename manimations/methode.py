from manim import *
import os
import numpy as np

# Définir le chemin d'exportation dans le même répertoire que le script
current_directory = os.path.dirname(os.path.abspath(__file__))
config.media_dir = os.path.join(current_directory, "media")


'''
Pour mettre en place un filtrage bayésien, deux informations sont nécessaires :
- Le modèle de prédiction $f(X,U)$ qui permet de décrire l'évolution du système en fonction de la commande.
- Le modèle de mesure $h(X)$ qui permet de décrire la relation entre l'état du système et la mesure.

'''


class Methode(MovingCameraScene):
    def construct(self):
        Title = Text("Méthode").scale(1.5).to_edge(UP)
        underline = Underline(Title)
        
        DefineX = VGroup(
            Text("définir "),
            MathTex(r"X").scale(1.5).set_color(BLUE)
        ).arrange()

        fxu = MathTex(r"f(X,U)").scale(1.5)
        fxu[0][2].set_color(BLUE)
        fxu[0][4].set_color(ORANGE)
        DesignerF = VGroup(
            Text("designer "),
            fxu
            
        ).arrange().next_to(DefineX, 2 * DOWN)
        
        hx = MathTex(r"h(X)").scale(1.5)
        hx[0][2].set_color(BLUE)
        DesignerH = VGroup(
            Text("identifier "),
            hx   
        ).arrange().next_to(DesignerF, 2 * DOWN)             
        
        
        self.play(Write(Title))
        self.play(Write(underline))
        self.play(FadeIn(DefineX))
        self.wait(2)
        self.play(FadeIn(DesignerF))
        self.wait(2)
        self.play(FadeIn(DesignerH))        
        self.wait(2)
        
        
        
            
        
if __name__ == "__main__":
    config.format = "mp4"
    Methode().render()
    
        
from manim import *
from manim import config
import os


# Définir le chemin d'exportation dans le même répertoire que le script
current_directory = os.path.dirname(os.path.abspath(__file__))
config.media_dir = os.path.join(current_directory, "media")

'''
Dans la logique du filtrage bayésien,
aucune grandeurs n'est considérée comme parfaitement connue.
On ne cherche donc pas à estimer une valeur exacte, mais plutôt une distribution de probabilité.
Cependant, par soucis de simplicité dans ce cours, sachez que lorsque l'on parle d'estimation,
on parle en réalité d'estimation de la distribution de probabilité de la grandeur à estimer.
'''

# faire un diagramme qui représente les différents blocs des systèmes d'un robot mobile
class DensiteProb(MovingCameraScene):
    def construct(self):
        # afficher le plan
        self.add(ThreeDAxes())
        
        self.camera.frame.move_to(3*UP+4*RIGHT)
        
        
        # aficher un point avec une fleche montrant la position du robot
        robot = Dot([2,2,0], color=BLUE)
        robotArrow = Arrow([2,2,0], [4,4,0])
        robotText = Text("position du robot").scale(0.75).next_to(robotArrow.get_end(), RIGHT, buff=0.1).shift(0.1*UP)
        
        self.play(Create(robot))
        self.play(Create(robotArrow))
        self.play(Write(robotText))
        
        
        # barrer la position du robot pour montrer qu'elle est incertaine
        robotGroup = VGroup(robot, robotArrow, robotText)
        cross = Cross(robotGroup)
        self.play(Create(cross))
        
        self.wait(1)
        
        # dessiner une forme pour représenter la densité de probabilité bleu dont la transparence est fonction de la probabilité
        # Création d'une ellipse
        ellipse = Ellipse(
            width=2,  # Largeur de l'ellipse
            height=1,  # Hauteur de l'ellipse
            color=BLUE,  # Couleur de l'ellipse
            fill_opacity=0.5  # Opacité du remplissage
        )
        
        # Position de l'ellipse
        ellipse.move_to([2, 2, 0])
        
        # Affichage de l'ellipse
        self.play(FadeOut(cross),FadeOut(robotArrow))
        newRobotTxt = robotText.copy().move_to(ellipse.get_center()+UP*ellipse.height)
        self.play(Transform(robot, ellipse), Transform(robotText, newRobotTxt))
        
        
        
    
        
        
        
if __name__ == "__main__":
    
    config.format = "mp4"
    DensiteProb().render()
    config.format = "gif"
    DensiteProb().render()
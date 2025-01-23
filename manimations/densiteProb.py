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
        
        axes = ThreeDAxes()
        # Dessiner une gaussienne 2D pour représenter la densité de probabilité
        def gaussian_2d(x, y, mu, cov):
            pos = np.array([x, y])
            inv_cov = np.linalg.inv(cov)
            diff = pos - mu
            exponent = -0.5 * np.dot(np.dot(diff.T, inv_cov), diff)
            return np.exp(exponent)
        
        mu = np.array([2, 2])
        cov = np.array([[0.5, 0.1], [0.1, 0.5]])
        
        # Créer la surface de la gaussienne
        surface = Surface(
            lambda u, v: axes.c2p(u, v, gaussian_2d(u, v, mu, cov)),
            u_range=[mu[0] - 2.5*np.sqrt(cov[0, 0]), mu[0] + 2.5*np.sqrt(cov[0, 0])],
            v_range=[mu[1] - 2.5*np.sqrt(cov[1, 1]), mu[1] + 2.5*np.sqrt(cov[1, 1])],
            resolution=(100, 100),
            fill_opacity=1,
            stroke_width=0,
        ).set_fill_by_value(axes, colorscale=[(BLACK, 0), (BLUE, gaussian_2d(mu[0],mu[1],mu, cov))], axis=2)
                    
        self.play(FadeOut(cross), FadeOut(robotArrow))
        newRobotTxt = robotText.copy().next_to(surface, UP+RIGHT, buff=0.2)
        self.play(FadeOut(robot), FadeIn(surface), Transform(robotText, newRobotTxt))
        
        self.wait(2)
        
        
        
    
        
        
        
if __name__ == "__main__":
    
    config.format = "mp4"
    DensiteProb().render()
    config.format = "gif"
    DensiteProb().render()
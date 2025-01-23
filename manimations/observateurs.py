from manim import *
from manim import config
import os


# Définir le chemin d'exportation dans le même répertoire que le script
current_directory = os.path.dirname(os.path.abspath(__file__))
config.media_dir = os.path.join(current_directory, "media")

'''
# Introduction aux observateurs
## Qu'est-ce qu'un observateur ?
En robotique, les observateurs permettent d'estimer des grandeurs qui ne sont pas forcement mesurable directement. Ils ont de nombreux autres buts, comme la réduction du bruit de mesure, ou la fusion de plusieurs capteurs pour fiabiliser ou rendre plus précis une estimation. Un observateur est aussi un estimateur d'états, les filtres bayésiens sont des observateurs.

<!-- graphique des différents types d'observateurs et de filtrage bayésien -->
'''

# faire un diagramme qui représente les différents blocs des systèmes d'un robot mobile
class Observateurs(MovingCameraScene):
    def construct(self):
        ControlTheory = Text("Théorie du contrôle").scale(1.5).move_to([0,3,0])
        
        #blocks controlleur et système
        controller = Rectangle(height=1.5, width=3, fill_opacity=0.5).set_color(GRAY).move_to([-2.5, 0, 0]).set_stroke(width=2)
        controllerTxt = Text("contrôleur").scale(0.5).move_to(controller.get_center())
        
        # # placer le texte au dessus du rectangle dynamiquement
        system = Rectangle(height=1.5, width=3, fill_opacity=0.5).set_color(GRAY).move_to([2.5, 0, 0]).set_stroke(width=2)
        systemTxt = Text("système").scale(0.5).move_to(system.get_center())
        
        # # placer un comparateur devant le controller
        comparator = Circle(radius=0.3, fill_opacity=0.5).set_color(GRAY).next_to(controller, LEFT, buff=1)
        comparatorCross = Cross(comparator).set_color(GRAY).scale(0.75)
            
        # # ajouter une consigne en entrée du comparateur avec un text et une ligne
        refLine = Line(start=comparator.get_left() + 1.5*LEFT, end = comparator.get_left())
        refTxt = Text("consigne").scale(0.4).next_to(refLine, UP, buff=0.1)
                
        # # ajouter l'erreur en sortie du comparateur avec un text et une ligne
        errorLine = Line(start=comparator.get_right(), end = controller.get_left())
        errorTxt = Text("erreur").scale(0.4).next_to(errorLine, UP, buff=0.1)
        
        # # ajouter une commande en sortie du contrôleur avec un text et une ligne
        commandLine = Line(start=controller.get_right(), end = system.get_left())
        commandTxt = Text("commande").scale(0.4).next_to(commandLine, UP, buff=0.1)
        
        # ajouter un capteur en dessous du controller et du système
        ConPlusSys = VGroup(controller, system)
        sensor = Rectangle(height=1, width=2, fill_opacity=0.5).set_color(GRAY).next_to(ConPlusSys, DOWN, buff=1).set_stroke(width=2)
        sensorTxt = Text("capteur").scale(0.5).move_to(sensor.get_center())
        
        # ajouter 3 lignes pour faire parvenir l'état du système au capteur
        stateLine1 = Line(start=system.get_right(), end = system.get_right() + 1*RIGHT)
        # la fin de la ligne 2 s'arrête à la hauteur du capteur mais à la même position horizontale que la fin de la ligne 1
        Line2End = [stateLine1.get_end()[0], sensor.get_right()[1], 0]
        stateLine2 = Line(start=stateLine1.get_end(), end = Line2End)
        stateLine3 = Line(start=stateLine2.get_end(), end = sensor.get_right())
        stateLine = VGroup(stateLine1, stateLine2, stateLine3)
        stateTxt = Text("état").scale(0.4).next_to(stateLine2, RIGHT, buff=0.1) 
        
        # ajouter 2 lignes pour faire parvenir l'estimation de l'état du système au capteur au comparateur
        line1End = [comparator.get_center()[0], sensor.get_left()[1], 0]
        estimationLine1 = Line(start=sensor.get_left(), end = line1End)
        estimationLine2 = Line(start=estimationLine1.get_end(), end = comparator.point_at_angle(-PI/2))
        estimationLine = VGroup(estimationLine1, estimationLine2)
        estimationTxt = Text("état estimé").scale(0.4).next_to(estimationLine1, UP, buff=0.1)
        
        
        
        self.play(Write(ControlTheory))
        # faire apparaitre la ligne de consigne de gauche à droite
        self.play(Create(refLine), Create(refTxt), Create(comparator), Create(comparatorCross), Create(errorLine), Create(errorTxt))
        self.play(FadeIn(controller), Create(controllerTxt))
        self.play(Create(commandLine), Create(commandTxt))
        self.play(FadeIn(system), Create(systemTxt))
        self.play(Create(stateLine), Create(stateTxt), Create(sensor), Create(sensorTxt))
        self.play(Create(estimationLine), Create(estimationTxt))
        self.wait(20)
        
        # ramplacer Xhat par Xhat != mesure
        redCross = Cross(estimationTxt).set_color(RED).scale(0.75).set_stroke(width=4)
        self.play(Create(redCross))
        self.wait(5)

        # décaler le capteur vers la droite en conservant le lien avec la ligne d'état
        oldSensor = VGroup(sensor, sensorTxt, stateLine3)
        newSensor = oldSensor.copy().next_to(sensor, RIGHT, buff=1)
        newSensor[2] = Line(start=stateLine2.get_end(), end = newSensor[0].get_right())
        self.play(Transform(oldSensor, newSensor))
        
        # ajouter un bloc d'observateur
        observer = Rectangle(height=1.5, width=3, fill_opacity=0.5).set_color(BLUE).next_to(sensor.get_left(), LEFT, buff=1.5).set_stroke(width=2)
        observerTxt = Text("observateur").scale(0.5).move_to(observer.get_center())
        newStateEstimationLine1 = Line(start=observer.get_left(), end = estimationLine2.get_start())
        
        # # ajouter une ligne pour faire parvenir les mesures du capteur à l'observateur
        measureLine = Line(start=sensor.get_left(), end = observer.get_right())
        measureTxt = Text("mesure").scale(0.4).next_to(measureLine, UP, buff=0.1)

        self.play(FadeIn(observer), Create(observerTxt), Transform(estimationLine1, newStateEstimationLine1), FadeOut(redCross), Transform(estimationTxt, estimationTxt.copy().next_to(newStateEstimationLine1, UP, buff=0.1)))
        self.play(Create(measureLine), Create(measureTxt))
        self.wait(10)   
        
        # zoom sur le bloc observateur
        self.play(
            self.camera.frame.animate.move_to(observer).set(height=observer.height),
            FadeOut(observer),
        )
        self.wait(5)
        ObsEq = Text("observateur = estimateur d'état").scale(0.2).move_to(observerTxt.get_center())
        self.play(Transform(observerTxt, ObsEq))
        self.wait(3)
        # placer le texte en haut
        newEstText = Text("estimateur d'état").next_to(observer, UP, buff=-0.4).scale(0.3)
        underline = Underline(newEstText).set_stroke(width=2)
        self.play(Transform(observerTxt, newEstText))
        self.play(Create(underline))
        self.wait(5)
        
        # dans les filtres bayésiens, il y a des filtres à particules, des filtres de Kalman, des filtres de Kalman étendus et des filtres de Kalman non linéaires, etc.
        # ajouter un texte pour expliquer les différents types de filtres bayésiens
        bayenianTxt = Text("filtres bayésiens").scale(0.2).move_to(self.camera.frame.get_center())
        particleFilter = Text("filtres à particules").scale(0.15).next_to(bayenianTxt, DOWN, buff=self.camera.frame.get_height()/4).shift(LEFT*self.camera.frame.get_width()/4)
        kalmanFilter = Text("filtres de Kalman").scale(0.15).next_to(bayenianTxt, DOWN, buff=self.camera.frame.get_height()/4).shift(RIGHT*self.camera.frame.get_width()/4)
        bayeniantxt_down = bayenianTxt.get_center() + DOWN*bayenianTxt.get_height()/2
        particleFilter_up = particleFilter.get_center() + UP*particleFilter.get_height()/2
        kalmanFilter_up = kalmanFilter.get_center() + UP*kalmanFilter.get_height()/2
        
        line1 = Line(start=bayeniantxt_down+LEFT*bayenianTxt.get_width()/3, end = particleFilter_up).set_stroke(width=2)
        line2 = Line(start=bayeniantxt_down+RIGHT*bayenianTxt.get_width()/3, end = kalmanFilter_up).set_stroke(width=2)
        self.play(FadeIn(bayenianTxt))
        self.play(FadeIn(particleFilter), Create(line1))
        self.play(FadeIn(kalmanFilter), Create(line2))
        self.wait(5)
        


        
if __name__ == "__main__":
    config.format = "mp4"
    Observateurs().render()
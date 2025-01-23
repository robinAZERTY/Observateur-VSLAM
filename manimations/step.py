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
        step = Text("Étapes du filtrage bayésien").scale(1.5).to_edge(UP)
        
        prediction = Text("prédiction").scale(1).next_to(step, DOWN, buff=2)
        predUnderline = Underline(prediction).set_color(ORANGE)
        pred = VGroup(prediction, predUnderline)
        
        update = Text("mise à jour").scale(1).next_to(prediction, DOWN, buff=1)
        updateUnderline = Underline(update).set_color(RED)
        upd = VGroup(update, updateUnderline)
                
        self.play(Write(step))
        self.wait(2)
        self.play(FadeIn(pred),FadeIn(upd))
        self.wait(3)
        self.play(FadeOut(step),FadeOut(upd),pred.animate.to_edge(UP))
        
        prevState = Text("estimation précédente").scale(0.75).to_edge(LEFT).set_color(BLUE).shift(RIGHT*0.75)
        prevStateex = MathTex(r"18°C").scale(1).move_to(prevState).set_color(BLUE)
        XhatMOne = MathTex(r"\hat{X}_{k-1}").scale(1).move_to(prevState).set_color(BLUE)
        
        predState = Text("nouvelle estimation").scale(0.75).next_to(prevState, RIGHT, buff=3).set_color(BLUE)
        predStateex = MathTex(r"19°C").scale(1).move_to(predState).set_color(BLUE)
        Xhat = MathTex(r"\hat{X}_{k}").scale(1).move_to(predState).set_color(BLUE)
        
        command = Text("commande").scale(0.75).next_to(predState, DOWN+LEFT, buff=1).set_color(ORANGE)
        commandex = MathTex(r"2kW").scale(1).move_to(command).set_color(ORANGE)
        U = MathTex(r"U_{k}").scale(1).move_to(command).set_color(ORANGE)
        
        a1 = Arrow(prevState, predState)
        a2 = Arrow(command, predState)
        self.play(Write(prevState), Write(command))
        self.wait(1)
        self.play(Write(predState), Write(a1), Write(a2))
        self.wait(1)
        self.play(Transform(prevState, prevStateex))
        self.wait(1)
        self.play(Transform(command, commandex))
        self.wait(1)
        self.play(Transform(predState, predStateex))
        self.wait(3)
        self.play(Transform(prevState, XhatMOne), Transform(command, U), Transform(predState, Xhat))
        self.wait(2)
        
        Equation = MathTex(r"\hat{X}_{k} = f(\hat{X}_{k-1}, U_{k})").scale(1)
        Equation[0][0:3].set_color(BLUE)
        Equation[0][6:11].set_color(BLUE)
        Equation[0][12:14].set_color(ORANGE)
                
        self.play(FadeOut(a1), FadeOut(a2), Transform(VGroup(prevState, command, predState), Equation))
        self.wait(2)
        
        
        
            
        
if __name__ == "__main__":
    config.format = "mp4"
    Step().render()

    
        
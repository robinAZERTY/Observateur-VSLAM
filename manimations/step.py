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
        self.play(FadeOut(predState), FadeOut(a1), FadeOut(a2), FadeOut(prevState), FadeOut(command))
        # self.play(Transform(prevState, prevStateex))
        # self.wait(1)
        # self.play(Transform(command, commandex))
        # self.wait(1)
        # self.play(Transform(predState, predStateex))
        # self.wait(3)
        # self.play(Transform(prevState, XhatMOne), Transform(command, U), Transform(predState, Xhat))
        # self.wait(2)
        
        
        
      # Adding the probability distribution graph with mu and sigma
        mu = 18
        sigma = 0.75

        axes = Axes(
            x_range=[15, 25, 1],
            y_range=[0, 0.5, 0.1],
            axis_config={"color": WHITE},
            x_length=6,
            y_length=3,
        ).shift(DOWN*0.5)

        graph = axes.plot(lambda x: (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2), color=BLUE)
        label = MathTex(r"p(\hat{X}_{k-1})").next_to(graph, UP, buff=0.1).shift(RIGHT)
        label[0][2:-1].set_color(BLUE)
        # graph_label = axes.get_graph_label(graph, label=label, x_val=mu, direction=RIGHT).shift(RIGHT*0.5+UP*0.5)

        mu_label = MathTex(str(mu)).next_to(axes.c2p(mu, 0), DOWN)
        mu_dot = Dot(point=axes.c2p(mu, 0), color=BLUE)

        self.play(Create(axes), Create(graph), Write(label))
        self.play(FadeIn(mu_dot), Write(mu_label))
        self.wait(3)


        # Updating the graph with the new mu and sigma
        mu = 19
        sigma = 1
        predicted = axes.plot(lambda x: (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2), color=BLUE)
        predictedLabel = MathTex(r"p(\hat{X}_{k})").next_to(predicted, UP, buff=0.1).shift(RIGHT)
        predictedLabel[0][2:-1].set_color(BLUE)
        predictedmu_label = MathTex(str(mu)).next_to(axes.c2p(mu, 0), DOWN)
        predictedmu_dot = Dot(point=axes.c2p(mu, 0), color=BLUE)
        
        # fleche vers la droite pour illustrer la commande
        commandeArrow = Arrow(axes.c2p(18, 0.3), axes.c2p(20, 0.3), buff=0)
        commande = MathTex(r"U_{k}").next_to(commandeArrow, UP, buff=0.1).set_color(ORANGE).shift(RIGHT)
        
        self.play(Write(commandeArrow),Write(commande))
        self.wait(2)
        self.play(FadeOut(commandeArrow),FadeOut(commande),Transform(graph,predicted), Transform(label,predictedLabel), Transform(mu_dot,predictedmu_dot), Transform(mu_label,predictedmu_label))


        Equation = MathTex(r"\hat{X}_{k} = f(\hat{X}_{k-1}, U_{k})").scale(1)
        Equation[0][0:3].set_color(BLUE)
        Equation[0][6:11].set_color(BLUE)
        Equation[0][12:14].set_color(ORANGE)
        
        self.play(FadeOut(predicted),FadeOut(predictedLabel),FadeOut(predictedmu_dot),FadeOut(predictedmu_label))
        self.play(Write(Equation))
        self.wait(2)
        self.play(FadeOut(Equation))
        
                
        # self.play(FadeOut(a1), FadeOut(a2), Transform(VGroup(prevState, command, predState), Equation))
        # self.wait(2)
        
        # self.play(FadeOut(Equation), FadeOut(pred),FadeOut(VGroup(prevState, command, predState)))
        # self.wait(2)

        
        prevState = Text("estimation précédente").scale(0.75).to_edge(LEFT).set_color(BLUE).shift(RIGHT*0.75)
        prevStateex = MathTex(r"19°C").scale(1).move_to(prevState).set_color(BLUE)
        XhatMOne = MathTex(r"\hat{X}_{k-1}").scale(1).move_to(prevState).set_color(BLUE)
        
        predState = Text("nouvelle estimation").scale(0.75).next_to(prevState, RIGHT, buff=3).set_color(BLUE)
        predStateex = MathTex(r"19.5°C").scale(1).move_to(predState).set_color(BLUE)
        Xhat = MathTex(r"\hat{X}_{k}").scale(1).move_to(predState).set_color(BLUE)
        
        mesure = Text("mesure").scale(0.75).next_to(predState, DOWN+LEFT, buff=1).set_color(ORANGE)
        mesureex = MathTex(r"20°C").scale(1).move_to(mesure).set_color(ORANGE)
        U = MathTex(r"Z_{k}").scale(1).move_to(mesure).set_color(ORANGE)


        
        upd.move_to(pred)
        
        # a2 = Arrow(mesure, predState)
        # self.play(FadeIn(upd))
        # self.wait(2)
        # self.play(Write(prevState), Write(mesure),Write(predState),Write(a1),Write(a2))
        # self.wait(1)
        # self.play(Transform(prevState, prevStateex))
        # self.wait(1)
        # self.play(Transform(mesure, mesureex))
        # self.wait(1)
        # self.play(Transform(predState, predStateex))
        # self.wait(3)
        # self.play(Transform(prevState, XhatMOne), Transform(mesure, U), Transform(predState, Xhat))
        # self.wait(2)
        
        
        
        
        
        
        
        
        
        
            
        
if __name__ == "__main__":
    config.format = "mp4"
    Step().render()

    
        
from manim import *
import os
import numpy as np

# Définir le chemin d'exportation dans le même répertoire que le script
current_directory = os.path.dirname(os.path.abspath(__file__))
config.media_dir = os.path.join(current_directory, "media")


'''
Le filtrage suis la logique des chaines de Markov : pour estimer l'état du système, 
nous n'avons besoins que de l'estimation précédente et de la mesure actuelle.
'''


class Markov(MovingCameraScene):
    def construct(self):
        def new_Est(t = 0):
            # rond pour l'estimation (avec Xhat_t)
            Est = VGroup( 
            Circle(color=BLUE,  radius=0.5).set_fill(BLUE, opacity=0.5).move_to(4*RIGHT*t+UP),
            MathTex(r"\hat{X}_{"+str(t)+"}").move_to(4*RIGHT*t+UP)
            )
            return Est
        
        def add_measure(Est,t):
            #ajouter une mesure à un état
            c = Circle(color=RED, radius=0.5).set_fill(RED, opacity=0.5).move_to(Est.get_center()+3*(DOWN+LEFT))
            a = Arrow(c,Est)
            measure = VGroup(
            c,
            MathTex("Z_{"+str(t)+"}").move_to(Est.get_center()+3*(DOWN+LEFT)),
            a,
            # text sur la fleche pour indiquer qu'on fait une mise à jour
            MathTex(r"\text{Mise à jour}").move_to(a.get_center()+1.3*RIGHT).scale(0.75)
            )
            return measure
        
        def add_command(Est,t):
            #ajouter une commande à un état
            c = Circle(color=ORANGE, radius=0.5).set_fill(ORANGE, opacity=0.5).move_to(Est.get_center()+3*(DOWN+LEFT))
            a = Arrow(c,Est)
            command = VGroup(
            c,
            MathTex("U_{"+str(t)+"}").move_to(Est.get_center()+3*(DOWN+LEFT)),
            a,
            # text sur la fleche pour indiquer qu'on fait une prédiction
            MathTex(r"\text{Prédiction}").move_to(a.get_center()+1.3*RIGHT).scale(0.75)
            )
            return command
        
        measureChance = 0.5
            
        last_markov = new_Est(0)
        self.add(last_markov)
        for i in range(1,10):
            self.wait(1)
            new_markov = new_Est(i)
            rand = np.random.rand()
            if rand < measureChance:
                new_measure_or_command = add_measure(new_markov,i)
            else:
                new_measure_or_command = add_command(new_markov,i)
            # new_measure_or_command = add_measure(new_markov,i)
            camCenter = VGroup(last_markov,new_markov,new_measure_or_command).get_center()
            self.play(
            Create(Arrow(last_markov, new_markov)),
            self.camera.frame.animate.move_to(camCenter),
            FadeIn(new_markov),
            Create(new_measure_or_command)
            )
            last_markov = new_markov
            
            self.wait(2)
        
            
        
if __name__ == "__main__":
    config.format = "mp4"
    Markov().render()
    config.format = "gif"
    Markov().render()
    
        
from manim import *
from manim import config
import os


# Définir le chemin d'exportation dans le même répertoire que le script
current_directory = os.path.dirname(os.path.abspath(__file__))
config.media_dir = os.path.join(current_directory, "media")

'''
un observateur prend en entrée les commandes, et les mesures des capteurs
en sortie il donne une estimation de l'état du système
'''

# faire un diagramme qui représente les différents blocs des systèmes d'un robot mobile
class EntreeSortie(MovingCameraScene):
    def construct(self):
        Entrees = Text("Entrées").scale(1.5).move_to([0,3,0]).set_color(BLUE)
        underEntrees = Underline(Entrees)
        EntreesUnder = VGroup(Entrees, underEntrees)
        
        Mesures = Text("mesures : ").scale(1).move_to([0,0,0]).align_to(Entrees, LEFT).shift(LEFT*2)
        temp = Text("temperature").scale(1).next_to(Mesures, RIGHT, buff=0.1)
        MesureeqZ = MathTex("Z").scale(1).next_to(Mesures, RIGHT, buff=0.1)
        
        
        Commande = Text("commandes : ").scale(1).next_to(Mesures, DOWN, buff=1)
        CommandeEx = Text("chauffage").scale(1).next_to(Commande, RIGHT, buff=0.1)
        CommandeqU = MathTex("U").scale(1).next_to(Commande, RIGHT, buff=0.2)
        
        # ligne de separation au milieu de la page
        sepLine = Line([0,0,0], [0,3,0], color=WHITE).shift(LEFT*2).shift(DOWN*2)
        
        lillteEntree = Entrees.copy().scale(0.75)
        
        littleMesure = Mesures.copy().scale(0.75).next_to(Entrees, DOWN, buff=1)
        littleZ = MesureeqZ.copy().scale(0.75).next_to(littleMesure, RIGHT, buff=0.2)

        littleCommande = Commande.copy().scale(0.75).next_to(littleMesure, DOWN, buff=0.5)
        littleU = CommandeqU.copy().scale(0.75).next_to(littleCommande, RIGHT, buff=0.2)
        
        litlleEntreeGroup = VGroup(lillteEntree, littleMesure, littleZ, littleCommande, littleU)
        litlleEntreeGroup.next_to(sepLine, LEFT, buff=1)
        

        
        self.play(Write(Entrees))
        self.play(Write(underEntrees))
        self.wait(1)
        self.play(Write(Mesures))
        self.wait(1)
        self.play(Write(temp))
        self.wait(1)
        self.play(Transform(temp, MesureeqZ))
        self.wait(1)
        self.play(Write(Commande))
        self.wait(1)
        self.play(Write(CommandeEx))
        self.wait(1)
        self.play(Transform(CommandeEx, CommandeqU))
        self.wait(1)
        self.play(Transform(EntreesUnder,lillteEntree), Transform(Mesures, littleMesure), Transform(temp, littleZ), Transform(Commande, littleCommande), Transform(CommandeEx, littleU))
        self.play(Write(sepLine))
        
        Sortie = Text("Sortie").scale(1.5).move_to([1.5,2,0]).set_color(RED)
        underSortie = Underline(Sortie)
        SortieUnder = VGroup(Sortie, underSortie)
        
        Estimation = Text("estimation : ").scale(1).next_to(sepLine, RIGHT, buff=1.5)
        temp = Text("temperature").scale(1).next_to(Estimation, RIGHT, buff=0.1)
        # Xhat
        EstimationeqZ = MathTex("\hat{X}").scale(1).next_to(Estimation, RIGHT, buff=0.1)
        
        self.play(Write(Sortie))
        self.play(Write(underSortie))
        self.wait(1)
        self.play(Write(Estimation))
        self.wait(1)
        self.play(Write(temp))
        self.wait(1)
        self.play(Transform(temp, EstimationeqZ))
        self.wait(1)
    
                        
        
        
        
if __name__ == "__main__":
    
    config.format = "mp4"
    EntreeSortie().render()

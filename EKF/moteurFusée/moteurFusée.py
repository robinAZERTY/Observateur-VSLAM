from manim import *
from manim import config
import os
from itertools import cycle

ALL_COLORS = [RED, BLUE, GREEN, TEAL, YELLOW, PURPLE, MAROON, PINK, GOLD]


# Définir le chemin d'exportation dans le même répertoire que le script
current_directory = os.path.dirname(os.path.abspath(__file__))
config.media_dir = os.path.join(current_directory, "media")

from manim import *


   
class Engine(Scene):
    def construct(self):
        leftPoints = [
        [-0.2913114456738618,-1.0,0.0],
        [-0.27389805913295845,-0.8824596408489026,0.0],
        [-0.2477779793216035,-0.7518592417921277,0.0],
        [-0.2216578995102485,-0.6495555958643207,0.0],
        [-0.1911844730636677,-0.5450752766189008,0.0],
        [-0.15418102666424816,-0.4144748775621259,0.0],
        [-0.10847088699437694,-0.2904044984581898,0.0],
        [-0.06276074732450573,-0.17504081262470528,0.0],
        [-0.012697261019408691,-0.06403047342644662,0.0],
        [0.03954289860330126,0.04697986577181204,0.0],
        [0.09395973154362414,0.1471068383820061,0.0],
        [0.13096317794304368,0.21023036459278066,0.0],
        [0.13966987121349536,0.2319970977689098,0.0],
        [0.14184654453110826,0.25376383094503896,0.0],
        [0.14184654453110826,0.27335389080355516,0.0],
        [0.1353165245782695,0.29947397061491016,0.0],
        [0.12225648467259204,0.32777072374387806,0.0],
        [0.10919644476691454,0.353890803555233,0.0],
        [0.09613640486123705,0.37130419009613636,0.0],
        [0.08742971159078539,0.39960094322510425,0.0],
        [0.08307636495555956,0.4235443497188463,0.0],
        [0.08089969163794665,0.4496644295302013,0.0],
        [0.08089969163794665,0.47143116270633045,0.0],
        [0.08089969163794665,0.5127879557409758,0.0]
        ]
        rescale = 2.5
        # shift the points to the right
        leftPoints = [[x - 0.23, y, z] for x, y, z in leftPoints]
        # compute the left points by flipping the x axis
        rightPoints = [[-x, y, z] for x, y, z in leftPoints]
        
        leftPoints = [[x * rescale, y * rescale, z] for x, y, z in leftPoints]
        rightPoints = [[x * rescale, y * rescale, z] for x, y, z in rightPoints]
        points = leftPoints + rightPoints[::-1]
        
        background = Polygon(*points, fill_opacity=0.5, stroke_width=0).set_color([BLUE,RED]).set_sheen_direction(UP)
        
        # Combine left and right points but keep the tuyère open
        outline = VMobject().set_points_as_corners(points).set_color(GRAY)
        
        # ajouter des tuyaux de carburant
        fuel_pipe = Rectangle(height=1, width=0.1, fill_opacity=0.5).set_color(BLUE).move_to([0, 1.8, 0]).set_stroke(width=2)
        
        # Ajouter les annotations
        fuel_pipe_annotation = Text("Entrée de carburant").scale(0.4).move_to([2.5, 1.8, 0])
        fuel_pipe_line = Line(start=[0.1, 1.8, 0], end=[1.3, 1.8, 0]).set_color(WHITE)
        
        combustion_chamber_annotation = Text("Chambre de combustion").scale(0.4).move_to([-3, 1, 0])
        combustion_chamber_line = Line(start=[-0.5, 1, 0], end=[-1.5, 1, 0]).set_color(WHITE)

        tuyere_annotation = Text("Tuyère").scale(0.4).move_to([3.3, -1.5, 0])
        tuyere_line = Line(start=[1.2, -1.5, 0], end=[2, -1.5, 0]).set_color(WHITE)
        

        # Ajouter annotations et lignes
        self.add(tuyere_annotation, tuyere_line, fuel_pipe_annotation, fuel_pipe_line, combustion_chamber_annotation, combustion_chamber_line)
        self.add(background, outline, fuel_pipe) 
        

        


        # Taille de l'écran
        screen_height = config.frame_height

        # Position initiale et position hors écran en bas
        start_y = 0  # Position en haut de l'écran
        end_y = -screen_height / 2 - 1  # Position en dehors de l'écran en bas

        # Fonction pour créer une flèche animée
        def create_arrow():
            arrow = Elbow(width=0.5, angle=5 * PI / 4).set_color(RED)
            arrow.move_to([0, start_y, 0])  # Position initiale en haut
            arrow.set_stroke_width(1)  # Commence complètement transparent
            return arrow

        # Animation d'une seule flèche
        def animate_arrow(arrow, speed=1):
            # Animation de la flèche
            self.play(
                arrow.animate.shift([0, end_y - start_y, 0]).scale(4).set_stroke_width(20).set_color(ORANGE).set_opacity(0),
                rate_func=linear,
                run_time=1 / speed,
            )
            
        
        for i in range(6):
            arrow = create_arrow()
            animate_arrow(arrow, speed=2)
        

        # Attendre avant de terminer la scène
        self.wait()
        
if __name__ == "__main__":
    # Export en MP4
    config.format = "mp4"
    Engine().render()  # Rend en vidéo MP4
    
    # # Export en GIF
    config.format = "gif"
    Engine().render()  # Rend en GIF
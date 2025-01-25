from manim import *
from manim import config
import os
from itertools import cycle

ALL_COLORS = [RED, BLUE, GREEN, TEAL, YELLOW, PURPLE, MAROON, PINK, GOLD]


# Définir le chemin d'exportation dans le même répertoire que le script
current_directory = os.path.dirname(os.path.abspath(__file__))
config.media_dir = os.path.join(current_directory, "media")


'''
# Cas n°1 : moteur fusée
### Structure du système
![Animation Manim](../../manimations\media\videos\1080p60\Engine.mp4.gif)
### Énoncé
On souhaite controller la température dans la chambre de combustion d'un moteur de fusée car si elle est trop élevée, le moteur peut exploser. On dispose d'un capteur de température, mais il est déporté car autrement il ne résisterait pas très longtemps à la chaleur. On souhaite donc estimer la température dans la chambre de combustion, sachant qu'on ne peut pas la mesurer directement.

### Dynamique du système
Le carburant en combustion fait chauffer la chambre de combustion. Ensuite, la chambre de combustion évacue sa chaleur par rayonnement vers le vide ou par conduction vert d'autres éléments. Pour finir, une infime partie de la chaleur est transmise au compartiment du capteur, par conduction.
<!-- diagramme des échanges thermiques-->



$$\textbf{Vecteur d'état :}$$
$$X = \begin{bmatrix} T_{com} \\ T_{cap} \end{bmatrix}$$
$$\begin{aligned}
&\begin{aligned}
T_{com} &: \text{température dans la chambre de combustion}\\
T_{cap} &: \text{température au niveau du compartiment capteur}
\end{aligned}
\end{aligned}$$



$$\textbf{Vecteur de commande :}$$
$$U = \begin{bmatrix} P\end{bmatrix}$$
$$P : \textrm{la puissance thermique injectée dans la chambre de combustion.}$$



$$\textbf{Modèle de prédiction :}$$
$$f(X,U) = \begin{bmatrix} T_{com} + \Delta t*\frac{P}{C} * (1 - T_{cap} - T_{ext}) \\ T_{cap} + \Delta t*\alpha * (T_{com} - T_{cap}) \end{bmatrix}$$
$$\begin{aligned}
&\begin{aligned}
\Delta t &: \textrm{pas de temps} \\
C &: \textrm{capacité thermique de la chambre de combustion} \\
T_{ext} &: \textrm{température extérieure} \\
\alpha &: \textrm{coefficient de conduction entre la chambre de combustion et le compartiment capteur}
\end{aligned}
\end{aligned}$$



$$\textbf{Modèle de mesure :}$$
$$h(X) = \begin{bmatrix} T_{cap} \end{bmatrix}$$
$$\begin{aligned}
&\begin{aligned}
T_{cap} &: \textrm{température au niveau du compartiment capteur}
\end{aligned}
\end{aligned}$$

'''
   
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
        
        sensorBox = RoundedRectangle(corner_radius=0.1, height=0.5, width=0.5, fill_opacity=0.5).set_color(RED).move_to(outline.get_center()+[0.65, 1.6, 0]).set_stroke(width=2)
        sensorBoxAnnotation = Text("Compartiment capteur").scale(0.4).next_to(sensorBox, RIGHT)
        sensorBoxLine = Line(sensorBox.get_right(), sensorBoxAnnotation)
        
        title = Text("Moteur de fusée").scale(1.5).to_edge(UP)
        self.play(Write(title))
        
        engeGroup = VGroup(outline, background, fuel_pipe, combustion_chamber_line, tuyere_line, fuel_pipe_line, fuel_pipe_annotation, combustion_chamber_annotation, tuyere_annotation, sensorBox, sensorBoxAnnotation, sensorBoxLine)
        engeGroup.shift(DOWN)
        
        # Ajouter annotations et lignes
        self.play(Write(outline), FadeIn(background))
        self.play(Write(fuel_pipe))
        self.play(Write(combustion_chamber_line), Write(tuyere_annotation), Write(fuel_pipe_annotation), Write(combustion_chamber_annotation), Write(tuyere_line), Write(fuel_pipe_line))
        
        self.play(Write(sensorBox), Write(sensorBoxAnnotation), Write(sensorBoxLine))
        

        


        # Taille de l'écran
        screen_height = config.frame_height

        # Position initiale et position hors écran en bas
        start_y = background.get_center()[1]  # Position en haut de l'écran
        end_y = start_y-screen_height / 2 - 1  # Position en dehors de l'écran en bas

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
        

        self.play(FadeOut(engeGroup))
        self.wait(1)
        
        # définir le vecteur d'état
        vecteuretattxt = Text("Vecteur d'état").scale(0.75).next_to(title, DOWN)
        stateVector = MathTex(r"X = \begin{bmatrix} T_{com} \\ T_{cap} \end{bmatrix}").scale(1.2)
        stateVector[0][0].set_color(BLUE)
        stateVectorLegend = MathTex(r"\begin{aligned} T_{com} &: \text{température dans la chambre de combustion}\\ T_{cap} &: \text{température au niveau du compartiment capteur} \end{aligned}").scale(0.8).next_to(stateVector, DOWN)
        
        self.play(Write(vecteuretattxt))
        self.play(Write(stateVector))
        self.play(Write(stateVectorLegend))
        self.wait(2)
        
        # rectangle in left up corner
        rect = Rectangle(height=1.5, width=2.2, fill_opacity=0).set_color(BLUE).to_corner(UL).shift((LEFT+UP)*0.6).set_color(WHITE)
        # sepLine = Line([0,0,0], [0,3,0], color=WHITE).shift(LEFT*2).shift(DOWN*2)
        self.play(FadeOut(vecteuretattxt),
                FadeOut(stateVectorLegend), 
                  stateVector.animate.move_to(rect.get_center()).scale(0.5), 
                  title.animate.shift(RIGHT),
                  run_time=2)
        self.play(Write(rect))
        
        # définir la fonction de mesure
        fonctiondemesuretxt = Text("Fonction de mesure").scale(0.75).next_to(title, DOWN)
        measureFunction = MathTex(r"h(X) = \begin{bmatrix} T_{cap} \end{bmatrix}").scale(1.2)
        measureFunction[0][2].set_color(BLUE)
        
        self.play(Write(fonctiondemesuretxt))
        self.play(Write(measureFunction))
        self.wait(2)
        
        newrect = Rectangle(height=2.5, width=2.3, fill_opacity=0).to_corner(UL).shift((LEFT+UP)*0.6).set_color(WHITE)

        self.play(FadeOut(fonctiondemesuretxt),
                  Transform(rect, newrect),
                  measureFunction.animate.next_to(stateVector, DOWN).scale(0.5),
                    run_time=2)
        
        # vecteur de commande
        vecteurdecommandetxt = Text("Vecteur de commande").scale(0.75).next_to(title, DOWN)
        commandVector = MathTex(r"U = \begin{bmatrix} P \end{bmatrix}").scale(1.2)
        commandVector[0][0].set_color(ORANGE)
        commandVectorLegend = MathTex(r"P : \textrm{la puissance thermique injectée dans la chambre de combustion.}").scale(0.8).next_to(commandVector, DOWN)
        
        self.play(Write(vecteurdecommandetxt))
        self.play(Write(commandVector))
        self.play(Write(commandVectorLegend))
        self.wait(2)
        
        newrect = Rectangle(height=3.2, width=2.3, fill_opacity=0).to_corner(UL).shift((LEFT+UP)*0.6).set_color(WHITE)
        self.play(FadeOut(vecteurdecommandetxt),
                  FadeOut(commandVectorLegend),
                    Transform(rect, newrect),
                    commandVector.animate.next_to(measureFunction, DOWN).scale(0.5),
                        run_time=2)
        
        # Modèle de prédiction
        modelPredictiontxt = Text("Modèle de prédiction").scale(0.75).next_to(title, DOWN)
        self.play(Write(modelPredictiontxt))
        
        # rectangle pour anglober la système
        sysrect = Rectangle(height=2.5, width=10, fill_opacity=0).shift(DOWN+RIGHT).set_stroke(width=2)
        
        parroiesChambreCom = Rectangle(height=1.5, width=3, fill_opacity=0.1).move_to(sysrect.get_center()+LEFT*3)
        parroiesChambreComTxt = VGroup(
            Text("parroies chambre"),
            Text("de combustion")
        ).arrange(DOWN).scale(0.5).move_to(parroiesChambreCom).set_color(BLUE)
        compaCap = Rectangle(height=1.5, width=3, fill_opacity=0.1).move_to(sysrect.get_center()+RIGHT*3)
        compaCapTxt = VGroup(
            Text("compartiment"),
            Text("capteur")
        ).arrange(DOWN).scale(0.5).move_to(compaCap).set_color(BLUE)
        
        combArrow = Arrow(parroiesChambreCom.get_left()+LEFT*2, parroiesChambreCom.get_left())
        combTxt = Text("combustion").next_to(combArrow, UP).scale(0.5).shift(LEFT).set_color(ORANGE)
        coolingArrow = Arrow(parroiesChambreCom.get_bottom(), parroiesChambreCom.get_bottom()+DOWN*2)
        coolingTxt = Text("refroidissement").next_to(coolingArrow, RIGHT).scale(0.5).shift(LEFT)
        conductionArrow = Arrow(parroiesChambreCom.get_right(), compaCap.get_left())
        conductionTxt = Text("conduction").next_to(conductionArrow, UP).scale(0.5)
        rayonnementArrow = Arrow(compaCap.get_bottom(), compaCap.get_bottom()+DOWN*2)
        rayonnementTxt = Text("rayonnement").next_to(rayonnementArrow,RIGHT).scale(0.5).shift(LEFT)
        
        # self.add(rect)
        # self.add(parroiesChambreCom)
        # self.add(compaCap)
        # self.add(parroiesChambreComTxt)
        # self.add(compaCapTxt)
        # self.add(combArrow)
        # self.add(combTxt)
        # self.add(coolingArrow)
        # self.add(coolingTxt)
        # self.add(conductionArrow)
        # self.add(conductionTxt)
        # self.add(rayonnementArrow)
        # self.add(rayonnementTxt)
        self.play(Write(rect))
        self.play(Write(parroiesChambreCom), Write(compaCap), Write(parroiesChambreComTxt), Write(compaCapTxt))
        self.wait(1)
        self.play(Write(combArrow), Write(combTxt))
        self.play(Write(coolingArrow), Write(coolingTxt))
        self.play(Write(conductionArrow), Write(conductionTxt))
        self.wait(1)
        self.play(Write(rayonnementArrow), Write(rayonnementTxt))
        self.wait(2)
        
        self.play(
            Transform(combTxt, MathTex(r"P").move_to(combTxt.get_center()).set_color(ORANGE)),
            Transform(parroiesChambreComTxt, MathTex(r"T_{com}").move_to(parroiesChambreComTxt.get_center()).set_color(BLUE)),
            # Transform(coolingTxt, MathTex(r"\alpha(T_{com}-T_{cap})").scale(0.8).move_to(coolingTxt.get_center())),
            # Transform(conductionTxt, MathTex(r"\beta(T_{com}-T_{cap})").scale(0.8).move_to(conductionTxt.get_center())),
            Transform(compaCapTxt, MathTex(r"T_{cap}").move_to(compaCapTxt.get_center()).set_color(BLUE)),
            # Transform(rayonnementTxt, MathTex(r"\gamma(T_{cap}-T_{ext})").scale(0.8).move_to(rayonnementTxt.get_center()))
                )
        self.wait(2)
        self.play(
            Transform(coolingTxt, MathTex(r"\alpha(T_{com}-T_{cryo})").scale(0.8).move_to(coolingTxt.get_center())),
            Transform(conductionTxt, MathTex(r"\beta(T_{com}-T_{cap})").scale(0.8).move_to(conductionTxt.get_center())),
            Transform(rayonnementTxt, MathTex(r"\gamma(T_{cap}-T_{ext})").scale(0.8).move_to(rayonnementTxt.get_center()))
        )
        
        self.wait(2)
        
        self.play(FadeOut(VGroup(
            rect,
            parroiesChambreCom,
            compaCap,
            parroiesChambreComTxt,
            compaCapTxt,
            combArrow,
            combTxt,
            coolingArrow,
            coolingTxt,
            conductionArrow,
            conductionTxt,
            rayonnementArrow,
            rayonnementTxt))
        )
        
        # fonction f(X,U)
        fxuTxt = MathTex(r"f(X,U)").scale(0.8)
        fxuTxt[0][2].set_color(BLUE)
        fxuTxt[0][4].set_color(ORANGE)
        functiontxt = MathTex(r" = \begin{bmatrix} T_{com} + \Delta t*\frac{P-\alpha(T_{com}-T_{cap})-\beta(T_{com}-T_{cap})}{C_{com}} \\[10pt] T_{cap} + \Delta t * \frac{\beta(T_{com}-T_{cap})-\gamma(T_{cap}-T_{ext})}{C_{cap}} \end{bmatrix}").scale(0.8)
        functiontxtGroup = VGroup(fxuTxt, functiontxt).arrange()
        legend = MathTex(r"\begin{aligned} \Delta t &: \textrm{pas de temps} \\ C_{com} &: \textrm{capacité thermique de la chambre de combustion} \\ T_{ext} &: \textrm{température extérieure} \\ \alpha &: \textrm{coefficient de conduction entre la chambre de combustion et les ergols cryogéniques} \\ \beta &: \textrm{coefficient de conduction entre la chambre de combustion et le compartiment capteur} \\ \gamma &: \textrm{coefficient de conduction entre le compartiment capteur et l'extérieur} \end{aligned}").scale(0.5).next_to(functiontxtGroup, DOWN*1.5)
        self.play(Write(functiontxtGroup))
        self.play(Write(legend))
        
        self.wait(2)
        
        newrect = Rectangle(height=3.5, width=2.3, fill_opacity=0).to_corner(UL).shift((LEFT+UP)*0.6).set_color(WHITE)
        self.play(
            FadeOut(functiontxt),
            FadeOut(legend),
            fxuTxt.animate.next_to(commandVector, DOWN).scale(0.8),
            Transform(rect, newrect)
        )
        
        
        
if __name__ == "__main__":
    # Export en MP4
    config.format = "mp4"
    Engine().render()  # Rend en vidéo MP4
    
    # # Export en GIF
    # config.format = "gif"
    # Engine().render()  # Rend en GIF
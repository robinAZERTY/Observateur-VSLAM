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

time = [0.0,1.0101010101010102,2.0202020202020203,3.0303030303030303,4.040404040404041,5.050505050505051,6.0606060606060606,7.070707070707071,8.080808080808081,9.090909090909092,10.101010101010102,11.111111111111112,12.121212121212121,13.131313131313131,14.141414141414142,15.151515151515152,16.161616161616163,17.171717171717173,18.181818181818183,19.191919191919194,20.202020202020204,21.212121212121215,22.222222222222225,23.232323232323235,24.242424242424242,25.252525252525253,26.262626262626263,27.272727272727273,28.282828282828284,29.292929292929294,30.303030303030305,31.313131313131315,32.323232323232325,33.333333333333336,34.343434343434346,35.35353535353536,36.36363636363637,37.37373737373738,38.38383838383839,39.3939393939394,40.40404040404041,41.41414141414142,42.42424242424243,43.43434343434344,44.44444444444445,45.45454545454546,46.46464646464647,47.47474747474748,48.484848484848484,49.494949494949495,50.505050505050505,51.515151515151516,52.525252525252526,53.535353535353536,54.54545454545455,55.55555555555556,56.56565656565657,57.57575757575758,58.58585858585859,59.5959595959596,60.60606060606061,61.61616161616162,62.62626262626263,63.63636363636364,64.64646464646465,65.65656565656566,66.66666666666667,67.67676767676768,68.68686868686869,69.6969696969697,70.70707070707071,71.71717171717172,72.72727272727273,73.73737373737374,74.74747474747475,75.75757575757576,76.76767676767678,77.77777777777779,78.7878787878788,79.7979797979798,80.80808080808082,81.81818181818183,82.82828282828284,83.83838383838385,84.84848484848486,85.85858585858587,86.86868686868688,87.87878787878789,88.8888888888889,89.89898989898991,90.90909090909092,91.91919191919193,92.92929292929294,93.93939393939395,94.94949494949496,95.95959595959597,96.96969696969697,97.97979797979798,98.98989898989899,100.0]
P = [0.0,52.63157894736842,105.26315789473684,157.89473684210526,210.52631578947367,263.1578947368421,315.7894736842105,368.4210526315789,421.05263157894734,473.6842105263158,526.3157894736842,578.9473684210526,631.578947368421,684.2105263157895,736.8421052631578,789.4736842105262,842.1052631578947,894.7368421052631,947.3684210526316,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0,1000.0]
TrueTcom = [-196.0,-189.37173893572074,-177.88295658104337,-162.0615692528338,-141.70369108974404,-118.29842992063234,-91.1618342284684,-60.72262927422174,-26.74365189412496,11.57860848671691,53.772467767851985,99.03686463071284,147.5070757754128,198.50858265186633,251.421783766554,305.9256881924349,363.0058350333887,421.9226298829588,482.7738125155362,545.2098547668278,603.6649095615268,658.8304688233269,711.5083311774165,761.519797773185,809.1590601359774,853.9174929294564,896.0978128714764,936.1484957050826,973.878574179,1008.7198500067396,1042.1493981865256,1073.944088957647,1103.730420913893,1132.3265865386545,1158.8064680300783,1184.02616920761,1208.10587087605,1230.1042641076526,1249.9722198857264,1268.1086666786136,1284.73207765057,1300.090301953397,1314.0058237479145,1326.042724302784,1336.7870169561234,1347.0819426937394,1356.8262141234843,1365.5547142289788,1373.77625254533,1381.0960553974064,1388.1415071974222,1393.8989671133638,1399.7992341224076,1405.559401270992,1410.9114817058687,1416.0954729321425,1421.2550700777979,1426.027374966902,1430.5711880741153,1436.0093544334923,1440.6554060532583,1444.5628254324456,1448.233407665237,1452.5380787369404,1456.4782311992474,1461.1945406907937,1465.6979282431596,1470.0817133142955,1473.4956737747893,1477.0193863873376,1479.9101814459827,1482.3420177188164,1484.583033628241,1487.061954520889,1489.270334128977,1491.5120125977398,1493.8945283852845,1496.9001993328436,1500.1044235612553,1504.0408162659546,1507.2043242028944,1510.7970381131158,1514.9239730571248,1518.542821660621,1522.4848449829815,1526.3434893746555,1530.1263349843246,1533.5068986575325,1535.8651365847184,1538.0502432258647,1540.0471242332455,1541.9010490041169,1543.7929799511003,1545.852718107786,1547.9658378965207,1550.5626508334735,1552.4554781360803,1553.812795264498,1554.0606623406934,1554.3994942852062]
measurments = [0.0,-9.873958947325331,-15.63573491538931,-8.238972473508472,-9.362373741130716,1.7873399709374782,-2.7748907904488824,7.668468090346956,3.2063199560489473,12.772455613836154,19.900199745369594,21.91792215248808,44.263353062236156,42.43329850861104,55.919744005924684,68.60680662762421,64.3762209024976,76.08417662639297,93.74354638194298,99.50391671228626,104.96122401382897,118.98999946930913,126.12619249471601,133.8507381768187,148.4810369453791,157.4542698075062,163.35372601100747,171.77744883354995,175.45020564431422,177.3342125860278,185.8677719801849,199.40436275782963,198.2951476298167,199.42895057339865,206.9671064221647,210.24154011365886,214.3766139620821,218.74607097052836,220.6553224351803,229.42532913733578,224.61166413947157,229.68529611657718,232.5669404679543,232.59664099262642,241.84698330078106,248.04142098230528,239.65832618020727,237.73059741821547,250.92581953091332,250.4867264020689,250.52993445354753,247.0379039421193,249.8447759561681,245.31089088295403,250.22237773885595,245.3973551589428,258.853076520265,249.70093215807418,258.92090321408534,258.4775205559287,254.24828019303175,252.07968665832198,257.7691905527124,250.7289915035825,257.44751052487965,260.58643129196145,261.40632424406107,261.1270746558787,263.56290594036295,259.7783135227939,264.7829363172973,264.17321334723204,262.36798608349477,270.0860434255671,269.3148662941507,266.20396872654345,269.1900219502756,264.8101572873951,263.234569219427,266.42264589582993,266.90554796528795,271.15677772832424,270.0020624124311,278.0422879018623,261.2051131585911,261.85736832576686,282.4982574600524,273.26115729907974,271.04226060607044,267.83676313738647,277.9797239162,276.0074388133196,271.88501054646724,279.9497841926567,277.14714832771824,276.9583017851704,283.16589847021885,272.6102188019703,282.35492202986416,269.7567141676745]
EkfTcom = [-193.5826204835657,-188.80772282836554,-177.0346964068586,-160.63442661692866,-139.93202309717262,-115.13275384057998,-86.57332751575257,-54.46423978257621,-19.010970142998033,19.613875436908216,61.2904114088019,105.88518954203623,153.23522416482567,203.18845188105365,255.58461823678107,310.25548428495694,367.03569791542805,425.8029529419927,486.4354954216,548.8229369345291,607.5402700932926,662.796913223732,714.7985303441817,763.7568276687167,809.8674508097835,853.315608529648,894.2586819277371,932.8422700294544,969.2100303133143,1003.491432743071,1035.7891318645711,1066.2262870603588,1094.9202924988797,1121.9702145544074,1147.4825336417107,1171.5373106004492,1194.221191729036,1215.6208022763892,1235.794609739894,1254.78632815184,1272.641458183042,1289.4086726087853,1305.1408248280795,1319.8847303009732,1333.6716292148776,1346.5395295253652,1358.5469875300541,1369.7538556631544,1380.2055245617491,1389.9518095003011,1399.0314976041293,1407.492300327544,1415.3576273277206,1422.6754991383696,1429.4929239212458,1435.8471919822605,1441.7756821211956,1447.3170153062874,1452.499107405838,1457.3482125185192,1461.9156199510182,1466.217530802055,1470.2579553501262,1474.0484825912351,1477.623813016896,1481.0005602249535,1484.215538738441,1487.286541664666,1490.2257649641347,1493.0220548384264,1495.6827904545512,1498.20349975509,1500.5799775260198,1502.8148704379146,1504.9235001251109,1506.9124453895392,1508.7921363431212,1510.576348346579,1512.2909047887917,1513.954056994627,1515.5931857888288,1517.2007697040333,1518.7864531907026,1520.3679568097,1521.9395302761268,1523.5075639262016,1525.072528482192,1526.6329405574634,1528.1787951069948,1529.6826261576232,1531.1330052581864,1532.5245474878095,1533.855446372556,1535.1296677873306,1536.3561402146292,1537.542243138323,1538.7047882316213,1539.8341302600936,1540.9158682335033,1541.9208672390102]
   
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
        rayonnementTxt = Text("conduction").next_to(rayonnementArrow,RIGHT).scale(0.5).shift(LEFT)
        
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
        self.play(Write(sysrect))
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
            sysrect,
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
        functiontxt = MathTex(r" = \begin{bmatrix} T_{com} + \Delta t*\frac{P-\alpha(T_{com}-T_{cryo})-\beta(T_{com}-T_{cap})}{C_{com}} \\[10pt] T_{cap} + \Delta t * \frac{\beta(T_{com}-T_{cap})-\gamma(T_{cap}-T_{ext})}{C_{cap}} \end{bmatrix}").scale(0.8)
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
        
        # ajoute un graph vide avec un label pour l'axe du temps

# Créer les axes
        axes = Axes(
            x_range=[0, max(time) + 1, 10],  # Étendue des axes x (temps)
            y_range=[-200, max(TrueTcom) + 50, 300],  # Étendue des axes y (P et TrueTcom)
            x_length=6,
            y_length=4,
        ).shift(DOWN*1.5)
        axes_labels = axes.get_axis_labels(x_label="Time (s)", y_label="").shift(0.5 * DOWN)

        # Tracer le graphique initial (P)
        graph_P = axes.plot_line_graph(
            x_values=time,
            y_values=P,
            line_color=ORANGE,
            add_vertex_dots=False,  # Pas de points
        )
        graph_PLab = MathTex(r"P").next_to(graph_P, UP).set_color(ORANGE)

        # Tracer le graphique final (TrueTcom)
        graph_TrueTcom = axes.plot_line_graph(
            x_values=time,
            y_values=TrueTcom,
            line_color=WHITE,
            add_vertex_dots=False,  # Pas de points
        )
        graph_TrueTcomLab = Text("vraie température").scale(0.5).next_to(graph_TrueTcom, UP)

        # Ajouter les axes et le graphique initial à la scène
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(graph_P), Write(graph_PLab))
        self.wait(2)

        # Transformer le graphique P en TrueTcom
        self.play(FadeOut(graph_P), FadeIn(graph_TrueTcom), FadeOut(graph_PLab), FadeIn(graph_TrueTcomLab))
        self.wait(2)    
        
        graph_measurments = axes.plot_line_graph(
            x_values=time,
            y_values=measurments,
            line_color=RED,
            add_vertex_dots=False,  # Pas de points
        )
        graph_measurmentsLab = Text("mesures").scale(0.75).next_to(graph_measurments, UP).set_color(RED)  
        
        self.play(Create(graph_measurments), Write(graph_measurmentsLab)) 
        self.wait(2)
        
        graph_ekf = axes.plot_line_graph(
            x_values=time,
            y_values=EkfTcom,
            line_color=BLUE,
            add_vertex_dots=False,  # Pas de points
            stroke_width=6
        )
        
        graph_ekfLab = Text("estimation EKF").scale(0.5).next_to(graph_ekf, UP).shift(DOWN+RIGHT*2).set_color(BLUE)
        self.play(Create(graph_ekf), Write(graph_ekfLab))
        self.wait(2)        
        
        
if __name__ == "__main__":
    # Export en MP4
    config.format = "mp4"
    Engine().render()  # Rend en vidéo MP4
    
    # # Export en GIF
    # config.format = "gif"
    # Engine().render()  # Rend en GIF
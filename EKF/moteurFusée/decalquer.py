
import cv2
import numpy as np

# Liste pour stocker les points
points = []

# Fonction pour gérer les clics de souris
def mouse_callback(event, x, y, flags, param):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:  # Clic gauche pour ajouter un point
        points.append((x, y))
    elif event == cv2.EVENT_RBUTTONDOWN:  # Clic droit pour terminer
        if len(points) > 2:
            save_points_to_file("polygon_points.txt", points)
            print("Points sauvegardés dans 'polygon_points.txt'")
        else:
            print("Pas assez de points pour former un polygone !")

# Fonction pour enregistrer les points dans un fichier .txt
def save_points_to_file(filename, points):
    # centrer et normaliser les points
    points = np.array(points)
    #reverse y
    points[:,1] = -points[:,1]
    points = points - np.mean(points, axis=0)
    points = points / np.max(np.abs(points))
    #add a 3 dimension to each point (z=0)
    points = np.hstack((points, np.zeros((len(points), 1))))

    
    with open(filename, "w") as file:
        file.write("# Points du polygone\n[\n")
        for point in points:
            file.write(f"[{point[0]},{point[1]},{point[2]}],\n")
        file.write("]")

# Charger une image pour décalquer
# C:\Users\robin\Desktop\Observateur-VSLAM\EKF\moteurFusée\media\images\j9w0e7slomj31.png
image_path = 'image.png'  # Remplacez par le chemin de votre image
image = cv2.imread(image_path)
if image is None:
    print(f"Impossible de charger l'image : {image_path}")
    exit()

# Redimensionner si nécessaire
# image = cv2.resize(image, (int(image.shape), int(900*1.5)))

# Initialiser la fenêtre OpenCV
cv2.namedWindow("Polygon Drawer")
cv2.setMouseCallback("Polygon Drawer", mouse_callback)

while True:
    # Copie de l'image de base
    temp_image = image.copy()

    # Dessiner les lignes entre les points
    for i in range(1, len(points)):
        cv2.line(temp_image, points[i - 1], points[i], (0, 255, 0), 2)

    # Si plus de 2 points, dessiner un polygone
    if len(points) > 2:
        cv2.polylines(temp_image, [np.array(points)], isClosed=True, color=(0, 0, 255), thickness=2)

    # Afficher les points
    for point in points:
        cv2.circle(temp_image, point, 5, (255, 0, 0), -1)

    # Afficher l'image
    cv2.imshow("Polygon Drawer", temp_image)

    # Quitter avec la touche 'q'
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()

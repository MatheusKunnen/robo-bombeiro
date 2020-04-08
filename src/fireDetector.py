#####################################################
#   @autores:                                        #
#           - Jhonny Kristyan Vaz-Tostes de Assis   #
#           - Matheus Kunnen Ledesma                #
#           - Patricia Abe Turato                   #
#####################################################
import cv2 
import numpy as np

class FireDetector:
    
    kernel = np.ones((5,5),np.uint8) # Matriz para GaussianBlur

    def __init__(self):
        self.lower_color = np.array([46, 141, 0])
        self.upper_color = np.array([95, 255, 133])
        self.initCapture()

    def initCapture(self):
        # Inicia captura de camera
        self.cap = cv2.VideoCapture(0)
        # Obtem tamanho da imagem   
        self.frame_w = self.cap.get(3) 
        self.frame_h = self.cap.get(4)

    # Atualiza frame com uma captura atualizada
    def updateFrame(self):
        _, self.frame = self.cap.read()

    # Aplica a mascara de cor (e outros processos) no frame atual para detetar o fogo
    def processFrame(self):
        # Converte fram BGR para HSV 
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Remove ruido da imagem
        hsv = cv2.GaussianBlur(hsv, self.kernel, 0)

        # Filtra cor definida
        self.mask = cv2.inRange(hsv, self.lower_color, self.upper_color)
        
        # Melhora as bordas da mascara e elimina ruido da mascara
        self.mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        self.mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    # Calcula posicao do contorno com maior area a partir do Frame atual
    def updateContour(self):
        pass
import cv2
import numpy as np
from humanMannager import HumanMannager 

class VideoAnalyzer:
    def __init__(self):
        self.cap = None
        self.fgbg = cv2.createBackgroundSubtractorMOG2()
        self.kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        self.estado = 'No se identifica movimiento'
        self.color = (0,0,255)
        self.hm = HumanMannager()
    
    def captureVideo(self):
        self.cap = cv2.VideoCapture('tmpvideo/pasillo_Trim_1.mp4')

    def applySubtraction(self, frame, gray):
        # get area points
        pts = np.array([[330, 400], [125, 710], [815, 710], [600, 400]], np.int32)
        # dibujar el rectangulo de interés
        cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

        # imagen auxiliar para el rectangulo de interés
        imgAux = np.zeros(shape=(frame.shape[:2]), dtype=np.uint8)
        imgAux = cv2.drawContours(imgAux, [pts], -1, (255), -1)
        image_area = cv2.bitwise_and(gray, gray, mask=imgAux)

        fgmask = self.fgbg.apply(image_area)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, self.kernel)
        fgmask = cv2.dilate(fgmask, self.kernel, iterations=1)
        return fgmask

    def createHeader(self, frame):
        # create header
        cv2.rectangle(frame, (0,0), (frame.shape[1],40), (0,0,0), 1)
        color = (0,255,0)
        self.estado = 'Estado: No se identifica movimiento'        

    def printContours(self, frame, fgmask):
        cnts = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        for cnt in cnts:
            if cv2.contourArea(cnt) < 700:
                continue
            # get rectangle that contains the contour
            (x, y, w, h) = cv2.boundingRect(cnt)
            # draw rectangle
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # show text state
            self.estado = 'Se identifica movimiento con #' + str(len(self.hm.activeHumans)) 
            self.color = (0,0,255)
            # add human
            humanID = self.hm.addHuman(x, y)
            # show human id
            cv2.putText(frame, str(humanID), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        # remove inactive humans
        self.hm.cleanHumans()
        

    def printFrame(self, frame, fgmask):
        # show text state
        cv2.putText(frame, self.estado, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, self.color, 2)
        # show frames
        cv2.imshow('fgmask', fgmask)
        cv2.imshow('frame', frame)
    
    def analyse(self):
        self.captureVideo()

        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            
            # reduce to half the size and convert to gray
            frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # create header
            self.createHeader(frame)

            # apply background subtraction
            fgmask = self.applySubtraction(frame, gray)

            # find contours
            self.printContours(frame, fgmask)

            # print frame
            self.printFrame(frame, fgmask)

            if cv2.waitKey(700) & 0xFF == ord('q'):
                break

import cv2
import numpy as np

# obtener el video
cap = cv2.VideoCapture('tmpvideo/pasillo.mp4')

# segmentador de fondo
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

# recorrer los frames
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # reducir a la mitad del tamaño
    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    # convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # crear encabezado
    cv2.rectangle(frame, (0,0), (frame.shape[1],40), (0,0,0), 1)
    color = (0,255,0)
    texto = 'Estado: No se identifica movimiento'

    # indicar los cuatro puntos del rectangulo de interés
    pts = np.array([[330, 400], [125, 710], [815, 710], [600, 400]], np.int32)
    # dibujar el rectangulo de interés
    cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

    # imagen auxiliar para el rectangulo de interés
    imgAux = np.zeros(shape=(frame.shape[:2]), dtype=np.uint8)
    imgAux = cv2.drawContours(imgAux, [pts], -1, (255), -1)
    image_area = cv2.bitwise_and(gray, gray, mask=imgAux)

    # segmentar el fondo
    fgmask = fgbg.apply(image_area)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    fgmask = cv2.dilate(fgmask, kernel, iterations=2)

    # obtener los contornos de la imagen segmentada
    cnts = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for cnt in cnts:
        if cv2.contourArea(cnt) < 700:
            continue
        
        # obtener el rectangulo que contiene al contorno
        (x, y, w, h) = cv2.boundingRect(cnt)
        # dibujar el rectangulo
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # colocar encabezado con texto
        texto = 'Estado: Se identifica movimiento'
        color = (0,0,255)


    # colocar encabezado con texto
    cv2.putText(frame, texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    # mostrar imagen
    cv2.imshow('frame', frame)
    cv2.imshow('auxiliar', fgmask)

    if cv2.waitKey(70) & 0xFF == ord('q'):
        break
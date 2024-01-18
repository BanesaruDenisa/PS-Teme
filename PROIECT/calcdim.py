import cv2
import numpy as np


import cv2
import numpy as np

def detectare_margini_canny(path_imagine):
    # Citirea imaginii originale
    imagine = cv2.imread(path_imagine)
    cv2.imshow('Imagine Originala', imagine)

    # Convertirea în scala de gri
    gray = cv2.cvtColor(imagine, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Scala de Gri', gray)

    # Aplicarea unui filtru Gaussian pentru netezire
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    cv2.imshow('Imagine Netezită', blurred)

    # Calculul gradienților pe axa X și pe axa Y
    grad_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
    cv2.imshow('Gradient X', cv2.convertScaleAbs(grad_x))
    cv2.imshow('Gradient Y', cv2.convertScaleAbs(grad_y))

    # Calculul magnitudinii și unghiului gradienților
    magnitudine, unghi = cv2.cartToPolar(grad_x, grad_y, angleInDegrees=True)
    cv2.imshow('Magnitudinea Gradientului', cv2.convertScaleAbs(magnitudine))

    # Nu putem vizualiza non-maximum suppression și hysteresis thresholding direct folosind OpenCV
    # Detectarea marginilor folosind Canny
    canny = cv2.Canny(blurred, 100, 200)
    cv2.imshow('Margini Detectate - Canny', canny)

    # Așteptare pentru o apăsare de tastă și închiderea tuturor ferestrelor
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Apelarea funcției
detectare_margini_canny('inima.jpg')



def calculare_dimensiune_rinichi(path_imagine):
    # Citirea și preprocesarea imaginii
    imagine = cv2.imread(path_imagine, 0)
    canny = cv2.Canny(imagine, 100, 200)

    # Găsirea contururilor
    contururi, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Presupunând că rinichiul este cel mai mare contur
    contur_rinichi = max(contururi, key=cv2.contourArea)

    # Găsirea extremităților conturului rinichiului
    stanga = tuple(contur_rinichi[contur_rinichi[:, :, 0].argmin()][0])
    dreapta = tuple(contur_rinichi[contur_rinichi[:, :, 0].argmax()][0])
    sus = tuple(contur_rinichi[contur_rinichi[:, :, 1].argmin()][0])
    jos = tuple(contur_rinichi[contur_rinichi[:, :, 1].argmax()][0])

    # Calcularea dimensiunilor
    latime = np.linalg.norm(np.array(stanga) - np.array(dreapta))
    inaltime = np.linalg.norm(np.array(sus) - np.array(jos))

    return latime, inaltime


latime, inaltime = calculare_dimensiune_rinichi('inima.jpg')
print(f"Latime: {latime}, Inaltime: {inaltime}")



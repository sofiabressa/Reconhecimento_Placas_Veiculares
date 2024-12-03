import cv2
import numpy as np

def preprocessar_imagem(imagem_original):
    # Converter para tons de cinza
    imagem_cinza = cv2.cvtColor(imagem_original, cv2.COLOR_BGR2GRAY)

    # Aplicar filtros para remover ruídos
    imagem_cinza = cv2.bilateralFilter(imagem_cinza, 9, 75, 75)
    #imagem_cinza = cv2.GaussianBlur(imagem_cinza, (5, 5), 0)

    # Aplicar limiarização adaptativa para tornar os caracteres mais destacados
    imagem_limiarizada = cv2.adaptiveThreshold(
        imagem_cinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    return imagem_limiarizada

def processar_contornos(imagem_original, imagem_processada):
    contornos, _ = cv2.findContours(imagem_processada, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    possiveis_placas = []

    for contorno in contornos:
        perimetro = cv2.arcLength(contorno, True)
        aprox = cv2.approxPolyDP(contorno, 0.02 * perimetro, True)
        area = cv2.contourArea(contorno)
        x, y, w, h = cv2.boundingRect(contorno)

        # Verificações de proporção e área
        if h > w or h < (w * 0.2) or area < 10000 or area > 70000:
            continue

        if len(aprox) >= 4 and len(aprox) < 10:
            cv2.drawContours(imagem_original, [aprox], -1, (0, 255, 0), 2)

            # Recortar a imagem da placa
            x, y, w, h = cv2.boundingRect(contorno)
            imagem_recortada = imagem_original[y:y + h, x:x + w]
            imagem_processada = filtrar_placas(imagem_recortada)
            possiveis_placas.append((imagem_recortada, imagem_processada))

    return possiveis_placas

def filtrar_placas(imagem_recortada):
    
    # Converter para tons de cinza e aplicar limiarização
    imagem_cinza = cv2.cvtColor(imagem_recortada, cv2.COLOR_BGR2GRAY)
    _, imagem_limiarizada = cv2.threshold(imagem_cinza, 100, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Aplicar operações morfológicas
    kernel_close = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    imagem_close = cv2.morphologyEx(imagem_limiarizada, cv2.MORPH_CLOSE, kernel_close)

    kernel_open = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    imagem_open = cv2.morphologyEx(imagem_close, cv2.MORPH_OPEN, kernel_open)

    kernel_dilate = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    imagem_dilate = cv2.dilate(imagem_open, kernel_dilate, iterations=1)

    kernel_erode = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    imagem_erode = cv2.erode(imagem_dilate, kernel_erode, iterations=1)

    return imagem_erode

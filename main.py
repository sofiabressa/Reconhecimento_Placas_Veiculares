import os
import cv2
from processar_imagem import preprocessar_imagem, processar_contornos
from ocr import aplicar_ocr
from resultado import exibir_resultado
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

def detectar_placa(imagem_path):
    # Ler a imagem original
    imagem_original = cv2.imread(imagem_path)
    
    # Processar a imagem para aprimorar os contornos e detectar a placa
    imagem_processada = preprocessar_imagem(imagem_original)
    
    # Detectar possíveis contornos que possam ser placas
    possiveis_placas = processar_contornos(imagem_original, imagem_processada)
    
    if len(possiveis_placas) == 0:
        print(f"Nenhuma placa detectada em {imagem_path}")
        return
    
    # Aplicar OCR para ler as placas detectadas
    placa_detectada, placa_recortada, placa_recortada_processada = aplicar_ocr(possiveis_placas)
    
    # Exibir os resultados (imagem original, processada e o texto da placa)
    exibir_resultado(imagem_original, imagem_processada, placa_recortada, placa_recortada_processada, placa_detectada)

def processar_imagens_da_pasta(pasta_imagens):

    lista_imagens = os.listdir(pasta_imagens)
    
    for imagem_file in lista_imagens:
        if imagem_file.lower().endswith(('.jpg', '.jpeg', '.png')):
            imagem_path = os.path.join(pasta_imagens, imagem_file)
            print(f"Processando imagem: {imagem_path}")
            detectar_placa(imagem_path)

if __name__ == "__main__":
    pasta_imagens = "images"
    processar_imagens_da_pasta(pasta_imagens)

import cv2
import pytesseract
import re
from resultado import possibilidades_placas_antigas, possibilidades_placas_novas

# Função para encontrar placas no padrão antigo
def encontrar_placa(string):
    padrao = r'[A-Z]{3}\d{4}'
    placas_encontradas = re.findall(padrao, string)
    return placas_encontradas[0] if placas_encontradas else None

# Função para encontrar placas no padrão Mercosul
def encontrar_placa_mercosul(string):
    padrao = r'[A-Z]{3}[0-9][0-9A-Z][0-9]{2}'
    placas_encontradas = re.findall(padrao, string)
    return placas_encontradas[0] if placas_encontradas else None

# Função para aplicar OCR em uma imagem processada
def executar_ocr(imagem, idioma):
    try:
        config = r'-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --psm 6 --oem 3'
        resultado = pytesseract.image_to_string(imagem, lang=idioma, config=config)
        texto = "".join(filter(str.isalnum, resultado))
        return texto
    except Exception as e:
        print(f"Erro ao executar OCR: {e}")
        return ""

# Função principal para aplicar OCR nas possíveis placas
def aplicar_ocr(possiveis_placas):
    for placa_recortada, placa_recortada_processada in possiveis_placas:
        x, y, w, h = cv2.boundingRect(placa_recortada_processada)
        if h > 120:
            placa_recortada_processada = placa_recortada_processada[30:-10]

        # Executar OCR em português e inglês
        texto_por = executar_ocr(placa_recortada_processada, 'por')
        texto_eng = executar_ocr(placa_recortada_processada, 'eng')

        # Verificar placas no formato mercosul e antigo
        for texto in [texto_por, texto_eng]:
            if not texto:
                continue

            placa_mercosul = encontrar_placa_mercosul(texto)
            if placa_mercosul:
                return placa_mercosul, placa_recortada, placa_recortada_processada

            placa_antiga = encontrar_placa(texto)
            if placa_antiga:
                return placa_antiga, placa_recortada, placa_recortada_processada

        # Gerar possibilidades para caracteres ambíguos
        ultimos_4_caracteres = texto_por[-4:] if texto_por else texto_eng[-4:]
        if not ultimos_4_caracteres:
            continue

        # Possibilidades para placas antigas
        possibilidades = possibilidades_placas_antigas(ultimos_4_caracteres)
        result = "\n".join([texto_por[:3] + p for p in possibilidades])

        # Possibilidades para placas Mercosul
        result += "\nMercosul:\n"
        possibilidades_mercosul = possibilidades_placas_novas(ultimos_4_caracteres)
        result += "\n".join([texto_por[:3] + p for p in possibilidades_mercosul])

        return result, placa_recortada, placa_recortada_processada

    return None, None, None

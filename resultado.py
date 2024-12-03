import matplotlib.pyplot as plt
import cv2

# Dicionário para mapear letras que podem ser confundidas com números
letras_numeros = {
    'I': '1',
    'O': '0',
    'Q': '0',
    'Q': 'O',
    'Z': '2',
    'S': ['5', '9'],
    'G': '6',
    'B': '8',
    'A': '4',
    'E': '8',
    'T': '7',
    'Y': '7',
    'L': '1',
    'U': '0',
    'D': '0',
    'R': '2',
    'P': '0',
    'F': '0',
    'J': '1',
    'K': '1',
    'V': '0',
    'W': '0',
    'X': '0',
    'N': '0',
    'M': '0',
    'H': '0',
    'C': '0',
    'Ç': '0',
    'Á': '0',
    'Â': '0',
    'Ã': '0',
    'À': '0',
}

# Função para exibir os resultados
def exibir_resultado(imagem, imagem_processada, imagem_recortada, imagem_recortada_processada, placa_detectada):
    fig, axs = plt.subplots(2, 2, figsize=(10, 6))

    axs[0, 0].imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
    axs[0, 0].set_title("Imagem Original")
    axs[0, 0].axis('off')

    axs[0, 1].imshow(cv2.cvtColor(imagem_processada, cv2.COLOR_BGR2RGB))
    axs[0, 1].set_title("Imagem Processada")
    axs[0, 1].axis('off')

    axs[1, 0].imshow(cv2.cvtColor(imagem_recortada, cv2.COLOR_BGR2RGB))
    axs[1, 0].set_title("Imagem Recortada")
    axs[1, 0].axis('off')

    axs[1, 1].imshow(cv2.cvtColor(imagem_recortada_processada, cv2.COLOR_BGR2RGB))
    axs[1, 1].set_title("Recorte Processado")
    axs[1, 1].axis('off')

    plt.figtext(0.5, 0.05, f"Placa Detectada: {placa_detectada}", fontsize=12, ha='center')
    plt.tight_layout()
    plt.show()

# Função para substituir letras ambíguas por números
def possibilidades_placas_antigas(ultimos_caracteres: str):
    todas_possibilidades = ['']

    for caractere in reversed(ultimos_caracteres):
        novas_possibilidades = []
        substituicoes = letras_numeros.get(caractere, [caractere])

        # Lista de substituições
        if not isinstance(substituicoes, list):
            substituicoes = [substituicoes]

        # Combinação de possibilidades
        for substituicao in substituicoes:
            for possibilidade in todas_possibilidades:
                novas_possibilidades.append(substituicao + possibilidade)

        todas_possibilidades = novas_possibilidades

    return todas_possibilidades

# Função para gerar possibilidades para placas no formato Mercosul
def possibilidades_placas_novas(value: str):
    def combinar_elementos(lista, prefixo=''):
        if not lista:
            return [prefixo]

        resultado = []
        for item in lista[0]:
            resultado.extend(combinar_elementos(lista[1:], prefixo + item))
        return resultado

    possibilidades = []
    for caractere in value:
        substituicoes = letras_numeros.get(caractere, [caractere])

        # Lista de substituições
        if not isinstance(substituicoes, list):
            substituicoes = [substituicoes]

        possibilidades.append(substituicoes)

    return combinar_elementos(possibilidades)

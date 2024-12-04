# Projeto de Reconhecimento de Placas Veiculares

Este repositório contém o projeto final da disciplina de **Processamento Digital de Imagens**, cujo objetivo é realizar o reconhecimento de placas veiculares brasileiras. O foco do projeto é processar imagens de placas localizadas na parte traseira de carros, garantindo uma melhor visibilidade para o reconhecimento.

## Funcionalidades

O projeto utiliza técnicas de processamento de imagens para localizar e reconhecer os caracteres presentes nas placas. Ele opera especificamente com os dois padrões de placas brasileiras: o padrão antigo (AAA1234) e o padrão Mercosul (AAA1A23).

## Tecnologias Utilizadas

As bibliotecas principais utilizadas no projeto são:

- **Pytesseract**: Biblioteca de OCR (Reconhecimento Óptico de Caracteres) para extrair textos de imagens.
- **OpenCV**: Usada para manipulação e processamento de imagens, como conversão para tons de cinza, detecção de bordas e contornos.
- **Matplotlib**: Utilizada para visualização de resultados, exibindo as imagens originais e processadas lado a lado.

## Principais Funções do Projeto

### 1. `preprocessar_imagem(imagem_original)`
- Converte a imagem original para tons de cinza.
- Remove ruídos aplicando filtros bilaterais.
- Realça os caracteres das placas utilizando limiarização adaptativa.

### 2. `processar_contornos(imagem_original, imagem_processada)`
- Detecta contornos na imagem processada.
- Filtra possíveis placas com base em critérios de proporção e área.
- Recorta e processa imagens para localizar placas com maior precisão.

### 3. `filtrar_placas(imagem_recortada)`
- Aplica limiarização e operações morfológicas (fechamento, abertura, dilatação e erosão) para destacar caracteres e reduzir ruídos.

### 4. `encontrar_placa(string)` e `encontrar_placa_mercosul(string)`
- Localizam e validam caracteres correspondentes aos padrões brasileiro antigo e Mercosul em uma string.

### 5. `executar_ocr(imagem, idioma)`
- Aplica OCR para extrair o texto da placa, suportando idiomas como português e inglês.

### 6. `aplicar_ocr(possiveis_placas)`
- Executa o OCR em todas as placas detectadas e tenta validar os padrões conhecidos.
- Gera variações para caracteres ambíguos e valida placas.

### 7. `exibir_resultado(imagem, imagem_processada, imagem_recortada, imagem_recortada_processada, placa_detectada)`
- Exibe os resultados processados, incluindo a imagem original, processada, recortada e o texto da placa detectada.

### 8. `detectar_placa(imagem_path)`
- Função principal que coordena o processo completo de leitura de uma imagem de entrada, processamento, detecção de placas e exibição dos resultados.

### 9. `processar_imagens_da_pasta(pasta_imagens)`
- Processa todas as imagens em uma pasta, aplicando os métodos acima para detectar e reconhecer placas.

## Estrutura do Projeto
├── images/ # Pasta de imagens de entrada para testes (não esta inclusa nesse repositório) 
├── main.py
├── ocr.py
├── processar_imagem.py
├── resultado.py

## Referências bibliográficas
- BOMFIM, Roberto Espinheira da Costa; LIMA, Rebeca Tourinho; MONTEIRO, Roberto Luiz Souza. Algoritmo de reconhecimento automático de placas de veículos baseado em matlab e tesseract OCR. 2014.
- NETO, Vargas; DE SÁ, Aroldo. Reconhecimento automático de placas veiculares do Mercosul utilizando o Tesseract OCR. 2023.
- ANDRINO JUNIOR, Carlos Alberto; MORAES, Gabriel Lima de. Identificação de placas de veículos. UENP, Salto Grande, Ribeirão do Sul, Brazil. Disponível em: https://github.com/Gabriellimmaa/reconhecimento-e-leitura-placa-carro-ptBR.
- RAJPUT, Hitesh; SOM, Tanmoy; KAR, Soumitra. An automated vehicle license plate recognition system. Computer, v. 48, n. 8, p. 56-61, 2015
GONZALEZ, Rafael C.; WOODS, Richard E. Processamento digital de imagem. Pearson, ISBN-10: 8576054019, v. 10, p. 11-27, 2010.

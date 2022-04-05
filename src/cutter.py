# Importa as bibliotecas
import cv2, os, glob # OpenCV, OS, Glob 

files = glob.glob('src/handled_data/processed_CAPTCHA/*') # Cria uma lista com os arquivos (imagens) na pasta de origem

for file in files:
    image = cv2.imread(file) # Abre a imagem em uma variavel com o OpenCV
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) # Coverte a imagem de RGB para escala cinza
    
    # Converte a imagem pra preto e branco invertendo a original
    _, new_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV)

    # Encontra os contornos da letras
    contours, _ = cv2.findContours(new_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    letters_area = [] # Prepara uma lista para receber os dados das letras

    # Fitrar os contornos das letras
    for contour in contours:
        (x, y, wid, hei) = cv2.boundingRect(contour) # Cria um retangulo sobre a possivel letra
        area = cv2.contourArea(contour) # Atribui a area do contorno (possivel letra) a uma variavel
        if area > 115: # Caso a area do contorno seja maior que o tamanho indicado
            letters_area.append((x, y, wid, hei)) # Ele é considerando uma letra e é adicionado a lista

    # Se a imagem possuir mais de 5 letras significa que houve algum erro (nesse caso) e a imagem é descartada
    if len(letters_area) != 5:
        continue

    # Converte a imagem em RGB novamente
    final_image = cv2.merge([image] * 3)

    # Desenha os contornos e separa as letras em arquivos diferentes
    i = 0
    for rectan in letters_area:
        x, y, wid, hei = rectan # Abre os valores da entidade da lista
        letter_image = image[y-2:y+hei+2, x-2:x+wid+2] # Cria um contorno 2 pixels maior do que o criado pelo OpenCV por segurança
        i += 1
        name_file = os.path.basename(file).replace(".png", f"letra{i}.png")
        cv2.imwrite(f'src/handled_data/letters/{name_file}.png', letter_image) # Cria a imagem com a letra cortada
        cv2.rectangle(final_image, (x-2, y-2), (x+wid+2, y+hei+2), (0, 0, 255), 1) # Desenha um retagulo vermelho onde foi feito o corte na imagem original
    
    name_file = os.path.basename(file)
    cv2.imwrite(f"src/handled_data/identified/{name_file}", final_image) # Salva novamente a imagem original
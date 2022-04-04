# from keras.models import load_model
# from helpers import resize_to_fit
# from imutils import paths
# import numpy as np
# import cv2, pickle, os
# from CAPTCHA_processing import image_processing

# def solve_CAPTCHA():
#     # Importar modelo e o LabelBinarizer
#     with open("model/label_model.dat", "rb") as translate_file: 
#         lb = pickle.load(translate_file)
    
#     model = load_model("model/trained_model.hdf5")

#     # Usando o modelo para resolver o CAPTCHA

#     # Ler os arquivos da pasta toSolve e
#         # Tratar a imagem
#     image_processing("../toSolve", destiny_folder="../toSolve")
#         # Identificar letras
#     files = list(paths.list_images("../toSolve")) # Cria uma lista com os arquivos (imagens) na pasta de origem

#     for file in files:
#         image = cv2.imread(file) # Abre a imagem em uma variavel com o OpenCV
#         image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) # Coverte a imagem de RGB para escala cinza
        
#         # Converte a imagem pra preto e branco invertendo a original
#         _, new_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV)

#         # Encontra os contornos da letras
#         contours, _ = cv2.findContours(new_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#         letters_area = [] # Prepara uma lista para receber os dados das letras

#         # Fitrar os contornos das letras
#         for contour in contours:
#             (x, y, wid, hei) = cv2.boundingRect(contour) # Cria um retangulo sobre a possivel letra
#             area = cv2.contourArea(contour) # Atribui a area do contorno (possivel letra) a uma variavel
#             if area > 115: # Caso a area do contorno seja maior que o tamanho indicado
#                 letters_area.append((x, y, wid, hei)) # Ele é considerando uma letra e é adicionado a lista

#         letters_area = sorted(letters_area, key=lambda x: x[0]) # Coloca as letras em ordem

#         prediction = []

#         # Desenha os contornos e separa as letras em arquivos diferentes
#         i = 0
#         for rectan in letters_area:
#             x, y, wid, hei = rectan # Abre os valores da entidade da lista
#             letter_image = image[y-2:y+hei+2, x-2:x+wid+2] # Cria um contorno 2 pixels maior do que o criado pelo OpenCV por segurança
            
#             # Ajustar as letras para o modelo
#             letter_image = resize_to_fit(letter_image, 20, 20)
#             letter_image = np.expand_dims(letter_image, axis=2)
#             letter_image = np.expand_dims(letter_image, axis=0)

#             # Aplicar o modelo nas letras
#             predict_letter = model.predict(letter_image)
#             predict_letter = lb.inverse_transform(predict_letter)[0] # Transformar resultado
#             prediction.append(predict_letter)                        # Adicionar resultado à lista

#         predict_text = "".join(prediction) # Juntar as letras em uma solução

#         return predict_text

# if __name__ == "__main__":
#     checker = "y"
#     while checker == "y":
#         solution = solve_CAPTCHA()
#         os.system('cls') or None
#         print(f"===================\n Solution: {solution} \n===================")
#         checker = input("\nDo you want to solve another CAPTCHA? [y/n] \nRemenber! Change de CAPTCHA image in the toSolve directory before rerun. ")
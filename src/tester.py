import pyautogui as ptog
import cv2, os, glob
from PIL import Image

manners = [
    cv2.THRESH_BINARY,
    cv2.THRESH_BINARY_INV,
    cv2.THRESH_TOZERO,
    cv2.THRESH_TOZERO_INV,
    cv2.THRESH_TRUNC,
]

def treatmentChoose():
    img = cv2.imread('C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA\\data\\unprocessed\\screenshot_test.png')
    grayImage = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    i = 0
    for manner in manners:
        _, noiseless_image = cv2.threshold(grayImage, 127, 255, manner or cv2.THRESH_OTSU)
        cv2.imwrite(f'testScripts/processingTests/noiseless_image_{i}.png', noiseless_image)
        i += 1


# def image_Processing(origin_folder, destiny_folder='data\\unprocessed'):
#     files = glob.glob(f'{origin_folder}/*')


if __name__ == "__main__":
    treatmentChoose()

# # Importa as bibliotecas 
# import cv2, os, glob # OpenCV, OS, Glob 
# from PIL import Image # Image de Pillow

# # Cria uma função com o processo
# def image_processing(origin_folder, destiny_folder='src/handled_data/processed_CAPTCHA'):
    
#     files = glob.glob(f"{origin_folder}/*") # Cria uma lista com os arquivos (imagens) na pasta de origem
    
#     for file in files: 
#         image = cv2.imread(file) # Abre a imagem em uma variavel com o OpenCV
#         gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) # Coverte a imagem de RGB para escala cinza

#         # Testa a aplicação dos dois metodos (THRESH_TRUNC ou THRESH_OTSU) para limpar o ruido de fundo da imagem 
#         _, noiseless_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_TRUNC or cv2.THRESH_OTSU) 
#         fname = os.path.basename(file)
#         cv2.imwrite(f'{destiny_folder}/{fname}', noiseless_image) # Depois escreve o resultado na pasta destino
    
#     files = glob.glob(f"{destiny_folder}/*") # Cria novamente uma lista com os arquivos (imagens) na pasta destino
    
#     for file in files: 
#         image = Image.open(file) # Abre a imagem com a biclioteca Pillow
#         image = image.convert("L") # Converte a imagem para escala de cinza
#         image2 = Image.new("L", image.size, 255) # Cria uma nova imagem com o mesmo tamanho da original com fundo branco

#         for x in range(image.size[1]):
#             for y in range(image.size[0]):           # Varre a imagem original pixel a pixel e caso este seja de um tom
#                 pixel_color = image.getpixel((y, x)) # acima do esperado ele é inserido como um pixel preto na nova imagem
#                 if pixel_color < 115:                # caso não ele permanece branco na nova imagem
#                     image2.putpixel((y, x), 0)

#         # Salva a nova imagem na pasta destino (sobrescrevendo a antiga)
#         name_file = os.path.basename(file)
#         image2.save(f'{destiny_folder}/{name_file}')

# if __name__ == "__main__":        # Inicio
#     image_processing('dbCAPTCHA') # Chama a função

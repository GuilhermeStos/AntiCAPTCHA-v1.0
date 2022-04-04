# Importando a biblioteca OpenCV
import cv2
from PIL import Image
from cv2 import imread
from cv2 import hconcat
from cv2 import vconcat

# Criando uma lista com os metodos a serem testados
manners = [
    cv2.THRESH_BINARY,
    cv2.THRESH_BINARY_INV,
    cv2.THRESH_TOZERO,
    cv2.THRESH_TOZERO_INV,
    cv2.THRESH_TRUNC,
]

# Atribuindo um imagem à variavel para teste
image = cv2.imread("C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA v1.0\\data\\unprocessed\\screenshot_test.png")

# Transformando a imagem em escala de cinza
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

i = 0
for manner in manners:
    _, noiseless_image = cv2.threshold(gray_image, 127, 255, manner or cv2.THRESH_OTSU)
    cv2.imwrite("C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA v1.0\\data\\unprocessed\\screenshot.png", noiseless_image)
    image1 = imread("C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA v1.0\\data\\unprocessed\\screenshot.png")
    image_concate = vconcat([image, image1])
    cv2.imwrite("C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA v1.0\\data\\unprocessed\\screenshot.png", image_concate)
    print(i)
    i += 1
    
    
    
    
    # if (i % 2) == 0:
    #     image_concate = vconcat([image, image1])
    #     cv2.imwrite("C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA v1.0\\data\\unprocessed\\screenshot.png", image_concate)
    #     print(i)
    # else:
    #     image_concate = vconcat([image, image1])
    #     cv2.imwrite("C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA v1.0\\data\\unprocessed\\screenshot.png", image_concate)
    #     print(i)
    

# image = Image.open("C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA v1.0\\data\\processed\\screenshot_test.png")

# image.show()
import os
import AntiCAPTCHA
import glob as gb
import cv2 as cv
from PIL import Image

def image_processing(manner, originFolder, destinyFolder):
    """Coleta as imagens e aplica o processamento em todas.

    Args:
        manner (integer): ID da função a ser utilizada.
        originFolder (str): Pasta de origem das imagens.
        destinyFolder (str): Pasta de destino das imagens.
    """
    
    files = gb.glob(f'{originFolder}/*')
    
    for file in files: 
        image = cv.imread(file)
        grayImage = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

        _, noiselessImage = cv.threshold(grayImage, 127, 255, manner or cv.THRESH_OTSU) 
        fileName = os.path.basename(file)
        cv.imwrite(f'{destinyFolder}/{fileName}', noiselessImage)
    
    files = gb.glob(f'{destinyFolder}/*')
    
    for file in files: 
        image = Image.open(file)
        image = image.convert("L")
        image2 = Image.new("L", image.size, 255)

        for x in range(image.size[1]):
            for y in range(image.size[0]):
                pixelColor = image.getpixel((y, x))
                if pixelColor < 115:
                    image2.putpixel((y, x), 0)

        nameFile = os.path.basename(file)
        image2.save(f'{destinyFolder}/{nameFile}')

def begin_processing(manner):
    """Chama as funções iniciais e prepara a interface.

    Args:
        manner (int): ID da função a ser utilizada.
    """

    for i in range(6):
        os.remove(f'C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA v1.0\\data\\screenshot{i}.png')
    
    AntiCAPTCHA.header_setup("TREAT IMAGES")

    src =r'C:\Users\gui19\Documents\Projetos\AntiCAPTCHA v1.0\data\unprocessed\screenshot_test.png' 
    des =r'C:\Users\gui19\Documents\Projetos\AntiCAPTCHA v1.0\data\processed\screenshot_test.png' 
    os.replace(src, des)        
    
    origin =  input("| Pasta de origem das imagens:                       |")
    print(f"\033[A\033[A| {origin}                                      |")

    print("|" + (" " * 52) + "|")
    
    destiny = input("| Pasta de destimo das imagens processadas:          |")
    print(f"\033[A\033[A| {destiny}                                        |")
    
    image_processing(manner, origin, destiny)

    print("|" + ("_" * 52) + "|")

if __name__ == "__main__":
    begin_processing(cv.THRESH_TRUNC)
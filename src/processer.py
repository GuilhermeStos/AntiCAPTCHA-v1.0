import os
import AntiCAPTCHA
import glob as gb
import cv2 as cv
from PIL import Image

def image_processing(manner, originFolder, destinyFolder):
    
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
    AntiCAPTCHA.header_setup("TREAT IMAGES")
              
    origin =  input("| Pasta de origem das imagens:                       |")
    destiny = input("| Pasta de destimo das imagens processadas:          |")
    image_processing(manner, origin, destiny)

if __name__ == "__main__":
    image_processing('dbCAPTCHA')
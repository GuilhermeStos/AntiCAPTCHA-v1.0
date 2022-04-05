import os
import cv2 as cv
import glob as gb
from PIL import Image

def image_processing(originFolder, destinyFolder='C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA v1.0\\data\\unprocessed'):
    
    files = gb.glob(f'{originFolder}/*')
    
    for file in files: 
        image = cv.imread(file)
        grayImage = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

        _, noiseless_image = cv.threshold(grayImage, 127, 255, cv.THRESH_TRUNC or cv.THRESH_OTSU) 
        fname = os.path.basename(file)
        cv.imwrite(f'{destinyFolder}/{fname}', noiseless_image)
    
    files = gb.glob(f"{destinyFolder}/*")
    
    for file in files: 
        image = Image.open(file)
        image = image.convert("L")
        image2 = Image.new("L", image.size, 255)

        for x in range(image.size[1]):
            for y in range(image.size[0]):
                pixel_color = image.getpixel((y, x))
                if pixel_color < 115:
                    image2.putpixel((y, x), 0)

        name_file = os.path.basename(file)
        image2.save(f'{destinyFolder}/{name_file}')

if __name__ == "__main__":
    image_processing('dbCAPTCHA')

import os
import glob
import AntiCAPTCHA
import cv2 as cv
import pyautogui as ptog
from PIL import Image

manners = [
    cv.THRESH_BINARY,
    cv.THRESH_BINARY_INV,
    cv.THRESH_TOZERO,
    cv.THRESH_TOZERO_INV,
    cv.THRESH_TRUNC,
]

def menu_setup():
    print("| Escolha o metodo de Threshold:                     |")
    print("|                                                    |")
    print("| 1 - Binario                                        |")
    print("| 2 - Binario Invertido                              |")
    print("| 3 - Para Zero                                      |")
    print("| 4 - Para Zero Invertido                            |")
    print("| 5 - Truncado                                       |")
    print("|" + ("_" * 52) + "|")
    print(" ")
    return input("| Sua opção: ")

def test_image(grayImage, manner):
    _, noiseless_image = cv.threshold(grayImage, 127, 255, manner or cv.THRESH_OTSU)
    cv.imwrite('testScripts\\processingTests\\noiseless_image.png', noiseless_image)
    img = Image.open('C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA v1.0\\data\\unprocessed\\noiseless_image.png')
    img.show()
    ptog.confirm("Gostaria de testar outra imagem?")

def treatment_choose():
    AntiCAPTCHA.header_setup("TREAT IMAGES")
    option = menu_setup()
    img = cv.imread('C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA\\data\\unprocessed\\screenshot_test.png')
    grayImage = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

    if option == "1":
        test_image(grayImage, cv.THRESH_BINARY)
    if option == "2":
        test_image(grayImage, cv.THRESH_BINARY_INV)
    if option == "3":
        test_image(grayImage, cv.THRESH_TOZERO)
    if option == "4":
        test_image(grayImage, cv.THRESH_TOZERO_INV)
    if option == "5":
        test_image(grayImage, cv.THRESH_TRUNC)

if __name__ == "__main__":
    treatment_choose()
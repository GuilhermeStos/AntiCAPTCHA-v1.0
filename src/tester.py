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

import cv2

# Criando uma lista com os metodos a serem testados
manners = [
    cv2.THRESH_TRUNC,
    cv2.THRESH_BINARY,
    cv2.THRESH_BINARY_INV,
    cv2.THRESH_TOZERO,
    cv2.THRESH_TOZERO_INV
]
def text_images(img, text, i):
    img = cv2.putText(img=img, text=text, org=(0, 25), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(0, 0, 255), thickness=1)
    cv2.imwrite(f"C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA v1.0\\data\\unprocessed\\screenshot{i}.png", img)

# Atribuindo um imagem à variavel para teste
image = cv2.imread("C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA v1.0\\data\\unprocessed\\screenshot_test.png")

# Transformando a imagem em escala de cinza
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

i = 0
for manner in manners:    
    _, noiseless_image = cv2.threshold(gray_image, 127, 255, manner or cv2.THRESH_OTSU)
    img = cv2.cvtColor(noiseless_image, cv2.COLOR_GRAY2RGB)
    
    if manner == 0:
        text_images(img, "Binario", i)
    elif manner == 1:
        text_images(img, "Binario Inv", i)
    elif manner == 2:
        text_images(img, "Truncado", i)
    elif manner == 3:
        text_images(img, "Para Zero", i)
    elif manner == 4:
        text_images(img, "Para Zero Inv", i)
    
    i += 1

text_images(image, "Padrao", 5)


# image = Image.open("C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA v1.0\\data\\processed\\screenshot_test.png")

# image.show()
import AntiCAPTCHA
import processer
import cv2 as cv
from PIL import Image

manners = [
    cv.THRESH_TRUNC,
    cv.THRESH_BINARY,
    cv.THRESH_BINARY_INV,
    cv.THRESH_TOZERO,
    cv.THRESH_TOZERO_INV
]

def menu_setup():
    """Cria a interface do menu.

    Returns:
        str: Opção escolhida pelo usuario.
    """
    
    print("| Escolha o metodo de Threshold:                     |")
    print("|                                                    |")
    print("| 1 - Truncado                                       |")
    print("| 2 - Binario                                        |")
    print("| 3 - Binario Invertido                              |")
    print("| 4 - Para Zero                                      |")
    print("| 5 - Para Zero Invertido                            |")
    print("|" + ("_" * 52) + "|")
    print(" ")
    return input("| Sua opção: ")

def test_image(path='C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA v1.0\\data\\unprocessed\\screenshot_test.png'):
    """Cria uma amostra de imagem com todos os metodos para teste.

    Args:
        path (str, optional): Caminho do arquivo a ser usado como modelo. Defaults to 'C:\Users\gui19\Documents\Projetos\AntiCAPTCHA v1.0\data\unprocessed\screenshot_test.png'.
    """

    def text_image(img, text, i):
        """Cria uma imagem com o modelo aplicado.

        Args:
            img (OpenCV data): Traz a imagem OpenCV armazenada.
            text (str): Texto de identificação da imagem.
            i (int): Valor usado para nomear a imagem.
        """
        img = cv.putText(img=img, text=text, org=(0, 25), fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=1, color=(0, 0, 255), thickness=1)
        cv.imwrite(f'C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA v1.0\\data\\screenshot{i}.png', img)

    def concat_tile(im_list_2d):
        """Agrupa as imagens em uma unica.

        Args:
            im_list_2d (lista de imagens): Traz as imagens a serem colocadas juntas.

        Returns:
            imagem: Imagem concatenada.
        """
        return cv.vconcat([cv.hconcat(im_list_h) for im_list_h in im_list_2d])

    image = cv.imread(fr'{path}')
    grayImage = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

    i = 0
    for manner in manners:    
        _, noiselessImage = cv.threshold(grayImage, 127, 255, manner or cv.THRESH_OTSU)
        img = cv.cvtColor(noiselessImage, cv.COLOR_GRAY2RGB)
        
        if manner == 0:
            text_image(img, "Binario", i)
        elif manner == 1:
            text_image(img, "Binario Inv", i)
        elif manner == 2:
            text_image(img, "Truncado", i)
        elif manner == 3:
            text_image(img, "Para Zero", i)
        elif manner == 4:
            text_image(img, "Para Zero Inv", i)
    
        i += 1

    text_image(image, "Padrao", 5)

    i = 0
    imgs = []
    for i in range(6):
        imgs.append(cv.imread(f'C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA v1.0\\data\\screenshot{i}.png'))

    img = concat_tile([[imgs[5], imgs[0]],
                       [imgs[1], imgs[2]], 
                       [imgs[3], imgs[4]]])
    
    cv.imwrite('C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA v1.0\\data\\processed\\samples.png', img)

    image = Image.open('C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA v1.0\\data\\processed\\samples.png')
    image.show()


def treatment_choose():
    """Chama outras funções de outros scripts com base no input recebido.
    """

    AntiCAPTCHA.header_setup("TREAT IMAGES")
    
    path = input("| Insira o caminho da imagem na maquina:             |")
    print("| Crinando imagem de teste...                        |")

    AntiCAPTCHA.header_setup("TREAT IMAGES")
    test_image(path)
    
    option = menu_setup()

    if option == '1':
        processer.begin_processing(cv.THRESH_TRUNC)
    elif option == '2':
        processer.begin_processing(cv.THRESH_BINARY)
    elif option == '3':
        processer.begin_processing(cv.THRESH_BINARY_INV)
    elif option == '4':
        processer.begin_processing(cv.THRESH_TOZERO)
    elif option == '5':
        processer.begin_processing(cv.THRESH_TOZERO_INV)

if __name__ == "__main__":
    treatment_choose()
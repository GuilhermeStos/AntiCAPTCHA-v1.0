import pyautogui as ptog
import AntiCAPTCHA
from PIL import Image

def get_position(location):
    conf = ptog.confirm(f"Posicione o mouse no canto {location} da imagem desejada e pressione ENTER.")
    
    if conf == "OK":
        mouseX, mouseY = ptog.position()
        return mouseX, mouseY
    else:
        return 

def get_area():
    step = " Passo 1 - Dimensionamento"
    print("|" + step + (" " * (52 - (len(step)))) + "|")

    posX1, posY1 = get_position("superior esquerdo")
    posX2, posY2 = get_position("inferior direito")

    wid = posX2 - posX1
    hei = posY2 - posY1
    return posX1, posY1, wid, hei

def get_screenshot_position():
    x, y, wid, hei = get_area()

    step = " Passo 2 - Captura de teste"
    print("|" + step + (" " * (52 - (len(step)))) + "|")

    img = ptog.screenshot('C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA v1.0\\data\\unprocessed\\screenshot_test.png', region=(x, y, wid, hei))
       
    img = Image.open('C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA v1.0\\data\\unprocessed\\screenshot_test.png')
    img.show()    
    return x, y, wid, hei

def screenshot_database(x, y, wid, hei):
    step = " Passo 3 - Realizar capturas"
    print("|" + step + (" " * (52 - (len(step)))) + "|")

    print(" ")
    step = " Certifiqui-se de que a janela esteja na aberta!!!"
    print("|" + step + (" " * (52 - (len(step)))) + "|")

    step = " Quantos screenshots deseja que sejam realizados?"
    screens = input("|" + step + (" " * (52 - (len(step)))))

    step = "Quantos segundos deseja esperar?"
    delay = input("|" + step + (" " * (52 - (len(step)))))
    
    ptog.alert('Não esqueça de re-abrir a janela que deseja realizar os screenshots, antes de clicar em "OK"')
    for c in range(int(screens)):
        ptog.screenshot(f'C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA v1.0\\data\\unprocessed\\screen{c}.png', region=(x, y, wid, hei))
        ptog.click(x=87, y=51)
        ptog.PAUSE = int(delay)

def create_screen():
    AntiCAPTCHA.header_setup("CAPTURE DATA")
    x, y, wid, hei = get_screenshot_position()
    screenshot_database(x, y, wid, hei)
import pyautogui as ptog
import AntiCAPTCHA
from PIL import Image

def get_position(location):
    """Captura a posição do cursor na tela.

    Args:
        location (str): Posição onde se deve colocar o cursor.

    Returns:
        integer: Retorna os valores X e Y relativos a posição do cursor na tela.
    """
    
    conf = ptog.confirm(f"Posicione o mouse no canto {location} da imagem desejada e pressione ENTER.")
    
    if conf == "OK":
        mouseX, mouseY = ptog.position()
        return mouseX, mouseY
    else:
        AntiCAPTCHA.begin()

def get_area():
    """Calcula as dimensões da região desejada.

    Returns:
        int: Valor de X e Y do canto superior esquerdo, além da largura e altura da região.
    """
    
    step = " Passo 1 - Dimensionamento"
    print("|" + step + (" " * (52 - (len(step)))) + "|")

    posX1, posY1 = get_position("superior esquerdo")
    posX2, posY2 = get_position("inferior direito")

    wid = posX2 - posX1
    hei = posY2 - posY1
    return posX1, posY1, wid, hei

def get_screenshot_position():
    """Captura a tela na região retangular desejada.

    Returns:
        int: Valor de X e Y do canto superior esquerdo, além da largura e altura da região capturada.
    """
    
    x, y, wid, hei = get_area()

    step = " Passo 2 - Captura de teste"
    print("|" + step + (" " * (52 - (len(step)))) + "|")

    img = ptog.screenshot('C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA v1.0\\data\\unprocessed\\screenshot_test.png', region=(x, y, wid, hei))
       
    img = Image.open('C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA v1.0\\data\\unprocessed\\screenshot_test.png')
    img.show()    
    return x, y, wid, hei

def screenshot_database(x, y, wid, hei):
    """Captura um mesmo ponto da tela e atualiza a página o número desejado de vezes (criando um banco de dados bruto).

    Args:
        x (int): Valor X da posição do canto superior esquerdo da área de captura.
        y (int): Valor Y da posição do canto superior esquerdo da área de captura.
        wid (int): Largura da área de captura.
        hei (int): Altura da área de captura.
    """
    
    step = " Passo 3 - Realizar capturas"
    print("|" + step + (" " * (52 - (len(step)))) + "|")
    print("|" + (" " * 52) + "|")

    step = " Certifique-se de que a janela esteja na aberta!!!"
    print("|" + step + (" " * (52 - (len(step)))) + "|")

    screens = input("| Quantos screenshots devem ser realizados? ")
    step = len(str(screens))
    print(f"\033[A| Quantos screenshots devem ser realizados? {screens}" + (" " * (9 - step)) + "|")

    delay = input("| Quantos segundos deseja esperar? ")
    step = len(str(delay))
    print(f"\033[A| Quantos segundos deseja esperar? {delay}" + (" " * (18 - step)) + "|")
    print("|" + ("_" * 52) + "|")

    ptog.alert('Não esqueça de re-abrir a janela que deseja realizar os screenshots, antes de clicar em "OK"')
    for c in range(int(screens)):
        ptog.screenshot(f'C:\\Users\\gui19\\Documents\\Projetos\\AntiCAPTCHA v1.0\\data\\unprocessed\\screen{c}.png', region=(x, y, wid, hei))
        ptog.click(x=87, y=51)
        ptog.PAUSE = int(delay)

def create_screen():
    """Chama as fuções criando a tela realizando os processos.
    """
    
    AntiCAPTCHA.header_setup("CAPTURE DATA")
    x, y, wid, hei = get_screenshot_position()
    screenshot_database(x, y, wid, hei)
    AntiCAPTCHA.begin()

if __name__ == "__main__":
    create_screen()
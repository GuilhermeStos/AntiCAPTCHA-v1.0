import os
import captor
import tester

def menu_setup():
    """Função de criação do menu inicial.

    Returns:
        string: O número da opção escolhida no menu.   
    """
    print("| 1 - Adiquirir imagens para a database              |")
    print("| 2 - Realizar testes de aprimoramento da imagem     |")
    print("| 3 - Treinar modelo para a solução dos CAPTCHAs     |")
    print("| 4 - Aplicar modelo de IA                           |")
    print("|" + ("_" * 52) + "|")
    print(" ")

    return input("| Sua opção: ")

def header_setup(name):
    """Função de criação de cabeçalhos.

    Args:
        name (string): Nome a ser inserido no cabeçalho.
    """
    
    os.system('cls') or None
    os.system('title AntiCAPTCHA')
    os.system('mode con: cols=54 lines=12')
    x = len(name)
    x = 52 - x
    print(" " + ("_" * 52) + " ")
    print("|" + (" " * 52) + "|")
    if (x % 2) == 0:
        x /= 2
        print("|" + (" " * int(x)) + name + (" " * int(x)) + "|")
    else:
        x = (x - 1) / 2 
        print("|" + (" " * int(x)) + name + (" " * int(x) + 1) + "|")
    print("|" + (" " * 52) + "|")

def choose_metod(opt):
    """Chama outras funções de outros scripts com base no input recebido.

    Args:
        opt (string): Valor da opção desejada no menu.
    """
    
    if opt == "1":
        captor.create_screen()
    elif opt == "2":
        tester.treatment_choose()
        pass
    elif opt == "3":
        pass
    elif opt == "4":
        pass

def begin():
    """Inicio do script. Chama as funções de criação do menu inicial.
    """
    
    header_setup("AntiCAPTCHA MENU")
    option = menu_setup()
    choose_metod(option)

if __name__ == "__main__":
    begin()
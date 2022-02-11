 from Xlib import X
import pyautogui
from PIL import ImageGrab

# | Time para começar o codigo

from time import sleep
sleep(3)

# | 1º . Para iniciar o jogo precisa : clicar em qualquer aba da tela e depois dar espaço


def inicio():
    pyautogui.moveTo(263, 773)
    pyautogui.click(button='left', clicks=2)
    pyautogui.press('space')

# | Logica do jogo : Se em posição X,Y tiver pixel de tal cor presione tal tecla

# | 2º . Reconhecendo pixel

    # | Teste de coordenadas
    # print(pyautogui.position())

    # | Testar a cor do dinossauro (obs: resultado Dino (83,83,83) Fundo (247,247,247))
    #screen = ImageGrab.grab()
    #color = screen.getpixel((194, 641))
    # print(color)


fundo_color = (247, 247, 247)
dino_color = (83, 83, 83)


def capture_screen():
    screen = ImageGrab.grab()
    return screen


def detect_color(screen):
    for x in range(288, 574):
        for y in range(343, 654):
            color = screen.getpixel((x, y))
            if color == (83, 83, 83):
                return True


def jump():
    pyautogui.press("up")


inicio()
while True:
    screen = capture_screen()
    if detect_color(screen):
        jump()
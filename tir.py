import pygame
import random



pygame.init()   #1 шаг инициализации Pygame
#нужно создать игровой цикл. это всё что происходит в игре: клики, движение мыши, нажатия клавиш, и т.д.
running = True #2 шаг создать переменную, которая будет определять, будет ли игра продолжаться. в тот момент, когда нужно будет завершить игру мы сделаем её равной False


#создаём переменные экрана. экран создается отдельной командой с указанными размерами
SCREEN_WIDTH = 800  #4 шаг ширина экрана
SCREEN_HEIGHT = 600  #5 шаг высота экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 6 шаг создание экрана

pygame.display.set_caption("My Game") #7 шаг заголовок окна
icon = pygame.image.load("icon.png") #8 шаг загрузка иконки
pygame.display.set_icon(icon) #9 шаг установка иконки

target_image = pygame.image.load("target.png") #10 шаг создание переменной картинки цели
target_width, target_height = 50 #11 шаг размеры ширины и высоты цели

target_x = random.randint(0, SCREEN_WIDTH - target_width) #12 шаг позиция цели по горизонтали (ось x)
target_y = random.randint(0, SCREEN_HEIGHT - target_height) #13 шаг позиция цели по вертикали (ось y)

color = rondom.randint(0, 255), random.randint(0, 225), random.randint(0, 255) #14 шаг цвет цели выходит так же рондомно

#цикл, в котором происходит основная игровая логика
while running:
    pass

pygame.quit() #3 шаг функция завершения игры, закрывать окно с игрой,как тоько завершиться цикл. running = False/
# это основа игры, которую мы сделали в ветке main
# нужно создать 2 ветки. 1 с константами - которые не меняются, 2 с переменными - которые будут происходить в цикле (меняться)


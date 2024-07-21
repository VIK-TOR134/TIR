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
icon = pygame.image.load("img/icon.png") #8 шаг загрузка иконки
pygame.display.set_icon(icon) #9 шаг установка иконки

target_image = pygame.image.load("img/target.png") #10 шаг создание переменной картинки цели
target_width = 50
target_height = 50 #11 шаг размеры ширины и высоты цели

target_x = random.randint(0, SCREEN_WIDTH - target_width) #12 шаг позиция цели по горизонтали (ось x)
target_y = random.randint(0, SCREEN_HEIGHT - target_height) #13 шаг позиция цели по вертикали (ось y)

color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255) #14 шаг цвет цели выходит так же рондомно

#цикл, в котором происходит основная игровая логика
while running:
    screen.fill((color)) #15 шаг заливка игрового окна



    for event in pygame.event.get(): #16 шаг получение событий  в игре
        if event.type == pygame.QUIT: #17 шаг завершение игры при нажатии крестика в верхнем левом углу окна
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: #18 шаг проверка нажатия мыши
            mouse_x, mouse_y = pygame.mouse.get_pos() #19 шаг получение координат мыши
            if mouse_x > target_x and mouse_x < target_x + target_width and mouse_y > target_y and mouse_y < target_y + target_height: #20 шаг проверка нахождения мыши в области цели
                target_x = random.randint(0, SCREEN_WIDTH - target_width) #21 шаг перемещение цели в случайное место
                target_y = random.randint(0, SCREEN_HEIGHT - target_height) #22 шаг перемещение цели в случайное место
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    screen.blit(target_image, (target_x, target_y))  #шаг 23 Рисуем цель на экране
    pygame.display.update()  #шаг 24 Обновляем экран

pygame.quit() #3 шаг функция завершения игры, закрывать окно с игрой,как тоько завершиться цикл. running = False/
# это основа игры, которую мы сделали в ветке main
# нужно создать 2 ветки. 1 с константами - которые не меняются (шаг 4-14), 2 с переменными - которые будут происходить в цикле (меняться)


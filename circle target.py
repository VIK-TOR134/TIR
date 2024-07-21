import pygame
import random
import math  # Добавляем для доступа к математическим функциям

pygame.init()

SKREEN_WIDTH = 800
SKREEN_HEIGHT = 600
SKREEN = pygame.display.set_mode((SKREEN_WIDTH, SKREEN_HEIGHT))
pygame.display.set_caption("Игра ТИР")
icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)
target_image = pygame.image.load("img/target.png")
target_width = 80  # исправил опечатку в слове "width" от "wigth"
target_height = 80

# Параметры для движения по закругленной траектории
circle_center_x = SKREEN_WIDTH // 2
circle_center_y = SKREEN_HEIGHT // 2
radius = 200
angle = 0
speed = 0.00096  # Скорость движения по кругу

color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
running = True  # исправил опечатку в слове "running" от "runing"
while running:
    SKREEN.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                angle = 0  # Сброс угла на начальную позицию

    # Обновление позиции цели для движения по круговой траектории
    target_x = int(circle_center_x + radius * math.cos(angle))
    target_y = int(circle_center_y + radius * math.sin(angle))
    angle += speed

    if angle >= 2 * math.pi:
        angle = 0  # Сброс угла, чтобы избежать увеличения до бесконечности

    SKREEN.blit(target_image, (target_x, target_y))

    pygame.display.update()

pygame.quit()
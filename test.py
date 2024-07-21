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
speed = 0.0027595 # Скорость движения по кругу

color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
running = True  # исправил опечатку в слове "running" от "runing"

# Добавляем счетчики для попыток и попаданий
attempts = 0
hits = 0

# Шрифт для отображения счетчиков
font = pygame.font.Font(None, 36)

while running:
    SKREEN.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            attempts += 1  # Увеличиваем счетчик попыток
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                hits += 1  # Увеличиваем счетчик попаданий
                angle = 0  # Сброс угла на начальную позицию
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Обновление позиции цели для движения по круговой траектории
    target_x = int(circle_center_x + radius * math.cos(angle))
    target_y = int(circle_center_y + radius * math.sin(angle))
    angle += speed

    if angle >= 2 * math.pi:
        angle = 0  # Сброс угла, чтобы избежать увеличения до бесконечности


    SKREEN.blit(target_image, (target_x, target_y))

    # Отображение счетчиков на экране
    score_text = f"{attempts}:{hits}"
    text_surface = font.render(score_text, True, (255, 255, 255))
    SKREEN.blit(text_surface, (10, 10))

    pygame.display.update()

pygame.quit()
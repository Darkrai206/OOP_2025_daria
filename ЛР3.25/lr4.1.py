import pygame
from pygame.draw import *
from math import pi

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))  # Белый фон

def draw_head(surface, x, y, size):
    """Рисуем голову зайца"""
    ellipse(surface, (200, 200, 200), (x, y, size, size*0.8))
    # Глаза
    circle(surface, (0, 0, 0), (x + size*0.3, y + size*0.3), size*0.08)
    circle(surface, (0, 0, 0), (x + size*0.7, y + size*0.3), size*0.08)
    # Нос
    polygon(surface, (255, 100, 100), [
        (x + size*0.5, y + size*0.45),
        (x + size*0.45, y + size*0.55),
        (x + size*0.55, y + size*0.55)
    ])
    # Усы
    line(surface, (0, 0, 0), (x + size*0.45, y + size*0.5), (x + size*0.25, y + size*0.45), 1)
    line(surface, (0, 0, 0), (x + size*0.45, y + size*0.55), (x + size*0.25, y + size*0.55), 1)
    line(surface, (0, 0, 0), (x + size*0.55, y + size*0.5), (x + size*0.75, y + size*0.45), 1)
    line(surface, (0, 0, 0), (x + size*0.55, y + size*0.55), (x + size*0.75, y + size*0.55), 1)

def draw_ears(surface, x, y, size):
    """Рисуем уши зайца"""
    # Левое ухо
    ellipse(surface, (200, 200, 200), (x + size*0.2, y - size*0.7, size*0.3, size*0.9))
    ellipse(surface, (255, 150, 150), (x + size*0.25, y - size*0.6, size*0.2, size*0.7))
    # Правое ухо
    ellipse(surface, (200, 200, 200), (x + size*0.5, y - size*0.7, size*0.3, size*0.9))
    ellipse(surface, (255, 150, 150), (x + size*0.55, y - size*0.6, size*0.2, size*0.7))

def draw_body(surface, x, y, size):
    """Рисуем тело зайца"""
    ellipse(surface, (200, 200, 200), (x - size*0.2, y + size*0.5, size*1.4, size*1.2))

def draw_legs(surface, x, y, size):
    """Рисуем лапы зайца"""
    # Передние лапы
    ellipse(surface, (200, 200, 200), (x + size*0.1, y + size*1.2, size*0.4, size*0.3))
    ellipse(surface, (200, 200, 200), (x + size*0.5, y + size*1.2, size*0.4, size*0.3))
    # Задние лапы
    ellipse(surface, (200, 200, 200), (x - size*0.1, y + size*1.4, size*0.5, size*0.4))
    ellipse(surface, (200, 200, 200), (x + size*0.6, y + size*1.4, size*0.5, size*0.4))

def draw_tail(surface, x, y, size):
    """Рисуем хвост зайца"""
    circle(surface, (200, 200, 200), (x + size*0.8, y + size*1.6), size*0.15)

def draw_hare(surface, x, y, size):
    """Рисуем всего зайца, используя все части"""
    draw_body(surface, x, y, size)
    draw_head(surface, x, y, size)
    draw_ears(surface, x, y, size)
    draw_legs(surface, x, y, size)
    draw_tail(surface, x, y, size)

# Рисуем зайца в центре экрана
draw_hare(screen, 150, 100, 100)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
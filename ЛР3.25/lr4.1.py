import pygame
from pygame.draw import *
from math import pi

pygame.init()

# Конфигурация экрана
SCREEN_CONFIG = {
    'width': 400,
    'height': 400,
    'bg_color': (255, 255, 255),
    'fps': 30
}

# Конфигурация зайца
HARE_CONFIG = {
    'main_color': (200, 200, 200),
    'ear_inner_color': (255, 150, 150),
    'nose_color': (255, 100, 100),
    'eye_color': (0, 0, 0),
    'whisker_color': (0, 0, 0),
    
    # Пропорции элементов относительно общего размера
    'proportions': {
        'head': {'width': 1.0, 'height': 0.8},
        'ears': {
            'outer': {'width': 0.3, 'height': 0.9, 'y_offset': -0.7},
            'inner': {'width': 0.2, 'height': 0.7, 'y_offset': -0.6}
        },
        'eyes': {
            'radius': 0.08,
            'left_x_offset': 0.3,
            'right_x_offset': 0.7,
            'y_offset': 0.3
        },
        'nose': {
            'points': [
                (0.5, 0.45),  # Центральная верхняя точка
                (0.45, 0.55), # Левая нижняя точка
                (0.55, 0.55)   # Правая нижняя точка
            ]
        },
        'whiskers': {
            'left': {'start': (0.45, 0.5), 'end': (0.25, 0.45)},
            'right': {'start': (0.55, 0.5), 'end': (0.75, 0.45)}
        },
        'body': {'width': 1.4, 'height': 1.2, 'x_offset': -0.2, 'y_offset': 0.5},
        'legs': {
            'front': {'width': 0.4, 'height': 0.3, 'y_offset': 1.2},
            'back': {'width': 0.5, 'height': 0.4, 'y_offset': 1.4}
        },
        'tail': {'radius': 0.15, 'x_offset': 0.8, 'y_offset': 1.6}
    }
}

def draw_head(surface, config, x, y, size):
    """Рисуем голову зайца с глазами, носом и усами"""
    p = config['proportions']
    
    # Голова (эллипс)
    ellipse(surface, config['main_color'], 
            (x, y, size * p['head']['width'], size * p['head']['height']))
    
    # Глаза
    eye_radius = size * p['eyes']['radius']
    circle(surface, config['eye_color'], 
           (x + size * p['eyes']['left_x_offset'], y + size * p['eyes']['y_offset']), 
           eye_radius)
    circle(surface, config['eye_color'], 
           (x + size * p['eyes']['right_x_offset'], y + size * p['eyes']['y_offset']), 
           eye_radius)
    
    # Нос
    nose_points = [(x + size * point[0], y + size * point[1]) for point in p['nose']['points']]
    polygon(surface, config['nose_color'], nose_points)
    
    # Усы
    for side in ['left', 'right']:
        whisker = p['whiskers'][side]
        line(surface, config['whisker_color'],
             (x + size * whisker['start'][0], y + size * whisker['start'][1]),
             (x + size * whisker['end'][0], y + size * whisker['end'][1]), 1)

def draw_ears(surface, config, x, y, size):
    """Рисуем уши зайца (внешнюю и внутреннюю часть)"""
    p = config['proportions']['ears']
    
    for x_offset in [0.2, 0.5]:  # Позиции левого и правого уха
        # Внешнее ухо
        ellipse(surface, config['main_color'],
                (x + size * x_offset, 
                 y + size * p['outer']['y_offset'],
                 size * p['outer']['width'], 
                 size * p['outer']['height']))
        
        # Внутреннее ухо
        ellipse(surface, config['ear_inner_color'],
                (x + size * (x_offset + 0.05),  # Смещение внутрь
                 y + size * p['inner']['y_offset'],
                 size * p['inner']['width'], 
                 size * p['inner']['height']))

def draw_body(surface, config, x, y, size):
    """Рисуем тело зайца"""
    p = config['proportions']['body']
    ellipse(surface, config['main_color'],
            (x + size * p['x_offset'], 
             y + size * p['y_offset'],
             size * p['width'], 
             size * p['height']))

def draw_legs(surface, config, x, y, size):
    """Рисуем лапы зайца"""
    p = config['proportions']['legs']
    
    # Передние лапы
    for x_offset in [0.1, 0.5]:
        ellipse(surface, config['main_color'],
                (x + size * x_offset, 
                 y + size * p['front']['y_offset'],
                 size * p['front']['width'], 
                 size * p['front']['height']))
    
    # Задние лапы
    for x_offset in [-0.1, 0.6]:
        ellipse(surface, config['main_color'],
                (x + size * x_offset, 
                 y + size * p['back']['y_offset'],
                 size * p['back']['width'], 
                 size * p['back']['height']))

def draw_tail(surface, config, x, y, size):
    """Рисуем хвост зайца"""
    p = config['proportions']['tail']
    circle(surface, config['main_color'],
           (x + size * p['x_offset'], 
            y + size * p['y_offset']), 
           size * p['radius'])

def draw_hare(surface, config, x, y, size):
    """Рисуем всего зайца, используя все части"""
    draw_body(surface, config, x, y, size)
    draw_head(surface, config, x, y, size)
    draw_ears(surface, config, x, y, size)
    draw_legs(surface, config, x, y, size)
    draw_tail(surface, config, x, y, size)

def main():
    screen = pygame.display.set_mode((SCREEN_CONFIG['width'], SCREEN_CONFIG['height']))
    screen.fill(SCREEN_CONFIG['bg_color'])
    
    # Рисуем зайца в центре экрана
    hare_size = 100
    draw_hare(screen, HARE_CONFIG, 
              SCREEN_CONFIG['width'] // 2 - hare_size // 2, 
              100, 
              hare_size)
    
    pygame.display.update()
    clock = pygame.time.Clock()
    
    running = True
    while running:
        clock.tick(SCREEN_CONFIG['fps'])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    pygame.quit()

if __name__ == "__main__":
    main()

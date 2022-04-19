import pygame
import os

COLORS = {
    'BLACK': (0, 0, 0),
    'WHITE': (255, 255, 255)
}

WIDTH = 720
HEIGHT = 960

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Valorant clicker")

img_dir = os.path.abspath('images')

WEAPON_IMAGES = {
    '0': pygame.image.load(os.path.join(img_dir, r'classic.png')).convert_alpha(),
    '1': pygame.image.load(os.path.join(img_dir, r'ghost.png')).convert_alpha(),
    '2': pygame.image.load(os.path.join(img_dir, r'sheriff.png')).convert_alpha(),
    '3': pygame.image.load(os.path.join(img_dir, r'spectre.png')).convert_alpha(),
    '4': pygame.image.load(os.path.join(img_dir, r'judge.png')).convert_alpha(),
    '5': pygame.image.load(os.path.join(img_dir, r'guardian.png')).convert_alpha(),
    '6': pygame.image.load(os.path.join(img_dir, r'vandal.png')).convert_alpha(),
    '7': pygame.image.load(os.path.join(img_dir, r'operator.png')).convert_alpha(),
    '8': pygame.image.load(os.path.join(img_dir, r'knife.png')).convert_alpha(),
}

AGENT_IMAGES = {
    '0': pygame.image.load(os.path.join(img_dir, r'cypher.png')).convert_alpha(),
    '1': pygame.image.load(os.path.join(img_dir, r'viper.png')).convert_alpha(),
    '2': pygame.image.load(os.path.join(img_dir, r'jett.png')).convert_alpha(),
    '3': pygame.image.load(os.path.join(img_dir, r'omen.png')).convert_alpha(),
    '4': pygame.image.load(os.path.join(img_dir, r'breach.png')).convert_alpha(),
    '5': pygame.image.load(os.path.join(img_dir, r'reyna.png')).convert_alpha(),
    '6': pygame.image.load(os.path.join(img_dir, r'sage.png')).convert_alpha(),
    '7': pygame.image.load(os.path.join(img_dir, r'pheonix.png')).convert_alpha(),
    '8': pygame.image.load(os.path.join(img_dir, r'yoru.png')).convert_alpha(),
}

WEAPON_COST = {
    0: 100,
    1: 322,
    2: 777,
    3: 1337,
    4: 10501,
    5: 100500,
    6: 238238,
    7: 1000007,
    8: 12345678
}

WEAPON_DPC = {
    0: 1,
    1: 3,
    2: 7,
    3: 15,
    4: 77,
    5: 238,
    6: 777,
    7: 1307,
    8: 12345
}

AGENT_COST = {
    0: 100,
    1: 322,
    2: 777,
    3: 1337,
    4: 10501,
    5: 100500,
    6: 238238,
    7: 1000007,
    8: 12345678
}

AGENT_DPS = {
    0: 1,
    1: 3,
    2: 7,
    3: 15,
    4: 77,
    5: 238,
    6: 777,
    7: 1307,
    8: 12345
}

HOT_KEYS = {
    1: pygame.K_1,
    2: pygame.K_2,
    3: pygame.K_3,
    4: pygame.K_4,
    5: pygame.K_5,
    6: pygame.K_6,
    7: pygame.K_7,
    8: pygame.K_8,
    9: pygame.K_9,
}

BACKGROUND = pygame.image.load(os.path.join(img_dir, r'background.jpg')).convert_alpha()
TOPSTRIPE = pygame.image.load(os.path.join(img_dir, r'top_stripe.jpg')).convert_alpha()
BOTTOMSTRIPE = pygame.image.load(os.path.join(img_dir, r'bottom_stripe.jpg')).convert_alpha()
COIN = pygame.image.load(os.path.join(img_dir, r'coin.png')).convert_alpha()
LEFTARROW = pygame.image.load(os.path.join(img_dir, r'left_arrow.png')).convert_alpha()
RIGHTARROW = pygame.image.load(os.path.join(img_dir, r'right_arrow.png')).convert_alpha()

PAGE = {
    0: pygame.image.load(os.path.join(img_dir, r'active.png')).convert_alpha(),
    1: pygame.image.load(os.path.join(img_dir, r'disable.png')).convert_alpha(),
    2: pygame.image.load(os.path.join(img_dir, r'non_active.png')).convert_alpha(),
}

centar_balance = 10
balance = 0
DPC = 1
agent_DPS = 0

screen_num = 0
weapon_num = 0
agent_num = 0
max_bought_weapon = -1

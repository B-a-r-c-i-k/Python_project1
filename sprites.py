import pygame
import vars


class MainSkin(pygame.sprite.Sprite):
    def __init__(self, skin_num):
        pygame.sprite.Sprite.__init__(self)
        self.image = vars.WEAPON_IMAGES[str(max(0, skin_num))]
        self.rect = self.image.get_rect()
        self.rect.center = (vars.WIDTH / 2, vars.HEIGHT / 2)

class AgentSkin(pygame.sprite.Sprite):
    def __init__(self, skin_num):
        pygame.sprite.Sprite.__init__(self)
        self.image = vars.AGENT_IMAGES[str(max(0, skin_num))]
        self.rect = self.image.get_rect()
        self.rect.center = (vars.WIDTH / 2 - 50, vars.HEIGHT / 2 - 50)




class TopStripe(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = vars.TOPSTRIPE
        self.rect = self.image.get_rect()
        self.rect.center = (360, 50)


class BottomStripe(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = vars.BOTTOMSTRIPE
        self.rect = self.image.get_rect()
        self.rect.center = (360, vars.HEIGHT - 145 / 2)


class COIN(pygame.sprite.Sprite):
    def __init__(self, width_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = vars.COIN
        self.rect = self.image.get_rect()
        self.rect.center = (width_pos, 50)


class LeftArrow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = vars.LEFTARROW
        self.rect = self.image.get_rect()
        self.rect.center = (80, vars.HEIGHT - 145 / 2)


class RightArrow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = vars.RIGHTARROW
        self.rect = self.image.get_rect()
        self.rect.center = (640, vars.HEIGHT - 145 / 2)

class Page(pygame.sprite.Sprite):
    def __init__(self, width, height, num):
        pygame.sprite.Sprite.__init__(self)
        self.image = vars.PAGE[num]
        self.rect = self.image.get_rect()
        self.rect.center = (width, height)

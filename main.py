import pygame
import vars
import sprites
import time
import math


def draw_main_things():
    vars.screen.blit(vars.BACKGROUND, (0, 100))
    all_sprites = pygame.sprite.Group()
    top_stripe = sprites.TopStripe()
    coin = sprites.COIN(320 - vars.centar_balance * len(str(vars.balance)))
    bottom_stripe = sprites.BottomStripe()
    left_arrow = sprites.LeftArrow()
    right_arrow = sprites.RightArrow()
    all_sprites.add(top_stripe, bottom_stripe, coin, left_arrow, right_arrow)
    all_sprites.draw(vars.screen)
    font = pygame.font.Font(None, 40)
    balance_text = font.render(str(vars.balance), True, vars.COLORS['WHITE'])
    vars.screen.blit(balance_text, (360 - vars.centar_balance * len(str(vars.balance)), 40))
    damage_per_click_text = font.render("Damage per click " + str(vars.DPC), True, vars.COLORS['WHITE'])
    damage_per_second_text = font.render("Agents help per second " + str(vars.agent_DPS), True, vars.COLORS['WHITE'])
    vars.screen.blit(damage_per_click_text, (240 - vars.centar_balance * len(str(vars.DPC)), 850))
    vars.screen.blit(damage_per_second_text, (200 - vars.centar_balance * len(str(vars.agent_DPS)), 900))


def draw_screen0():
    all_sprites = pygame.sprite.Group()
    skin = sprites.MainSkin(vars.max_bought_weapon)
    all_sprites.add(skin)
    all_sprites.draw(vars.screen)
    font = pygame.font.Font(None, 30)
    right_page_text = font.render("Weapons", True, vars.COLORS['WHITE'])
    left_page_text = font.render("Agents", True, vars.COLORS['WHITE'])
    vars.screen.blit(left_page_text, (40, vars.HEIGHT - 100 / 2))
    vars.screen.blit(right_page_text, (600, vars.HEIGHT - 100 / 2))


def draw_screen1():
    all_sprites = pygame.sprite.Group()
    skin = sprites.MainSkin(vars.weapon_num)
    all_sprites.add(skin)
    for i in range(9):
        if (i == vars.weapon_num):
            page_skin_active = sprites.Page(i * 60 + 140, 150, 0)
            all_sprites.add(page_skin_active)
        elif (i - 1 > vars.max_bought_weapon):
            page_skin_disable = sprites.Page(i * 60 + 140, 150, 1)
            all_sprites.add(page_skin_disable)
        else:
            page_skin_non_active = sprites.Page(i * 60 + 140, 150, 2)
            all_sprites.add(page_skin_non_active)
    all_sprites.draw(vars.screen)
    for i in range(9):
        font = pygame.font.Font(None, 30)
        page_num = font.render(str(i + 1), True, vars.COLORS['BLACK'])
        vars.screen.blit(page_num, (i * 60 + 134, 140))
    font = pygame.font.Font(None, 40)
    weapon_cost_text = font.render("Cost " + str(vars.WEAPON_COST[vars.weapon_num]), True, vars.COLORS['WHITE'])
    weapon_DPC_text = font.render("Damage per click " + str(vars.WEAPON_DPC[vars.weapon_num]), True,
                                  vars.COLORS['WHITE'])
    vars.screen.blit(weapon_cost_text, (250, vars.HEIGHT - 300))
    vars.screen.blit(weapon_DPC_text, (190, vars.HEIGHT - 250))
    font = pygame.font.Font(None, 30)
    right_page_text = font.render("Agents", True, vars.COLORS['WHITE'])
    left_page_text = font.render("Main", True, vars.COLORS['WHITE'])
    vars.screen.blit(left_page_text, (40, vars.HEIGHT - 100 / 2))
    vars.screen.blit(right_page_text, (600, vars.HEIGHT - 100 / 2))


def draw_screen2():
    all_sprites = pygame.sprite.Group()
    skin = sprites.AgentSkin(vars.agent_num)
    all_sprites.add(skin)
    for i in range(9):
        if (i == vars.agent_num):
            page_skin_active = sprites.Page(i * 60 + 140, 150, 0)
            all_sprites.add(page_skin_active)
        else:
            page_skin_non_active = sprites.Page(i * 60 + 140, 150, 2)
            all_sprites.add(page_skin_non_active)
    all_sprites.draw(vars.screen)
    font = pygame.font.Font(None, 40)
    agent_cost_text = font.render("Cost " + str(vars.AGENT_COST[vars.agent_num]), True, vars.COLORS['WHITE'])
    agent_DPS_text = font.render("Agent helps per second " + str(vars.AGENT_DPS[vars.agent_num]), True,
                                 vars.COLORS['WHITE'])
    vars.screen.blit(agent_cost_text, (250, vars.HEIGHT - 300))
    vars.screen.blit(agent_DPS_text, (150, vars.HEIGHT - 250))
    font = pygame.font.Font(None, 30)
    right_page_text = font.render("Main", True, vars.COLORS['WHITE'])
    left_page_text = font.render("Weapons", True, vars.COLORS['WHITE'])
    vars.screen.blit(left_page_text, (40, vars.HEIGHT - 100 / 2))
    vars.screen.blit(right_page_text, (600, vars.HEIGHT - 100 / 2))
    for i in range(9):
        page_num = font.render(str(i + 1), True, vars.COLORS['BLACK'])
        vars.screen.blit(page_num, (i * 60 + 134, 140))


DRAW_SCREEN = {
    'drawscreen0': draw_screen0,
    'drawscreen1': draw_screen1,
    'drawscreen2': draw_screen2,

}


def main():
    RUN = True
    st = time.process_time()
    while (RUN):
        cur_st = time.process_time()
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                if (vars.screen_num == 0 and event.key == pygame.K_SPACE):
                    vars.balance += vars.DPC

                for i in range(9):
                    if (vars.screen_num == 1 and event.key == vars.HOT_KEYS[i + 1] and vars.max_bought_weapon + 1 >= i):
                        vars.weapon_num = i
                    if (vars.screen_num == 2 and event.key == vars.HOT_KEYS[i + 1]):
                        vars.agent_num = i

                if (vars.screen_num == 2 and event.key == pygame.K_b):
                    if (vars.balance >= vars.AGENT_COST[vars.agent_num]):
                        vars.balance -= vars.AGENT_COST[vars.agent_num]
                        vars.agent_DPS += vars.AGENT_DPS[vars.agent_num]

                if (vars.screen_num == 1 and event.key == pygame.K_b):
                    if (vars.balance >= vars.WEAPON_COST[vars.weapon_num]):
                        vars.balance -= vars.WEAPON_COST[vars.weapon_num]
                        vars.DPC += vars.WEAPON_DPC[vars.weapon_num]
                        if (vars.weapon_num - 1 == vars.max_bought_weapon):
                            vars.max_bought_weapon += 1

                if (event.key == pygame.K_RIGHT):
                    vars.screen_num = (vars.screen_num + 1) % 3
                if (event.key == pygame.K_LEFT):
                    vars.screen_num = (vars.screen_num + 2) % 3
            if (event.type == pygame.QUIT):
                RUN = False
        draw_main_things()
        DRAW_SCREEN['drawscreen' + str(vars.screen_num)]()
        vars.balance += vars.agent_DPS * (math.trunc(time.process_time() - st) - math.trunc(cur_st - st))
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import pygame, sys, random

def game():
    pygame.init()
    clock = pygame.time.Clock()
    sw,sh = 800,600
    screen = pygame.display.set_mode((sw,sh))
    pygame.display.set_caption("Protector")

    random_y = random.randint(0, sh-300)
    random_rot = random.randint(0, 180)
    x = 250

    text_size = 72
    wb = 10
    hb = 600

    score = 0


    player = pygame.image.load("data/ship.png")
    player = pygame.transform.rotate(player, -90)
    player = pygame.transform.scale(player, (100,100))
    player_rect = player.get_rect(center = (200,300))

    vel = 5

    text_change = "Elimate Asteroids"


    bullet = pygame.Rect(1000,1000, 50,5)

    enemy = pygame.image.load("data/enemy.png")
    enemy = pygame.transform.rotate(enemy, random_rot)
    enemy = pygame.transform.scale(enemy, (90,90))
    enemy_rect = enemy.get_rect(center = (sw-200, random_y))

    base_border = pygame.Rect(320, 0, wb, hb)

    font = pygame.font.SysFont('ubuntu', text_size)
    font1 = pygame.font.SysFont('ubuntu', 35)

    def game_intro():
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        intro = False

            screen.fill((0,0,0))
            intro_text = font.render("Protector", True, (0,255,0))
            screen.blit(intro_text, (sw/2-100,0))

            info_text = font1.render("Do Not let the Asteroids go into your base", True, (0,255,0))
            nfo_text = font1.render("Or past the line", True, (0,255,0))
            screen.blit(info_text, (sw/2-300,100))
            screen.blit(nfo_text, (sw/2-300,140))

            text1 = font1.render("Press SPACE to shoot", True, (0,255,0))
            screen.blit(text1, (sw/2-150,300))

            text2 = font1.render("Use WS to move, Press P to pause and C to start", True, (0,255,0))
            screen.blit(text2, (sw/2-380,400))

            pygame.display.update()
            clock.tick(5)

    def pause():
        paused = True

        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False

            screen.fill((255,255,255))
            pause_text = font.render("Paused", True, (0,0,0))
            screen.blit(pause_text, (sw/2-100,100))
            text1 = font1.render("Press C to countinue", True, (0,0,0))
            screen.blit(text1, (sw/2-150,200))
            pygame.display.update()
            clock.tick(5)

    def game_over():
        over = True
        while over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game()

            screen.fill((255,255,255))

            game_over = font.render("Game Over", True, (255,0,0))
            screen.blit(game_over, (sw/2-160,sh/2-100))

            help_text = font1.render("Sorry for your loss :(", True, (0,0,0))
            screen.blit(help_text, (sw/2-130,sh/2))

            help_text1 = font1.render("Press R to restart :(", True, (0,0,0))
            screen.blit(help_text1, (sw/2-130,sh/2+100))

            pygame.display.update()
            clock.tick(15)

    game_intro()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if bullet.x > sw:
                        bullet.x = player_rect.x+10
                        bullet.y = player_rect.y+44
                if event.key == pygame.K_p:
                    pause()


        bullet.x += 10
        enemy_rect.x -= 3

        text = font1.render(text_change, True, (255,255,255))
        score_text = font1.render("Score: " + str(score), True, (255,255,255))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and player_rect.y >= 0:
            player_rect.y -= vel
        if keys[pygame.K_s] and player_rect.y <= sh-100:
            player_rect.y += vel



        if enemy_rect.y >= sh-100:
            enemy_rect.y = enemy_rect.y - 200
        if enemy_rect.y < 0:
            enemy_rect.y = enemy_rect.y + 200



        if bullet.colliderect(enemy_rect):
            random_y = random.randint(0, sh-10)
            score += 1
            enemy_rect.x = sw+70
            enemy_rect.y = random_y

        if enemy_rect.colliderect(base_border):
            game_over()

        screen.fill((30,30,30))
        pygame.draw.rect(screen, (255,0,0), bullet)
        screen.blit(player, player_rect)
        screen.blit(enemy, enemy_rect)
        pygame.draw.rect(screen, (0,0,0), base_border)
        screen.blit(text, (sw-400,0))
        screen.blit(score_text, (0,0))
        pygame.display.update()
        clock.tick(60)
game()

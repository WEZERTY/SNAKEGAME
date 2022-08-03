import random
import time
from os import path

import pygame
import os
def game():

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 20, 20)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    HIGHT = 500
    WIDTH = 500
    xcor = WIDTH / 2
    ycor = HIGHT / 2
    foodx = round(random.randrange(0, WIDTH - 10)/10) * 10
    foody = round(random.randrange(0, HIGHT - 10)/10) * 10
    x = 0
    y = 0
    pygame.init()
    font_stile = pygame.font.SysFont(None, 22)
    score_font = pygame.font.SysFont("comicsansms", 25)
    snake_speed = 10
    snake_body = []
    length = 1
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HIGHT))

    def snakescore(score):
        mes = font_stile.render("Ваш счет: " + str(score), True, RED)
        screen.blit(mes, [0, 0])

    def newblock(snake_body):
        for x in snake_body[0:len(snake_body) - 1]:
            pygame.draw.rect(screen, GREEN, [x[0], x[1], 10, 10])

    def message(msg, color):
        mes = font_stile.render(msg, True, color)
        screen.blit(mes, [WIDTH / 16, HIGHT / 2])

    def maxscore(score):
        file = open("score.txt", "r")
        max = int(file.read())
        file.close()
        if max < score:
            file = open("score.txt", "w")
            file.write(str(score))
            file.close()
            return score
        return max
    def maxscore_message(score, max):
        mes = font_stile.render("Ваш счет: " + str(score) + " Ваш рекорд: " + str(max), True, RED)
        screen.blit(mes, [0, 30])



    pygame.display.set_caption('Змейка на PуGame')
    musicdir = path.join(path.dirname(__file__), "music")
    imagedir = path.join(path.dirname(__file__), "img")
    bg = pygame.image.load(path.join(imagedir, "поле.png")).convert()
    bg = pygame.transform.scale(bg, (WIDTH, HIGHT))
    bg_rect = bg.get_rect()
    pygame.mixer.music.load(path.join(musicdir, 'Intense.mp3'))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1)
    am = pygame.mixer.Sound(path.join(musicdir, 'apple_bite.ogg'))
    am.set_volume(0.5)
    food_zmei = [pygame.image.load(path.join(imagedir, "peres.png")).convert(), pygame.image.load(path.join(imagedir, "salad.png")).convert()]
    food = pygame.transform.scale(random.choice(food_zmei), (10, 10))
    food.set_colorkey(WHITE)
    foodrect = food.get_rect(x=foodx, y=foody)
    snake_image = pygame.transform.scale(pygame.image.load(path.join(imagedir, "HeadT.png")).convert(),(10, 10))

    run = True
    end = False
    while run:
        while end == True:
            screen.fill(BLUE)
            max = maxscore(length - 1)
            maxscore_message(length - 1, max)
            message("Ты проиграл, нажми 'С' для продолжения и 'Q' для выхода", RED)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        end = False
                        run = False
                    if event.key == pygame.K_c:
                        game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x = -10
                    snake_image = pygame.transform.scale(pygame.image.load(path.join(imagedir, "HeadL.png")).convert(),
                                                         (10, 10))
                    y = 0
                elif event.key == pygame.K_RIGHT:
                    x = 10
                    snake_image = pygame.transform.scale(pygame.image.load(path.join(imagedir, "HeadR.png")).convert(),
                                                         (10, 10))
                    y = 0
                elif event.key == pygame.K_DOWN:
                    y = 10
                    snake_image = pygame.transform.scale(pygame.image.load(path.join(imagedir, "HeadB.png")).convert(),
                                                         (10, 10))
                    x = 0
                elif event.key == pygame.K_UP:
                    y = -10
                    snake_image = pygame.transform.scale(pygame.image.load(path.join(imagedir, "HeadT.png")).convert(),
                                                         (10, 10))
                    x = 0
        xcor += x
        ycor += y
        if xcor < 0 or xcor >= WIDTH or ycor < 0 or ycor >= HIGHT:
            end = True
        if foodx == xcor and foody == ycor:
            am.play()
            foodx = round(random.randrange(0, WIDTH - 10) / 10) * 10
            foody = round(random.randrange(0, HIGHT - 10) / 10) * 10
            length += 1
            food = pygame.transform.scale(random.choice(food_zmei), (10, 10))
            food.set_colorkey(WHITE)
            foodrect = food.get_rect(x=foodx, y=foody)
        screen.fill(BLUE)
        screen.blit(bg, bg_rect)
        screen.blit(food, foodrect)
    #   pygame.draw.rect(screen, BLUE, (foodx, foody, 10, 10))
        snake_head = []
        snake_head.append(xcor)
        snake_head.append(ycor)
        snake_body.append(snake_head)
        if len(snake_body) > length:
            del snake_body[0]
        newblock(snake_body)
        for z in snake_body[:-1]:
            if z == snake_head:
                end = True
        snake_image.set_colorkey(BLACK)
        snake_rect = snake_image.get_rect(x=xcor, y=ycor)
        screen.blit(snake_image, snake_rect)
        snakescore(length -1)
        pygame.display.update()
        pygame.display.flip()
        clock.tick(snake_speed)

    message("GAME OVER", RED)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()

game()
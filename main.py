import random

import pygame

pygame.init()

width = 1158
height = 768
wn = pygame.display.set_mode((width, height))
white = (255, 255, 255)

run = True

background = pygame.image.load('background.jpg')

drop_speed = 0

basket = pygame.image.load('basket.png')
basket_x = 515
basket_y = 630
basket_speed = 0

apple = pygame.image.load('apple.png')
apple_y = -1
apple_x = random.randint(100, 1000)

mango = pygame.image.load('mango.png')
mango_y = -1
mango_x = random.randint(100, 1000)

banana = pygame.image.load('banana.png')
banana_y = -1
banana_x = random.randint(100, 1000)

pear = pygame.image.load('pear.png')
pear_y = -1
pear_x = random.randint(100, 1000)

score_value = 0
score_font = pygame.font.Font('cool_font.ttf', 50)
textX = 20
textY = 10

miss_value = 0
miss_font = pygame.font.Font('cool_font.ttf', 50)
missX = 910
missY = 10

difficulty_value = "easy"
difficulty_font = pygame.font.Font('cool_font.ttf', 50)
difficulty_x = 380
difficulty_y = 10

game_over_font = pygame.font.Font('cool_font.ttf', 200)
game_over_x = 75
game_over_y = 250

last_score_font = pygame.font.Font('cool_font.ttf', 90)
last_score_x = 175
last_score_y = 460


thing_to_drop = ["apple", "mango", "banana", "pear"]


def show_score(x, y):
    score = score_font.render(f"Score: {score_value}", True, (255, 255, 255))
    wn.blit(score, (x, y))


def show_missed(x, y):
    missed = miss_font.render(f"Missed: {miss_value}", True, (255, 255, 255))
    wn.blit(missed, (x, y))


def show_difficulty(x, y):
    difficulty = difficulty_font.render(f"Difficulty: {difficulty_value}", True, (255, 255, 255))
    wn.blit(difficulty, (x, y))


def game_over(gx, gy, lsx, lsy):
    gameover = game_over_font.render(f"GAME OVER", True, (255, 255, 255))
    last_score = last_score_font.render(f"YOUR SCORE WAS {score_value}", True, (255, 255, 255))
    wn.blit(gameover, (gx, gy))
    wn.blit(last_score, (lsx, lsy))


isgameover = False

nextthing = True

while run:
    wn.fill(white)
    wn.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and not isgameover:
                basket_speed = 6
            if event.key == pygame.K_LEFT and not isgameover:
                basket_speed = -6
            if event.key == pygame.K_q:
                isgameover = True
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT) and not isgameover:
                basket_speed = 0
    if isgameover:
        missY = 2000
        textY = 2000
        difficulty_y = 2000
        basket_y = 3000
        apple_y = 2000
        mango_y = 2000
        banana_y = 2000
        pear_y = 2000
        nextthing = False
        game_over(game_over_x, game_over_y, last_score_x, last_score_y)
    show_score(textX, textY)
    show_missed(missX, missY)
    show_difficulty(difficulty_x, difficulty_y)
    basket_x += basket_speed
    wn.blit(basket, (basket_x, basket_y))
    global thing
    if nextthing:
        thing = random.choice(thing_to_drop)
        nextthing = False
    if thing == "apple":
        apple_y += drop_speed
        wn.blit(apple, (apple_x, apple_y))
    if thing == "mango":
        mango_y += drop_speed
        wn.blit(mango, (mango_x, mango_y))
    if thing == "banana":
        banana_y += drop_speed
        wn.blit(banana, (banana_x, banana_y))
    if thing == "pear":
        pear_y += drop_speed
        wn.blit(pear, (pear_x, pear_y))
    if score_value < 20:
        drop_speed = 2
        difficulty_value = "easy"
    elif 20 <= score_value < 50:
        drop_speed = 3
        difficulty_value = "medium"
    elif score_value >= 50:
        drop_speed = 4
        difficulty_value = "hard"
    if apple_y > 704 or mango_y > 704 or banana_y > 704 or pear_y > 704:
        miss_value += 1
        if miss_value >= 10:
            isgameover = True
        else:
            apple_x = random.randint(290, 870)
            apple_y = -1
            mango_x = random.randint(290, 870)
            mango_y = -1
            banana_x = random.randint(290, 870)
            banana_y = -1
            pear_x = random.randint(290, 870)
            pear_y = -1
            nextthing = True
    if apple_y >= basket_y and (basket_x - 32) < apple_x < (basket_x + 128) or mango_y >= basket_y and (
            basket_x - 32) < mango_x < (basket_x + 128) or banana_y >= basket_y and (basket_x - 32) < banana_x < (
            basket_x + 128) or pear_y >= basket_y and (basket_x - 32) < pear_x < (basket_x + 128):
        score_value += 1
        nextthing = True
        apple_y = -1
        apple_x = random.randint(290, 870)
        mango_y = -1
        mango_x = random.randint(290, 870)
        banana_y = -1
        banana_x = random.randint(290, 870)
        pear_y = -1
        pear_x = random.randint(290, 870)
    pygame.display.update()

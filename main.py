import random
import json
import pygame

pygame.init()

width = 1158
height = 768
wn = pygame.display.set_mode((width, height))
fruits = pygame.image.load('images/fruits.png')
pygame.display.set_icon(fruits)
pygame.display.set_caption('Fruit Collect')
white = (255, 255, 255)

run = True
newhighscore = False

background = pygame.image.load('images/background.jpg')

drop_speed = 0

basket = pygame.image.load('images/basket.png')
basket_x = 515
basket_y = 630
basket_speed = 0

apple = pygame.image.load('images/apple.png')
apple_y = -1
apple_x = random.randint(100, 1000)

mango = pygame.image.load('images/mango.png')
mango_y = -1
mango_x = random.randint(100, 1000)

banana = pygame.image.load('images/banana.png')
banana_y = -1
banana_x = random.randint(100, 1000)

pear = pygame.image.load('images/pear.png')
pear_y = -1
pear_x = random.randint(100, 1000)

score_value = 0
score_font = pygame.font.Font('cool_font.ttf', 50)
incrementation = 0
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
    if newhighscore:
        last_score = last_score_font.render(f"YOUR SCORE WAS {score_value}", True, (255, 255, 255))
        high_score = last_score_font.render("NEW HIGHSCORE!!", True, (255, 255, 255))
        wn.blit(gameover, (gx, gy))
        wn.blit(last_score, (lsx, lsy))
        wn.blit(high_score, (215, 550))
    else:
        last_score = last_score_font.render(f"YOUR SCORE WAS {score_value}", True, (255, 255, 255))
        wn.blit(gameover, (gx, gy))
        wn.blit(last_score, (lsx, lsy))


isgameover = False

nextthing = True

while run:
    cursor_pos = pygame.mouse.get_pos()
    cursorXuf, cursorYuf = str(cursor_pos).split(',')
    cursorX = cursorXuf[1:]
    cursorY = cursorYuf[:-1]
    wn.fill(white)
    wn.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and not isgameover:
                if difficulty_value == "insane":
                    basket_speed = 8
                else:
                    basket_speed = 6
            if event.key == pygame.K_LEFT and not isgameover:
                if difficulty_value == "insane":
                    basket_speed = -8
                else:
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
        write_data = {"score": score_value}
        with open('scores.json') as read_file:
            data = json.load(read_file)
            if write_data["score"] > data["score"]:
                newhighscore = True
        if newhighscore:
            with open('scores.json', 'w') as write_file:
                json.dump(write_data, write_file)
    show_score(textX, textY)
    show_missed(missX, missY)
    show_difficulty(difficulty_x, difficulty_y)
    basket_x = cursorX
    wn.blit(basket, (int(basket_x), basket_y))
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
        incrementation = 1
    elif 20 <= score_value < 50:
        drop_speed = 3
        difficulty_value = "medium"
        incrementation = 1
    elif 50 <= score_value < 100:
        drop_speed = 4
        difficulty_value = "hard"
        incrementation = 2
    elif score_value >= 100:
        drop_speed = 5
        difficulty_value = "insane"
        incrementation = 3
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
    if apple_y >= basket_y and (int(basket_x) - 32) < apple_x < (int(basket_x) + 128) or mango_y >= basket_y and (
            int(basket_x) - 32) < mango_x < (int(basket_x) + 128) or banana_y >= basket_y and (int(basket_x) - 32) < banana_x < (
            int(basket_x) + 128) or pear_y >= basket_y and (int(basket_x) - 32) < pear_x < (int(basket_x) + 128):
        score_value += incrementation
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

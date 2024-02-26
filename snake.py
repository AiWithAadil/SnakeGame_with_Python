import pygame # This module for create game in python
import time
import random

pygame.init() 

#Colors section for snake game
bg_color = (0, 0, 0)
white = (255, 255, 255)
snake_color = (41, 240, 26)
food_color = (201, 18, 18)
text_color = (0, 0, 0)

# this is for display screen 
display_width = 600
display_height = 400

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# snake sizing
snake_size = 10
snake_speed = 15

font_style = pygame.font.SysFont("calibri", 25)
score_font = pygame.font.SysFont("comicsans", 34)

#def functions section
def show_score(score):
    value = score_font.render("Score: " + str(score), True, text_color)
    game_display.blit(value, [0, 0]) # blint mehthod used for display screen

def show_message(msg, color):
    message = font_style.render(msg, True, color)
    game_display.blit(message, [0, display_height / 2])

def draw_snake(snake_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(game_display, snake_color, [block[0], block[1], snake_size, snake_size])

def main_game():
    game_over = False
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, display_width - snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, display_height - snake_size) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            game_display.fill(white)
            show_message("You lost! Press P to play again or Q to quit", text_color)
            show_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        main_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0

                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0

                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_size

                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_size

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        game_display.fill(bg_color)

        pygame.draw.rect(game_display, food_color, [food_x, food_y, snake_size, snake_size])
        snake_segment = []
        snake_segment.append(x1)
        snake_segment.append(y1)
        snake_list.append(snake_segment)
        if len(snake_list) > snake_length:
            del snake_list[0]

        draw_snake(snake_size, snake_list)
        show_score(snake_length - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, display_width - snake_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, display_height - snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

main_game()




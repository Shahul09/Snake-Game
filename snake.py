import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Screen dimensions
width = 600
height = 400

# Create the game window
screen = pygame.display.set_mode((width, height))

# Set the game title
pygame.display.set_caption('Snake Game')

# Clock and font settings
clock = pygame.time.Clock()
snake_speed = 15
snake_block = 10
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display the player's score
def display_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    screen.blit(value, [0, 0])

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

# Function to display the game-over message
def game_over_message():
    message = font_style.render("You Lost! Press Q-Quit or C-Play Again", True, red)
    screen.blit(message, [width / 6, height / 3])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x = width / 2
    y = height / 2
    x_change = 0
    y_change = 0

    # Snake properties
    snake_list = []
    length_of_snake = 1

    # Initial position of food
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # Game logic
    while not game_over:

        while game_close:
            screen.fill(blue)
            game_over_message()
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        # Check boundaries (game over conditions)
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        x += x_change
        y += y_change
        screen.fill(black)

        # Draw the food
        pygame.draw.rect(screen, blue, [food_x, food_y, snake_block, snake_block])

        # Update the snake's body
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        display_score(length_of_snake - 1)

        # Check if snake eats the food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        pygame.display.update()

        # Set game speed
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
game_loop()

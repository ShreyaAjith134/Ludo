import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0,128,0)
BLUE = (0, 110, 255)
YELLOW = (255, 225, 0)

# Set up display
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 650
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ludo Game')

# Set up font
font = pygame.font.SysFont('arial', 40)

# Dice rolling function
def roll_dice():
    return random.randint(1, 6)

# Ludo path for each player (simplified)
ludo_path = [
    (0, 6), (0, 7), (0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 9), (6, 10), (6, 11), (6, 12), (6, 13), (6, 14),
    (7, 14), (8, 14), (8, 13), (8, 12), (8, 11), (8, 10), (8, 9), (9, 8), (10, 8), (11, 8), (12, 8), (13, 8), (14, 8),
    (14, 7), (14, 6), (13, 6), (12, 6), (11, 6), (10, 6), (9, 6), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1), (8, 0),
    (7, 0), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (5, 6), (4, 6), (3, 6), (2, 6), (1, 6)
]

# Load and scale tokens
red_token = pygame.transform.scale(pygame.image.load('red.png'), (35, 35))
yellow_token = pygame.transform.scale(pygame.image.load('yellow.png'), (35, 35))
green_token = pygame.transform.scale(pygame.image.load('green.png'), (35, 35))
blue_token = pygame.transform.scale(pygame.image.load('blue.png'), (35, 35))

# Set up token positions (starting from outside the board)
token_positions = {
    'red': 42,
    'blue': 29,
    'green': 3,
    'yellow': 16
}

# Set up the player turn order
players = ['blue', 'red', 'green', 'yellow']
current_player_index = 0

# Convert grid position to pixel coordinates
def grid_to_pixel(grid_pos):
    grid_size = 37
    x = grid_pos[1] * grid_size + 25  # Adjust the x position for centering
    y = grid_pos[0] * grid_size + 25  # Adjust the y position for centering
    return (x, y)

# Drawing the Ludo board (basic version)
def draw_board():
    board_img = pygame.transform.scale(pygame.image.load('board.jpg'), (555, 555))
    screen.blit(board_img,(23,23))


# Drawing dice on screen
def draw_dice(value):
    dice_text = font.render(str(value), True, BLACK)
    pygame.draw.rect(screen, BLACK, (255, 565, 45, 45), 1)
    screen.blit(dice_text, (270, 585))

# Draw tokens for each player
def draw_tokens():
    for player, pos in token_positions.items():
        if pos < len(ludo_path):  # Only draw if token is on the board
            x, y = grid_to_pixel(ludo_path[pos])
            if player == 'red':
                screen.blit(red_token,(x,y))
            elif player == 'blue':
                screen.blit(blue_token,(x,y))
            elif player == 'green':
                screen.blit(green_token,(x,y))
            elif player == 'yellow':
                screen.blit(yellow_token,(x,y))

# Move the current player's token along the path
def move_token(player, steps):
    token_positions[player] += steps
    if token_positions[player] >= len(ludo_path):  # If the token exceeds the path length, wrap around
        token_positions[player] = len(ludo_path) - 1  # Keep token at the end of the path for now

# Main game loop
def main():
    clock = pygame.time.Clock()
    dice_value = 1
    running = True

    global current_player_index

    while running:
        screen.fill(WHITE)
        draw_board()
        draw_tokens()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Press Space to roll the dice
                    dice_value = roll_dice()
                    current_player = players[current_player_index]  # Get the current player
                    move_token(current_player, dice_value)  # Move the current player's token

                    # Move to the next player's turn
                    current_player_index = (current_player_index + 1) % 4

        if current_player_index==0:
            label = font.render("Blue's turn!",1, BLUE)
            screen.blit(label, (350, 590))
        elif current_player_index==1:
            label = font.render("Red's turn!",1, RED)
            screen.blit(label, (350, 590))
        elif current_player_index==2:
            label = font.render("Green's turn!",1, GREEN)
            screen.blit(label, (350, 590))
        else:
            label = font.render("Yellow's turn!",1, YELLOW)
            screen.blit(label, (350, 590))

                     
        draw_dice(dice_value)

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()

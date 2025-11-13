import pygame
import random

# Initialize pygame
pygame.init()

# Colors
bg_color = (200, 255, 255)

# Window settings
window_width = 600
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong Game")

# Base sprite class
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# Player class
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height, is_left=True):
        super().__init__(player_image, player_x, player_y, player_speed, width, height)
        self.is_left = is_left

    def update(self):
        keys = pygame.key.get_pressed()
        if self.is_left:
            if keys[pygame.K_w] and self.rect.y > 0:
                self.rect.y -= self.speed
            if keys[pygame.K_s] and self.rect.y < window_height - self.rect.height:
                self.rect.y += self.speed
        else:
            if keys[pygame.K_UP] and self.rect.y > 0:
                self.rect.y -= self.speed
            if keys[pygame.K_DOWN] and self.rect.y < window_height - self.rect.height:
                self.rect.y += self.speed


# Game setup
clock = pygame.time.Clock()
FPS = 60

# Create paddles and ball
left_paddle = Player('paddle.png', 30, 200, 5, 20, 100, is_left=True)
right_paddle = Player('paddle.png', 550, 200, 5, 20, 100, is_left=False)
ball = GameSprite('ball.png', 300, 250, 4, 50, 50)

ball_speed_x = random.choice([-4, 4])
ball_speed_y = random.choice([-4, 4])

# Fonts
font = pygame.font.Font(None, 50)
lose_text_left = font.render("Left Player Loses!", True, (255, 0, 0))
lose_text_right = font.render("Right Player Loses!", True, (255, 0, 0))

# Game state
game = True
finish = False
show_message_time = 0

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    if not finish:
        window.fill(bg_color)

        left_paddle.update()
        right_paddle.update()

        # Move the ball
        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y

        # Ball collisions with top and bottom
        if ball.rect.y <= 0 or ball.rect.y >= window_height - ball.rect.height:
            ball_speed_y *= -1

        # Ball collisions with paddles
        if pygame.sprite.collide_rect(left_paddle, ball) or pygame.sprite.collide_rect(right_paddle, ball):
            ball_speed_x *= -1

        # Check for scoring
        if ball.rect.x < 0:
            finish = True
            show_message_time = pygame.time.get_ticks()
            window.blit(lose_text_left, (150, 200))
        elif ball.rect.x > window_width:
            finish = True
            show_message_time = pygame.time.get_ticks()
            window.blit(lose_text_right, (150, 200))

        left_paddle.reset()
        right_paddle.reset()
        ball.reset()

    else:
        # Display the last frame with the message
        window.fill(bg_color)
        left_paddle.reset()
        right_paddle.reset()
        ball.reset()

        # Show lose message for 2 seconds, then reset
        if pygame.time.get_ticks() - show_message_time < 2000:
            if ball.rect.x < 0:
                window.blit(lose_text_left, (150, 200))
            else:
                window.blit(lose_text_right, (150, 200))
        else:
            # Reset ball to center and resume play
            ball.rect.x = window_width // 2 - ball.rect.width // 2
            ball.rect.y = window_height // 2 - ball.rect.height // 2
            ball_speed_x = random.choice([-4, 4])
            ball_speed_y = random.choice([-4, 4])
            finish = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

            


import pygame
import random
bc color =(200.255,255)
window width = 600
window height = 500
window = display.set_mode((window_width,window_height)
class Gamesprite(self player_image, player_x,player_y,player_speed,width,height)
    def_init._init()
    self image = transform.scale(image.load(player_image),(width,height))
    self.speed = player_speed
    self.rect = self.image.get_rect()
    self.rect.x = player.player_x
    self.rect.y = player.player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
#player class
class player(Gamesprite):
    def_init_(self, player_image, player_x player_y, player_speed,width,height)
    def update_left(self):
    keys = key.get_pressed()
    if keys [K_s] and self.rect.y < window_height-80:
        self.rect.y += self.speed
    def move(self,is_left):
        if is_left:

#game flags
game = True
finish = False
clock = time.clock()
FPS = 60
#create paddles and ball
left_paddle = player('paddle.png',30,200)
right paddle = Player('paddle.png',520, 200)
ball = gamesprite('ball.png',200,200)
#game loop
while game:
    for e in event.get():
        if e.type == quit
        game=False
    if not finish:
        window.fill(bg_color)
        left_paddle.move()
        right_paddle.move
        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y

        #font for game over
        font.init()
        font1 = font.font(none,35)
        lose1 = style.render
!!!!


         #bounce off paddles
        if sprite.collide_rect(left_paddle, ball) or spite collide_rect(right paddle,ball)
        ball_speed_x *= -1
        ball_speed_y *= 1
        #bounce off top and bottom walls

        #check for scoring left
        if ball.rect.x < 0:
            finish= True
        window.blit(lose1,(150,200))
        game over = true

        #check for scoring right
        if ball.rect.x< window_width:
            finish=True
            


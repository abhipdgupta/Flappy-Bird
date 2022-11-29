import pygame
from pygame.locals import *
import random

pygame.init()
game_window=pygame.display.set_mode((380,650))
pygame.display.set_caption("Flappy Bird")

flappy_img=pygame.image.load('Flappy_img.png').convert_alpha()
flappy_img=pygame.transform.scale(flappy_img,(60,60))

pipe1=pygame.image.load('Cylinder_Flappy_img.png').convert_alpha()
pipe1=pygame.transform.scale(pipe1,(100,650))
pipe2=pygame.transform.scale(pipe1,(100,650))
pipe2=pygame.transform.flip(pipe2,False,True)


white=(255,0,0)
clock=pygame.time.Clock()
fps=59

font=pygame.font.SysFont(None, 40, bold=False, italic=True)


exit_game=False




def player_pos(p_img,p_x,p_y):
    game_window.blit(p_img,(p_x,p_y))

def text_display(text,color,x,y):
    display_text=font.render(text, True,color)
    game_window.blit(display_text,[x,y])  

def welcome():
    global exit_game
    game_window.fill((0,255,255))
    while not exit_game:
        flappy_text=pygame.image.load('Flappy_bird_text_img.png').convert_alpha()
        flappy_text=pygame.transform.scale(flappy_text,(300,200))
        player_pos(flappy_text,40,200)
        text_display('Enter to play game',(0,0,0),40,500)
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit()    
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        game_loop()

        pygame.display.update()

def game_loop():
 
    with open("Flappy_Bird_Game_Hi-Score.txt", "r") as f:
        hi_score=f.read()
    Fx=80            #constant position of flappy bird along x
    Fy=300           #Current Position of flappy bird along y
    l_Fy=0           #last position of flappy bird along y
    vel=3.5          #constant velocity with which bird drops
    a=80          #velocity with which bird moves up when flaps
    #velocity_x=0    no need as bird is not changing its position along x
    velocity_y=0     #declaration of current velocity along y
    score=0

    #Random positon of pipes with constrains
    ran_xa=random.randint(250,390)
    ran_y0=random.randint(-645,-200)
    ran_y400=ran_y0+650+200
    game_over=False

    global exit_game
  
    while not exit_game:
        if game_over==True:
            with open("Flappy_Bird_Game_Hi-Score.txt", "w") as f:
                f.write(str(hi_score))
            game_window.fill((0,255,255))
            game_o=pygame.image.load("Game_Over_img.png").convert_alpha()
            game_o=pygame.transform.scale(game_o,(200,300))
            player_pos(game_o,100,250)
            text_display("YOUR SCORE : "+ str(score),(255,0,0),100,200)
            text_display("HI SCORE :"+str(hi_score),white,100,300)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit()    
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        game_loop()

        else:                
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True

                if event.type==pygame.MOUSEBUTTONDOWN:
                    mouse_press=pygame.mouse.get_pressed()
                    if mouse_press[0]:
                        velocity_y=-a
                        l_Fy=Fy-30
            
            
            Fy=Fy+velocity_y+vel
            if Fy<l_Fy:
                velocity_y=0
            if Fy<0 or Fy>650:
                game_over=True

        
            game_window.fill((0,255,255))
            player_pos(flappy_img,Fx,Fy)

            player_pos(pipe1,ran_xa,ran_y400)
            player_pos(pipe2,ran_xa,ran_y0)
            ran_xa-=3
            

            if ran_xa<-90:
                score+=10
                if score>int(hi_score):
                    hi_score=score
                ran_xa=ran_xa+471
                ran_y0=random.randint(-645,-200)
                ran_y400=ran_y0+650+200
                if score>100:
                    ran_y400-=20
                if score>150:
                    ran_y400-=15
                if score>200:
                    ran_y400-=10        
            text_display('Score : '+str(score),(0,0,255),10,10)
            text_display('Hi-Score : '+str(hi_score),(0,0,255),180,10)

            #collision logic
            if Fx-ran_xa<60 and ran_xa-Fx<0:
                if ran_y400-Fy<50 or Fy-ran_y0<645:
                    game_over=True

            

        pygame.display.update()
        clock.tick(fps)     

welcome()

pygame.quit()
quit()
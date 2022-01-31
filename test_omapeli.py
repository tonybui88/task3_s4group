import pygame  
import sys    
from pygame.locals import * 
pygame.init()  

widths = 960 
hights = 600 
displays = pygame.display.set_mode((widths,hights))
pygame.display.set_caption("My new game")
black = (0,0,0)   
red= (255,0,0)  
green = (0,255,0)  
blue = (0,0,255)
white = (255,255,255) 

level = pygame.image.load("level.jpg").convert()
mario = pygame.image.load("mario.png").convert()
ball = pygame.image.load("tulipallo.png").convert()

cases = pygame.Surface((200,70))
case_1s = pygame.Surface((250,50))
cases.fill(blue) 
case_1s.fill(red)

displays.blit(level, (0,0))
displays.blit(ball, (0,0))
displays.blit(mario, (400,500))
displays.blit(cases, (0,200))
displays.blit(case_1s, (widths-250,600))

pygame.display.update()

ball_area = ball.get_rect()
mario_area = mario.get_rect()
cases_area = cases.get_rect()
case_1s_area = case_1s.get_rect()

ball_area.left = 400
mario_area.top = 500
cases_area.left = 0
cases_area.top = 200
case_1s_area.right = widths
case_1s_area.top = 300

speeds = [1,1]

font_style = pygame.font.SysFont(None, 50)
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    displays.blit(mesg, [widths/5, hights/2])

def gameloop():
    game_over = False
    game_close = False
    while not game_over:
        while game_close == True:
            displays.fill(white)
            message('Game Over! Press Q-Quit ', red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit() 
                    sys.exit()   
                if event.type == KEYDOWN:    
                    if event.key == K_ESCAPE: 
                        pygame.quit() 
                        sys.exit()
                    if event.key == K_q:
                        game_over = True
                        game_close = False
        for event in pygame.event.get():  
            if event.type == pygame.QUIT: 
                pygame.quit() 
                sys.exit()    
            if event.type == KEYDOWN:     
                if event.key == K_ESCAPE: 
                    pygame.quit() 
                    sys.exit()    
        ball_area.move_ip(speeds)
        if ball_area.left < 0 or ball_area.right > widths:
            speeds[0] = -speeds[0]
        if ball_area.top < 0 or ball_area.bottom > hights:
            speeds[1] = -speeds[1]
        if cases_area.colliderect(ball_area):
            if cases_area.colliderect(ball_area.move(-speeds[0],0)):
                speeds[1] = -speeds[1]    
            else:
                speeds[0] = -speeds[0]
        if case_1s_area.colliderect(ball_area):
            if case_1s_area.colliderect(ball_area.move(-speeds[0],0)):
                speeds[1] = -speeds[1]    
            else:
                speeds[0] = -speeds[0]

        mario_move = pygame.key.get_pressed()
        if mario_move[K_LEFT]:
            if mario_area.left < 0:
                mario_area.move_ip((0,0))
            else:       
                mario_area.move_ip((-1,0))  
        if mario_move[K_RIGHT]:
            if mario_area.right > widths:
                mario_area.move_ip((0,0))
            else:
                mario_area.move_ip((1,0))
        if mario_move[K_DOWN]:
            if mario_area.bottom > hights:
                mario_area.move_ip((0,0))
            else:
                mario_area.move_ip((0,1))
        if mario_move[K_UP]:
            if mario_area.top < 0:
                mario_area.move_ip((0,0))
            else:
                mario_area.move_ip((0,-1))
        
        if mario_area.colliderect(ball_area):
            game_close = True
            
        displays.blit(level, (0,0)) 
        displays.blit(ball, ball_area)
        displays.blit(mario, mario_area)
        displays.blit(cases, cases_area)
        displays.blit(case_1s, case_1s_area)
        pygame.display.update()
    pygame.quit()
    quit()
gameloop()
    
    
            
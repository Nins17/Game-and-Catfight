import pygame
import os
pygame.font.init()


#bellow are assigned variables

WIDTH, HEIGHT = 1450, 870
WIN=pygame.display.set_mode((WIDTH, HEIGHT))666
pygame.display.set_caption("Cat Fight")



CEBC7E = (206,188,126)
YELLOWGREEN = (0,255,0)
BROWN=(51,25,0)
WHITE=(255,255,255)
GAMEBORDER = pygame.Rect(WIDTH//2,0,3,HEIGHT)
FPS = 60
VEL =5
BULL_VEL = 20   
MAXNUM_BULL = 4

FONT_HEALTH = pygame.font.SysFont('calibri', 40)
RESULT_FONT = pygame.font.SysFont('comicsans', 80)
NOTE_FONT = pygame.font.SysFont('calibri', 30)

BG =pygame.transform.scale(pygame.image.load(os.path.join('imgs/bg5.jpg')),(WIDTH ,HEIGHT))

CHAR_ONE_HIT = pygame.USEREVENT + 1
CHAR_TWO_HIT = pygame.USEREVENT + 2 

CHARACTER_W,CHARACTER_H = 140,140
CHARACTER_WD,CHARACTER_HT = 1,1
CHARACTER_ONE_IMAGE =pygame.image.load(os.path.join('imgs/maine-coon-cat.png'))
CHARACTER_TWO_IMAGE =pygame.image.load(os.path.join('imgs/turkish-angora.png'))
TR_IMAGE =pygame.image.load(os.path.join('imgs/maine-coon-cat.png'))
TR_TWO_IMAGE =pygame.image.load(os.path.join('imgs/turkish-angora.png'))
CHARACTER_1 = pygame.transform.scale(CHARACTER_ONE_IMAGE, (CHARACTER_W,CHARACTER_H ))
CHARACTER_2 = pygame.transform.scale(CHARACTER_TWO_IMAGE, (CHARACTER_W,CHARACTER_H ))
TRANSCHAR_1 = pygame.transform.scale(TR_IMAGE,(CHARACTER_WD,CHARACTER_HT))
TRANSCHAR_2 = pygame.transform.scale(TR_TWO_IMAGE,(CHARACTER_WD,CHARACTER_HT))

BULL_w,BULL_H = 50,50
BULLET1_IMAGE= pygame.image.load(os.path.join('imgs/paintball.png'))
BULLET2_IMAGE= pygame.image.load(os.path.join('imgs/paintball2.png'))
BULLET1= pygame.transform.scale(BULLET1_IMAGE, (BULL_w, BULL_H ))
BULLET2=pygame.transform.scale(BULLET2_IMAGE, (BULL_w, BULL_H ))


    

# Movement of Character 1
def Char1_movement(keys_pressed, char_one):
    if keys_pressed[pygame.K_a] and  char_one.x - VEL > 0:#character1 left key
        char_one.x -= VEL 
    elif keys_pressed[pygame.K_d] and  char_one.x + VEL +  char_one.width < GAMEBORDER.x:#character1 right key
        char_one.x += VEL 
    elif keys_pressed[pygame.K_w] and  char_one.y - VEL > 0:#character1 up key
        char_one.y -= VEL 
    elif keys_pressed[pygame.K_s] and  char_one.y + VEL +  char_one.height < HEIGHT -15 :#character1 down key
        char_one.y += VEL
           
# Movement of Character 2
def Char2_movement(keys_pressed,char_two):   
    if keys_pressed[pygame.K_j] and char_two.x - VEL > GAMEBORDER.x + GAMEBORDER.width :#character2 left key
        char_two.x -= VEL 
    elif keys_pressed[pygame.K_l] and char_two.x + VEL + char_two.width < WIDTH:#character2 right key
        char_two.x += VEL 
    elif keys_pressed[pygame.K_i] and char_two.y - VEL > 0:#character2 up key
        char_two.y -= VEL 
    elif keys_pressed[pygame.K_k] and char_two.y + VEL + char_two.height < HEIGHT -15 :#character2 down key
        char_two.y += VEL 

   
#bullet things condition when the bullets hit the opponents
def hadle_bullets(char_one_bullets, char_two_bullets,char_one,char_two):
    for bullet in char_one_bullets:
        bullet.x += BULL_VEL
        if char_two.colliderect(bullet):
            pygame.event.post(pygame.event.Event(CHAR_TWO_HIT))
            char_one_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            char_one_bullets.remove(bullet)
            
    for bullet in char_two_bullets:
        bullet.x -= BULL_VEL
        if char_one.colliderect(bullet):
            pygame.event.post(pygame.event.Event(CHAR_ONE_HIT))
            char_two_bullets.remove(bullet)
        elif bullet.x<0:
            char_two_bullets.remove(bullet)
           
#display the winner           
def draw_winner(text):
    draw_text = RESULT_FONT.render(text, 1, YELLOWGREEN)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2-35))  
    pygame.display.update()
    pygame.time.delay(2000)
  
    
 #display note   
def  draw_note(text):
    draw_text = NOTE_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2+45))
    pygame.display.update()
    pygame.time.delay(5000)
    
    
    
# main window of the game where the characters are there.
def main_window(char_one, char_two, char_one_bullets,char_two_bullets,char_one_health,char_two_health):
    WIN.blit(BG,(0,0))
    pygame.draw.rect(WIN,BROWN,GAMEBORDER )
    char_one_healthtxt = FONT_HEALTH.render("Health: " + str(char_one_health),1, CEBC7E)
    char_two_healthtxt = FONT_HEALTH.render("Health: " + str(char_two_health),1, CEBC7E)
    WIN.blit(char_two_healthtxt,(WIDTH-char_two_healthtxt.get_width() - 15, 15))
    WIN.blit(char_one_healthtxt,(15,15))
    
    WIN.blit(CHARACTER_1,(char_one.x, char_one.y))
    WIN.blit(CHARACTER_2,(char_two.x, char_two.y))
    
    for bullet in char_one_bullets:
        WIN.blit(BULLET1, (bullet)) 
        
    for bullet in char_two_bullets:
       WIN.blit(BULLET2, (bullet))
    pygame.display.update()
            
          

# The function
def main():
    char_one = pygame.Rect(5, 500, CHARACTER_W,CHARACTER_H )    
    char_two = pygame.Rect(1310, 500, CHARACTER_W,CHARACTER_H )
    
    char_one_bullets = []
    char_two_bullets = []
    char_one_health  = 100
    char_two_health  = 100
    char_one_damage = 13
    char_two_damage  =14
    
    
    clock =pygame.time.Clock()
    run = True
    while run: 
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit() 
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(char_one_bullets) < MAXNUM_BULL:
                    bullet = pygame.Rect(char_one.x +char_one.width,char_one.y +
                        char_one.height//2-2, 20,15)
                    char_one_bullets.append(bullet)    
                
                if event.key == pygame.K_RCTRL and len(char_two_bullets) < MAXNUM_BULL:
                    bullet = pygame.Rect(char_two.x,char_two.y + 
                        char_two.height//2-2, 20,15)
                    char_two_bullets.append(bullet) 
                    
                    
            if event.type == CHAR_ONE_HIT: 
                char_one_health -= char_two_damage
                
            
            if event.type == CHAR_TWO_HIT:
                char_two_health -= char_one_damage 
                
            
            
        autosrt_text="wait........ **THE GAME WILL RESTART AUTOMATICALLY***"
        winner_text = ""
       
        if char_one_health <= 0:
            winner_text = "Right Side Wins!"
           
           
            
        if char_two_health <= 0:       
            winner_text = "Left Side Wins!"
           
                      
        if winner_text != "" and autosrt_text!="":
            draw_winner((winner_text)) 
            draw_note((autosrt_text))
            break  
        
        keys_pressed = pygame.key.get_pressed()
        Char1_movement(keys_pressed, char_one)
        Char2_movement(keys_pressed, char_two) 
        
        hadle_bullets(char_one_bullets, char_two_bullets,char_one,char_two)
             
        main_window(char_one,char_two,char_one_bullets,char_two_bullets,char_one_health,char_two_health)        
       
     
              
 
    main()
   
    
if __name__ =="__main__":
    main()
    

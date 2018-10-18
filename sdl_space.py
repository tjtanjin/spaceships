import sys
import pygame as pg
import random
pg.init()

class Ship(pg.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__()
        self.images = []
        self.images.append(pg.image.load('C:/Users/User/AppData/Local/Programs/Python/Python37-32/images/space-ship_1.png'))
        self.images.append(pg.image.load('C:/Users/User/AppData/Local/Programs/Python/Python37-32/images/space-ship_2.png'))
        self.images.append(pg.image.load('C:/Users/User/AppData/Local/Programs/Python/Python37-32/images/space-ship_3.png'))

        self.index = 0

        self.image = self.images[self.index]

        self.rect = self.image.get_rect()

        self.rect.x = 175
        self.rect.y = 600

        self.phealth = 3

    def update(self):

        self.index += 1
        
        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]

        self.reload = pg.time.get_ticks()

        if self.rect.x > screen_x - 116:
            self.rect.x = screen_x - 116
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def shoot(self, bullet_type):
        self.rect.x += pixels

    def health(self, damage):
        if damage == True:
            self.phealth -= 1
            pg.mixer.music.load('C:/Users/User/Appdata/Local/Programs/Python/Python37-32/sound/space-sound_pdamage.wav')
            pg.mixer.music.play()

class Bullet(pg.sprite.Sprite):
    def __init__(self):
        super(Bullet, self).__init__()
        self.images = []
        self.images.append(pg.image.load('C:/Users/User/AppData/Local/Programs/Python/Python37-32/images/space-pbullet_1.png'))
        self.images.append(pg.image.load('C:/Users/User/AppData/Local/Programs/Python/Python37-32/images/space-pbullet_2.png'))
        
        self.index = 0

        self.image = self.images[self.index]

        self.rect = self.image.get_rect()

    def update(self):

        self.index += 1
        
        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]

        self.rect.y -= 10

        if self.rect.y < 0:
            self.kill()
        
class Smallmeteor(pg.sprite.Sprite):
    def __init__(self):
        super(Smallmeteor, self).__init__()
        self.images = []
        self.images.append(pg.transform.scale(pg.image.load('C:/Users/User/AppData/Local/Programs/Python/Python37-32/images/space-meteor_small_1.png'), (48,48)))
        self.images.append(pg.transform.scale(pg.image.load('C:/Users/User/AppData/Local/Programs/Python/Python37-32/images/space-meteor_small_2.png'), (48,48)))
        self.images.append(pg.transform.scale(pg.image.load('C:/Users/User/AppData/Local/Programs/Python/Python37-32/images/space-meteor_small_3.png'), (48,48)))
        self.images.append(pg.transform.scale(pg.image.load('C:/Users/User/AppData/Local/Programs/Python/Python37-32/images/space-meteor_small_4.png'), (48,48)))

        self.index = random.randint(0,3)

        self.image = self.images[self.index]

        self.rect = self.image.get_rect()

        self.x = 200
        self.y = 200

    def update(self):
        
        self.index += 1
        
        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]

        self.rect.y += 4

        self.x = self.x + self.rect.x
        self.y = self.y + self.rect.y

        if self.rect.y > 700:
            self.kill()

    def bounce(self):
        self.rect.y -= 15
        self.rect.x = random.randint(-5,5)

class Enemy1(pg.sprite.Sprite):
    def __init__(self):
        super(Enemy1, self).__init__()
        self.images = []
        self.images.append(pg.image.load('C:/Users/User/AppData/Local/Programs/Python/Python37-32/images/space-e1_1.png'))
        self.images.append(pg.image.load('C:/Users/User/AppData/Local/Programs/Python/Python37-32/images/space-e1_2.png'))
        
        self.index = 0

        self.image = self.images[self.index]

        self.rect = self.image.get_rect()

    def update(self):
        
        self.index += 1
        
        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]

        self.rect.y += 3

        if self.rect.y > 700:
            self.kill()

class Smallex(pg.sprite.Sprite):
    def __init__(self):
        super(Smallex, self).__init__()
        self.images = []
        self.images.append(pg.transform.scale(pg.image.load('C:/Users/User/AppData/Local/Programs/Python/Python37-32/images/space-smallex_1.png'), (96,96)))
        self.images.append(pg.transform.scale(pg.image.load('C:/Users/User/AppData/Local/Programs/Python/Python37-32/images/space-smallex_2.png'), (96,96)))
        self.images.append(pg.transform.scale(pg.image.load('C:/Users/User/AppData/Local/Programs/Python/Python37-32/images/space-smallex_3.png'), (96,96)))
        self.images.append(pg.transform.scale(pg.image.load('C:/Users/User/AppData/Local/Programs/Python/Python37-32/images/space-smallex_4.png'), (96,96)))
        self.images.append(pg.transform.scale(pg.image.load('C:/Users/User/AppData/Local/Programs/Python/Python37-32/images/space-smallex_5.png'), (96,96)))
        
        self.index = 0

        self.image = self.images[self.index]

        self.rect = self.image.get_rect()

        pg.mixer.music.load('C:/Users/User/Appdata/Local/Programs/Python/Python37-32/sound/space-sound_smallex.wav')
        pg.mixer.music.play()

    def update(self):

        self.index += 1
        
        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]

        if self.index == 4:
            self.kill()

# --- Basic Set Up ---
clock = pg.time.Clock()
# --- Main Surface/Caption ---
screen_x = 500
screen_y = 700
screen = pg.display.set_mode((screen_x, screen_y))
pg.display.set_caption("SpaceShips!")
# --- Fonts to be used ---
score_font = pg.font.SysFont("Times", 24)
gameintro_text1_font = pg.font.SysFont("Calibri", 32)
gameintro_text2_font = pg.font.SysFont("Comic Sans", 72)
gameintro_instruction_font = pg.font.SysFont("Times", 18)
gameintro_instruction2_font = pg.font.SysFont("Comic Sans", 28)
gameover_text_font = pg.font.SysFont("Comic Sans", 72)
gameover_text2_font = pg.font.SysFont("Times", 24)
gameover_text3_font = pg.font.SysFont("Times", 30)
highscore_text_font = pg.font.SysFont("Times", 40)
# --- Colors to be used ---
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)

def text_objects(text, font, text_c):
    text_surface = font.render(text, True, text_c)
    return text_surface, text_surface.get_rect()

def button(text, text_s, text_c, x, y, w, h, ic, ac, action=None):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pg.draw.rect(screen, ac, (x,y,w,h))

        if click[0] == 1 and action != None:
            action()

    else:
        pg.draw.rect(screen, ic, (x,y,w,h))

    buttontext = pg.font.SysFont("Comic Sans", text_s)
    text_surface, text_rect = text_objects(text, buttontext, text_c)
    text_rect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(text_surface, text_rect)
# --- Game Intro Loop ---
def game_intro(dt):
    gameintro = True
    while gameintro == True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameintro = False
            mouse = pg.mouse.get_pos()
            if event.type == pg.MOUSEBUTTONDOWN and 300 > mouse[0] > 200 and 450 > mouse[1] > 400:
                gameintro = False
                gameplay = True
        
        screen.fill((0,0,0))
        button("Start!", 32, (255, 255, 255), 200, 400, 100, 50, (255, 0, 0), (200, 200, 200))
        gameintro_text1 = gameintro_text1_font.render("Welcome to", True, white)
        gameintro_text2 = gameintro_text2_font.render("Space Ships!", True, yellow)
        gameintro_text3 = gameintro_instruction_font.render("<- Left Arrow                Right Arrow ->", True, white)
        gameintro_text4 = gameintro_instruction2_font.render("MOVE", True, green)
        gameintro_text5 = gameintro_instruction_font.render("Space                   Bar", True, white)
        gameintro_text6 = gameintro_instruction2_font.render("SHOOT", True, green)
        screen.blit(gameintro_text1, (167, 200))
        screen.blit(gameintro_text2, (97, 250))
        screen.blit(gameintro_text3, (107, 310))
        screen.blit(gameintro_text4, (220, 312))
        screen.blit(gameintro_text5, (161, 332))
        screen.blit(gameintro_text6, (214, 334))
        pg.display.flip()
    gameplay = True
    highscore = 0
    game_play(gameplay, dt, highscore)
# --- Game Play Loop ---
def game_play(gameplay, dt, highscore):
    # --- Sprites/Characters Management ---
    interactive_objects = pg.sprite.Group()
    player_list = pg.sprite.Group()
    bullet_list = pg.sprite.Group()
    enemy_list = pg.sprite.Group()
    enemy_e1_list = pg.sprite.Group()
    enemy_smallmeteor_list = pg.sprite.Group()
    ship = Ship()
    player_list.add(ship)
    interactive_objects.add(ship)
    damage = False
    score = 0
    time_elapsed_since_pbullet = 0
    time_elapsed_since_e1spawn = 0
    time_elapsed_since_smallmeteorspawn = 0
    time_elapsed_since_bigmeteorspawn = 0
    gameplay = True
    while gameplay == True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameplay = False
        keypressed = pg.key.get_pressed()
        if keypressed[pg.K_LEFT]:
            ship.moveLeft(5)
        if keypressed[pg.K_RIGHT]:
            ship.moveRight(5)
        time_elapsed_since_pbullet += dt 
        if keypressed[pg.K_SPACE] and ship.phealth > 0 and time_elapsed_since_pbullet > 2000:
            bullet = Bullet()
            bullet.rect.x = ship.rect.x + 35
            bullet.rect.y = ship.rect.y
            interactive_objects.add(bullet)
            bullet_list.add(bullet)
            bullet = Bullet()
            bullet.rect.x = ship.rect.x + 75
            bullet.rect.y = ship.rect.y
            interactive_objects.add(bullet)
            bullet_list.add(bullet)
            time_elapsed_since_pbullet = 0
        time_elapsed_since_e1spawn += dt
        if time_elapsed_since_e1spawn > random.randint(6000,7000):
            e1 = Enemy1()
            e1.rect.x = random.randint(-400, 400)
            e1.rect.y = -120
            interactive_objects.add(e1)
            enemy_list.add(e1)
            enemy_e1_list.add(e1)
            time_elapsed_since_e1spawn = 0
        time_elapsed_since_smallmeteorspawn += dt
        if time_elapsed_since_smallmeteorspawn > random.randint(4000,5000):
            smallmeteor = Smallmeteor()
            smallmeteor.rect.x = random.randint(-400, 400)
            smallmeteor.rect.y = -100    
            interactive_objects.add(smallmeteor)
            enemy_list.add(smallmeteor)
            enemy_smallmeteor_list.add(smallmeteor)
            time_elapsed_since_smallmeteorspawn = 0
##        time_elapsed_since_bigmeteorspawn += dt
##        if time_elapsed_since_bigmeteorspawn > 5000:
##            bigmeteor = Meteor()
##            bigmeteor.rect.x = random.randint(-400, 400)
##            bigmeteor.rect.y = -100    
##            interactive_objects.add(bigmeteor)
##            enemy_list.add(bigmeteor)
##            time_elapsed_since_bigmeteorspawn = 0

        for hits in interactive_objects:
            meteorhits = pg.sprite.groupcollide(bullet_list, enemy_smallmeteor_list, True, True)  
            e1hits = pg.sprite.groupcollide(bullet_list, enemy_e1_list, True, True)
            playerhit = pg.sprite.groupcollide(player_list, enemy_list, False, True)
            for bullet_hit in meteorhits:
                score += 1
            for bullet_hit in e1hits:
                smallex = Smallex()
                smallex.rect.x = bullet_hit.rect.x - 40
                smallex.rect.y = bullet_hit.rect.y - 100
                interactive_objects.add(smallex)
                score += 5
            for damage_taken in playerhit:
                damage = True
                ship.health(damage)

        if ship.phealth <= 0:
            ship.kill()
            e1.kill()
            smallmeteor.kill()

        screen.fill((0,0,0))
        interactive_objects.update()
        interactive_objects.draw(screen)
        highscoreboard = score_font.render("High Score: " + str(highscore), True, (255, 255, 255))
        scoreboard = score_font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(scoreboard, (20, 50))
        screen.blit(highscoreboard, (20, 20))
        pg.display.flip()
        clock.tick(60)
        if ship.phealth <= 0:
            gameplay = False
    
    game_over(score, highscore)
# --- Game Over Loop ---
def game_over(score, highscore):
    gameover = True
    while gameover == True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameover = False
            mouse = pg.mouse.get_pos()
            if event.type == pg.MOUSEBUTTONDOWN and 300 > mouse[0] > 200 and 450 > mouse[1] > 400:
                gameplay = True
                gameover = False
        
        screen.fill((0,0,0))
        button("Start!", 32, (255, 255, 255), 200, 400, 100, 50, (255, 0, 0), (200, 200, 200))
        gameover_text = gameover_text_font.render("Game Over!", True, red)
        gameover_text2 = gameover_text2_font.render("Your High Score is:", True, white)
        gameover_text3 = gameover_text3_font.render(str(score), True, yellow)
        if score > highscore:
            highscore_text = highscore_text_font.render("You set a new highscore!", True, green)
            screen.blit(highscore_text, (50, 500))
        
        screen.blit(gameover_text, (110, 200))
        screen.blit(gameover_text2, (155, 300))
        screen.blit(gameover_text3, (240, 350))
        pg.display.flip()
    if score > highscore:
        highscore = score
    game_play(gameplay, dt, highscore)

    game_over(score, highscore)
dt = clock.tick()
game_intro(dt)
            
                

import sys
import pygame as pg
import random
pg.init()
# --- Player-Related Classes ---
# --- Player Space Ship ---
class Ship(pg.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__()
        #player sprites/animation
        self.images = []
        self.images.append(pg.image.load('space-image_ship_1.png'))
        self.images.append(pg.image.load('space-image_ship_2.png'))
        self.images.append(pg.image.load('space-image_ship_3.png'))
        self.index = 0
        self.image = self.images[self.index]
        #player position
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 600
        #player initial health count
        self.health = 3
        #player power up count
        self.powerupvalue = 0
        #player specific initial timers set to 0
        self.time_elapsed_since_pshoot = 0
        self.time_elapsed_since_powerup1 = 0
        self.time_elapsed_since_powerup2 = 0
    #player update at every frame
    def update(self):
        #player animation update
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        #player stays within play area
        if self.rect.x > screen_x - 116:
            self.rect.x = screen_x - 116
        if self.rect.x < 0:
            self.rect.x = 0
        #player shoot rate
        self.time_elapsed_since_pshoot += dt
    #player move right
    def moveRight(self, pixels):
        self.rect.x += pixels
    #player move left
    def moveLeft(self, pixels):
        self.rect.x -= pixels
    #player shoot
    def shoot(self):
        if self.time_elapsed_since_pshoot >= 160 and self.powerupvalue == 0: #player shoot with no powerup
            bullet = Bullet()
            bullet.rect.x, bullet.rect.y = self.rect.x + 35, self.rect.y
            interactive_objects.add(bullet)
            bullet_list.add(bullet)
            bullet = Bullet()
            bullet.rect.x, bullet.rect.y = self.rect.x + 75, self.rect.y
            interactive_objects.add(bullet)
            bullet_list.add(bullet)
            self.time_elapsed_since_pshoot = 0
        elif self.time_elapsed_since_pshoot >= 160 and self.powerupvalue == 1: #player shoot with powerup1
            bullet = Bullet()
            bullet.rect.x, bullet.rect.y = self.rect.x + 35, self.rect.y
            interactive_objects.add(bullet)
            bullet_list.add(bullet)
            bullet = Bullet()
            bullet.rect.x, bullet.rect.y = self.rect.x + 75, self.rect.y
            interactive_objects.add(bullet)
            bullet_list.add(bullet)
            bullet = Bullet()
            bullet.rect.x, bullet.rect.y = self.rect.x + 55, self.rect.y - 20
            interactive_objects.add(bullet)
            bullet_list.add(bullet)
            self.time_elapsed_since_pshoot = 0
        elif self.time_elapsed_since_pshoot >= 160 and self.powerupvalue == 2: #player shoot with powerup2
            pbullet2 = Pbullet2()
            pbullet2.rect.x, pbullet2.rect.y = self.rect.x + 35, self.rect.y - 635
            interactive_objects.add(pbullet2)
            opbullet_list.add(pbullet2)
            pbullet2 = Pbullet2()
            pbullet2.rect.x, pbullet2.rect.y = self.rect.x + 75, self.rect.y - 635
            interactive_objects.add(pbullet2)
            opbullet_list.add(pbullet2)
            self.time_elapsed_since_pshoot = 0
    #player test shoot
    def testshoot(self):
        if self.time_elapsed_since_pshoot >= 160: #player test shoot in gamemode select screen
            bullet = Bullet()
            bullet.rect.x, bullet.rect.y = self.rect.x + 35, self.rect.y
            test_list.add(bullet)
            bullet = Bullet()
            bullet.rect.x, bullet.rect.y = self.rect.x + 75, self.rect.y
            test_list.add(bullet)
            self.time_elapsed_since_pshoot = 0
    #player powerups
    def powerup(self):
        if self.powerupvalue == 1: #powerup1
            self.time_elapsed_since_powerup2 = 0 #reset other active powerups
            self.time_elapsed_since_powerup1 += dt
            if self.time_elapsed_since_powerup1 > 10000: #powerup1 duration (10sec)
                self.powerupvalue = 0
                self.time_elapsed_since_powerup1 = 0
        if self.powerupvalue == 2: #powerup2
            self.time_elapsed_since_powerup1 = 0 #reset other active powerups
            self.time_elapsed_since_powerup2 += dt
            if self.time_elapsed_since_powerup2 > 10000: #powerup2 duration (10sec)
                self.powerupvalue = 0
                self.time_elapsed_since_powerup2 = 0
    def consume(self):
        pg.mixer.Channel(1).play(pg.mixer.Sound('space-sound_powerup1.wav'))
# --- Player Main Bullet ---
class Bullet(pg.sprite.Sprite):
    def __init__(self):
        super(Bullet, self).__init__()
        #player bullet sprites/animation
        self.images = []
        self.images.append(pg.image.load('space-image_pbullet_1.png'))
        self.images.append(pg.image.load('space-image_pbullet_2.png'))
        self.index = 0
        self.image = self.images[self.index]
        #player bullet position
        self.rect = self.image.get_rect()
        #player bullet sound
        pg.mixer.Channel(0).play(pg.mixer.Sound('space-sound_pbullet.wav'))
    #player bullet update at every frame
    def update(self):
        #player bullet animation update
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        #player bullet speed/direction
        self.rect.y -= 10
        #player bullet killed once it leaves screen
        if self.rect.y < 0:
            self.kill()
# --- Player Power Up 2 Bullet ---
class Pbullet2(pg.sprite.Sprite):
    def __init__(self):
        super(Pbullet2, self).__init__()
        #pbullet2 sprites/animation
        self.images = []
        self.images.append(pg.transform.scale(pg.image.load('space-image_pbullet2_1.png'), (5, 650)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_pbullet2_2.png'), (5, 650)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_pbullet2_3.png'), (5, 650)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_pbullet2_4.png'), (5, 650)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_pbullet2_5.png'), (5, 650)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_pbullet2_6.png'), (5, 650)))
        self.index = 0
        self.image = self.images[self.index]
        #pbullet2  position
        self.rect = self.image.get_rect()
        #pbullet2 specific initial timer set to 0
        self.time_elapsed_since_pshoot2 = 0
        #pbullet2  sound
##tobeupdated        pg.mixer.Channel(0).play(pg.mixer.Sound('space-sound_pbullet.wav'))
    #pbullet2  update at every frame
    def update(self):
        #pbullet2  animation update
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        #pbullet2 removed every 160 ticks to simulate tracing laser
        self.time_elapsed_since_pshoot2 += dt
        if self.time_elapsed_since_pshoot2 > 160:
            self.kill()
            self.time_elapsed_since_pshoot2 = 0
# --- Player Life Display ---
class Playerlife(pg.sprite.Sprite):
    def __init__(self):
        super(Playerlife, self).__init__()
        #player life display sprites/animation
        self.images = []
        self.images.append(pg.transform.scale(pg.image.load('space-image_plife.png'), (36, 36)))
        self.index = 0
        self.image = self.images[self.index]
        #player life display position
        self.rect = self.image.get_rect()
    #player life display update at every frame
    def update(self):
        None
# --- Enemy-Related Classes ---
# --- Enemy 1 ---
class Enemy1(pg.sprite.Sprite):
    def __init__(self):
        super(Enemy1, self).__init__()
        #enemy 1 sprites/animation
        self.images = []
        self.images.append(pg.transform.scale(pg.image.load('space-image_e1_1.png'), (87, 90)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_e1_2.png'), (87, 90)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_e1_3.png'), (87, 90)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_e1_4.png'), (87, 90)))
        self.index = random.randint(0,3) #randomize starting index(frame) to play
        self.image = self.images[self.index]
        #enemy 1 position
        self.rect = self.image.get_rect()
        #enemy 1 initial health count
        self.health = 2
        #enemy 1 id
        self.id = 1
    #enemy 1 update at every frame
    def update(self):
        #enemy 1 animation update  
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        #enemy 1 speed/direction
        self.rect.y += 3
        #enemy 1 killed once it leaves screen
        if self.rect.y > 700:
            self.kill()
        #enemy 1 killed once health below 0
        if self.health <= 0:
            self.kill()
    #enemy 1 spawn
    def spawn(self):
        self.rect.x = random.randint(-20, 450)
        self.rect.y = -120
        interactive_objects.add(self)
        enemy_list.add(self)
# --- Enemy 2 ---
class Enemy2(pg.sprite.Sprite):
    def __init__(self):
        super(Enemy2, self).__init__()
        #enemy 2 sprites/animation
        self.images = []
        self.images.append(pg.transform.scale(pg.image.load('space-image_e2_1.png'), (76, 100)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_e2_2.png'), (76, 100)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_e2_3.png'), (76, 100)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_e2_4.png'), (76, 100)))
        self.index = random.randint(0,3) #randomize starting index(frame) to play
        self.image = self.images[self.index]
        #enemy 2 position
        self.rect = self.image.get_rect()
        #enemy 2 specific initial timer set to 0
        self.time_elapsed_since_e2shoot = 0
        #enemy 2 initial health count
        self.health = 3
        #enemy 2 id
        self.id = 2
    #enemy 2 update at every frame
    def update(self):
        #enemy 2 animation update  
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        #enemy 2 speed/direction
        self.rect.y += 2
        #enemy 2 killed once it leaves screen
        if self.rect.y > 700:
            self.kill()
        #enemy 2 shoot
        self.time_elapsed_since_e2shoot += dt
        if self.time_elapsed_since_e2shoot > 400:
            e2bullet = E2bullet()
            e2bullet.rect.x, e2bullet.rect.y = self.rect.x + 30, self.rect.y + 80
            interactive_objects.add(e2bullet)
            enemy_list.add(e2bullet)
            self.time_elapsed_since_e2shoot = 0
        #enemy 2 killed once health below 0
        if self.health <= 0:
            self.kill()
    #enemy 2 spawn
    def spawn(self):
        self.rect.x = random.randint(-20, 450)
        self.rect.y = -120
        interactive_objects.add(self)
        enemy_list.add(self)
# --- Small Meteor ---
class Smallmeteor(pg.sprite.Sprite):
    def __init__(self):
        #small meteor sprites/animation
        super(Smallmeteor, self).__init__()
        self.images = []
        sprite_size = random.randint(32, 64) #randomize small meteor size
        self.images.append(pg.transform.scale(pg.image.load('space-image_meteor_small_1.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_meteor_small_2.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_meteor_small_3.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_meteor_small_4.png'), (sprite_size, sprite_size)))
        self.index = random.randint(0,3) #randomize starting index(frame) to play
        self.image = self.images[self.index]
        #small meteor position
        self.rect = self.image.get_rect()
        self.x = 200
        self.y = 200
        #small meteor id
        self.id = 0
    #small meteor update at every frame
    def update(self):
        #small meteor animation update        
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        #small meteor speed/direction
        self.rect.y += 4
        #small meteor killed once it leaves screen
        if self.rect.y > 700:
            self.kill()
    #small meteor spawn
    def spawn(self):
        self.rect.x = random.randint(-20, 450)
        self.rect.y = -100    
        interactive_objects.add(self)
        enemy_list.add(self)
# --- Enemy Bullet Classes ---
class E2bullet(pg.sprite.Sprite):
    def __init__(self):
        super(E2bullet, self).__init__()
        #e2bullet sprites/animation
        self.images = []
        self.images.append(pg.transform.scale(pg.image.load('space-image_e2bullet_1.png'), (16, 32)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_e2bullet_2.png'), (16, 32)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_e2bullet_3.png'), (16, 32)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_e2bullet_4.png'), (16, 32)))
        self.index = 0
        self.image = self.images[self.index]
        #e2bullet position
        self.rect = self.image.get_rect()
        #e2bullet id
        self.id = 2.1
        #e2bullet sound
##        pg.mixer.Channel(0).play(pg.mixer.Sound('space-sound_pbullet.wav'))
    #e2bullet update at every frame
    def update(self):
        #e2bullet animation update
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        #e2bullet speed/direction
        self.rect.y += 7
        #e2bullet killed once it leaves screen
        if self.rect.y > 700:
            self.kill()
# --- Visual Effects Classes ---
# --- PowerUp 1 ---
class Powerup1(pg.sprite.Sprite):
    def __init__(self):
        #powerup 1 sprites/animation
        super(Powerup1, self).__init__()
        self.images = []
        self.images.append(pg.transform.scale(pg.image.load('space-image_powerup1_1.png'), (40, 40)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_powerup1_2.png'), (40, 40)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_powerup1_3.png'), (40, 40)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_powerup1_4.png'), (40, 40)))
        self.index = random.randint(0,3) #randomize starting index(frame) to play
        self.image = self.images[self.index]
        #powerup 1 position
        self.rect = self.image.get_rect()
        self.x = 200
        self.y = 200
        #powerup1 id
        self.id = 1
    #powerup 1 update at every frame
    def update(self):
        #powerup 1 animation update        
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        #powerup 1 speed/direction
        self.rect.y += 6
        #powerup 1 killed once it leaves screen
        if self.rect.y > 700:
            self.kill()
    #powerup1 spawn
    def spawn(self):
        self.rect.x = random.randint(0, 500)
        self.rect.y = -100    
        interactive_objects.add(self)
        powerup_list.add(self)
# --- PowerUp 2 ---
class Powerup2(pg.sprite.Sprite):
    def __init__(self):
        #powerup 2 sprites/animation
        super(Powerup2, self).__init__()
        self.images = []
        self.images.append(pg.transform.scale(pg.image.load('space-image_powerup2_1.png'), (40, 40)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_powerup2_2.png'), (40, 40)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_powerup2_3.png'), (40, 40)))
        self.index = random.randint(0,2) #randomize starting index(frame) to play
        self.image = self.images[self.index]
        #powerup 2 position
        self.rect = self.image.get_rect()
        self.x = 200
        self.y = 200
        #powerup2 id
        self.id = 2
    #powerup 2 update at every frame
    def update(self):
        #powerup 2 animation update        
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        #powerup 2 speed/direction
        self.rect.y += 6
        #powerup 2 killed once it leaves screen
        if self.rect.y > 700:
            self.kill()
    #powerup2 spawn
    def spawn(self):
        self.rect.x = random.randint(0, 500)
        self.rect.y = -100    
        interactive_objects.add(self)
        powerup_list.add(self)
# --- Player Explosion ---
class Pex(pg.sprite.Sprite):
    def __init__(self):
        super(Pex, self).__init__()
        #player explosion sprites/animation
        self.images = []
        sprite_size = random.randint(90, 120) #randomize player explosion size
        self.images.append(pg.transform.scale(pg.image.load('space-image_pex_1.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_pex_2.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_pex_3.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_pex_4.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_pex_5.png'), (sprite_size, sprite_size)))
        self.index = 0
        self.image = self.images[self.index]
        #player explosion position
        self.rect = self.image.get_rect()
        #player explosion sound
        pg.mixer.Channel(2).play(pg.mixer.Sound('space-sound_pdamage.wav'))
    #player explosion update at every frame
    def update(self):
        #player explosion animation update
        self.index += 1
        self.image = self.images[self.index]
        #player explosion killed once animation ends
        if self.index == 4:
            self.kill()
# --- Small Explosion ---
class Smallex(pg.sprite.Sprite):
    def __init__(self):
        super(Smallex, self).__init__()
        #small explosion sprites/animation
        self.images = []
        sprite_size = random.randint(56, 96) #randomize small explosion size
        self.images.append(pg.transform.scale(pg.image.load('space-image_smallex_1.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_smallex_2.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_smallex_3.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_smallex_4.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_smallex_5.png'), (sprite_size, sprite_size)))
        self.index = 0
        self.image = self.images[self.index]
        #small explosion position
        self.rect = self.image.get_rect()
        #small explosion sound
        pg.mixer.Channel(3).play(pg.mixer.Sound('space-sound_smallex.wav'))
    #small explosion update at every frame
    def update(self):
        #small explosion animation update
        self.index += 1
        self.image = self.images[self.index]
        #small explosion killed once animation ends
        if self.index == 4:
            self.kill()
# --- Asteroid Explosion ---
class Asteroidex(pg.sprite.Sprite):
    def __init__(self):
        super(Asteroidex, self).__init__()
        #asteroid explosion sprites/animation
        self.images = []
        sprite_size = random.randint(48, 72) #randomize asteroid explosion size
        self.images.append(pg.transform.scale(pg.image.load('space-image_asteroidex_1.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_asteroidex_2.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_asteroidex_3.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_asteroidex_4.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_asteroidex_5.png'), (sprite_size, sprite_size)))
        self.index = 0
        self.image = self.images[self.index]
        #asteroid explosion position
        self.rect = self.image.get_rect()
        #asteroid explosion sound
        pg.mixer.Channel(4).play(pg.mixer.Sound('space-sound_meteorex.wav'))
    #asteroid explosion update at every frame
    def update(self):
        #asteroid explosion animation update
        self.index += 1
        self.image = self.images[self.index]
        #asteroid explosion killed once animation ends
        if self.index == 4:
            self.kill()
# --- Stars ---
class Stars(pg.sprite.Sprite):
    def __init__(self):
        super(Stars, self).__init__()
        #stars sprites/animation
        self.images = []
        sprite_size = random.randint(8, 16) #randomize stars size
        self.images.append(pg.transform.scale(pg.image.load('space-image_stars_1.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_stars_2.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_stars_3.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_stars_4.png'), (sprite_size, sprite_size)))
        self.index = 0
        self.image = self.images[self.index]
        #stars position
        self.rect = self.image.get_rect()
    #stars update at every frame
    def update(self):
        #stars animation update
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        #stars speed/direction
        self.rect.y += 2
        #stars killed once it leaves screen
        if self.rect.y > 700:
            self.kill()
    def spawn(self):
        self.rect.x = random.randint(-20, 450)
        self.rect.y = -100
        noninteractive_objects.add(self)
# --- End Of Classes ---
# --- Miscellaneous Functions ---
def button(text, text_s, text_c, x, y, w, h, ic, ac, action=None):
    """
    Button function!
    Args:
        text: String/Text to be shown on the button
        text_s: Size of the text
        text_c: Color of the text
        x: X coordinate of the text
        y: Y coordinate of the text
        w: Width of the text
        h: Height of the text
        ic: initial color of the text
        ac: alternative color of the text
        action: Call a function if need be
    """
    mouse = pg.mouse.get_pos() #check mouse position
    click = pg.mouse.get_pressed() #check mouse click
    if x + w > mouse[0] > x and y + h > mouse[1] > y: #if mouse position within button position
        pg.draw.rect(screen, ac, (x,y,w,h)) #highlight with alternate color
        if click[0] == 1 and action != None: #on click execution function if applicable
            action()
    else:
        pg.draw.rect(screen, ic, (x,y,w,h)) #else draw with initial color
    buttontext_font = pg.font.SysFont("Comic Sans", text_s) #text font
    text_surface = buttontext_font.render(text, True, text_c) #text surface to draw on
    text_rect = text_surface.get_rect() #check text position
    text_rect.center = ((x+(w/2)), (y+(h/2))) #centralize text
    screen.blit(text_surface, text_rect) #draw text surface onto screen
# --- Main Game Loops ---
# --- Game Intro Loop ---
def game_intro():
    """
    Introductory loop to run when game is first launched.
    Args:
        None
    """
    #create display ship as decoration
    display_list = pg.sprite.Group()
    displayship = Ship()
    displayship.rect.x, displayship.rect.y = 190, 300
    display_list.add(displayship)
    gameintro = True
    while gameintro == True: #loop while gameintro is still running
        for event in pg.event.get():
            if event.type == pg.QUIT: #quit game
                gameintro = False
            mouse = pg.mouse.get_pos() #check mouse position
            if event.type == pg.MOUSEBUTTONDOWN and 298 > mouse[0] > 198 and 450 > mouse[1] > 400: #start game
                displayship.kill()
                gameintro = False
                gamemodeselect = True
            if event.type == pg.MOUSEBUTTONDOWN and 298 > mouse[0] > 198 and 510 > mouse[1] > 460: #quit game
                gameintro = False
                gamemodeselect = False
        # --- Draw The Screen ---
        screen.fill((0,0,0))
        button("Start", 32, (255, 255, 255), 198, 400, 100, 50, dark_green, green)
        button("Quit", 32, (255, 255, 255), 198, 460, 100, 50, dark_red, red)
        gameintro_text1 = gameintro_text1_font.render("Welcome to", True, white)
        gameintro_text2 = gameintro_text2_font.render("Space Ships!", True, yellow)
        display_list.update()
        display_list.draw(screen)
        screen.blit(gameintro_text1, (167, 200))
        screen.blit(gameintro_text2, (97, 250))
        pg.display.flip()
        clock.tick(24)
    #initial highscore set to 0
    highscore = 0
    #launch to gamemode select/exit game base on choice
    if gamemodeselect == True:
        gamemode_select(gamemodeselect, highscore)
    if gamemodeselect == False:
        pg.quit()
        sys.exit()
def gamemode_select(gamemodeselect, highscore):
    """
    Game loop that runs when selecting gamemode
    Args:
        gamemodeselect: Loop if true
        highscore: Check and include previous attempt highscores if applicable
    """
    #create test ships for players to try out controls
    global test_list
    test_list = pg.sprite.Group()
    testship = Ship()
    testship2 = Ship()
    testship.rect.x, testship.rect.y = 190, 170
    testship2.rect.x, testship2.rect.y = 190, 315
    test_list.add(testship)
    test_list.add(testship2)
    gamemodeselect = True
    while gamemodeselect == True: #loop while gamemodeselect is still running
        for event in pg.event.get():
            if event.type == pg.QUIT: #quit game
                gamemodeselect = False
                gameplay = False
            mouse = pg.mouse.get_pos() #check mouse position
            if event.type == pg.MOUSEBUTTONDOWN and 348 > mouse[0] > 148 and 450 > mouse[1] > 400: #gamemode 1
                gamemode = 1
                gamemodeselect = False
                gameplay = True
            if event.type == pg.MOUSEBUTTONDOWN and 348 > mouse[0] > 148 and 510 > mouse[1] > 460: #gamemode 2
                gamemode = 2
                gamemodeselect = False
                gameplay = True
        keypressed = pg.key.get_pressed()
        if keypressed[pg.K_LEFT]: #player1 movement to left
            testship.moveLeft(5)
        if keypressed[pg.K_RIGHT]: #player1 movement to right
            testship.moveRight(5)
        if keypressed[pg.K_KP3] and testship.health > 0: #player1 shoot
            testship.testshoot()
        if keypressed[pg.K_a]: #player2 movement to left
            testship2.moveLeft(5)
        if keypressed[pg.K_d]: #player2 movement to right
            testship2.moveRight(5)
        if keypressed[pg.K_SPACE] and testship2.health > 0: #player2 shoot
            testship2.testshoot()
        # --- Draw The Screen ---
        screen.fill((0,0,0))
        button("Single Player", 32, (255, 255, 255), 148, 400, 200, 50, dark_green, green)
        button("Two Player", 32, (255, 255, 255), 148, 460, 200, 50, dark_green, green)
        gamemodeselect_text1 = gamemodeselect_text1_font.render("Controls", True, yellow)
        gamemodeselect_text2 = gamemodeselect_instruction1_font.render("Single Player", True, white)
        gamemodeselect_text3 = gamemodeselect_instruction1_font.render("Two Player", True, white)
        gamemodeselect_text4 = gamemodeselect_instruction2_font.render("<- Left Arrow                Right Arrow ->", True, white)
        gamemodeselect_text5 = gamemodeselect_instruction2_font.render("<- A                D ->", True, white)
        gamemodeselect_text6 = gamemodeselect_instruction2_font.render("Space                   Bar", True, white)
        gamemodeselect_text7 = gamemodeselect_instruction2_font.render("Num                   3", True, white)
        gamemodeselect_text8 = gamemodeselect_instruction3_font.render("MOVE", True, green)
        gamemodeselect_text9 = gamemodeselect_instruction3_font.render("MOVE", True, green)
        gamemodeselect_text10 = gamemodeselect_instruction3_font.render("SHOOT", True, green)
        gamemodeselect_text11 = gamemodeselect_instruction3_font.render("SHOOT", True, green)
        test_list.update()
        test_list.draw(screen)
        screen.blit(gamemodeselect_text1, (167, 50))
        screen.blit(gamemodeselect_text2, (190, 100))
        screen.blit(gamemodeselect_text3, (195, 245))
        screen.blit(gamemodeselect_text4, (107, 125))
        screen.blit(gamemodeselect_text5, (175, 270))
        screen.blit(gamemodeselect_text6, (160, 150))
        screen.blit(gamemodeselect_text7, (163, 295))
        screen.blit(gamemodeselect_text8, (218, 125))
        screen.blit(gamemodeselect_text9, (218, 270))
        screen.blit(gamemodeselect_text10, (215, 150))
        screen.blit(gamemodeselect_text11, (215, 295))
        pg.display.flip()
        clock.tick(60)
    #launch gameplay/exit game base on choice
    if gameplay == True:
        game_play(gameplay, highscore, gamemode)
    if gameplay == False:
        pg.quit()
        sys.exit()
# --- Game Play Loop ---
def game_play(gameplay, highscore, gamemode):
    """
    Game loop that runs during actual gameplay.
    Args:
        gameplay: Loop if true
        highscore: Check and include previous attempt highscores if applicable
        gamemode: Check gamemode (single or two player)
    """
    # --- Initial Setup ---
    # --- Sprite Groups Generation ---
    global interactive_objects, noninteractive_objects, bullet_list, opbullet_list, enemy_list, powerup_list #main lists for interactions
    interactive_objects = pg.sprite.Group()
    noninteractive_objects = pg.sprite.Group()
    enemy_list = pg.sprite.Group()
    player_list = pg.sprite.Group()
    bullet_list = pg.sprite.Group()
    opbullet_list = pg.sprite.Group()
    plife_list = pg.sprite.Group()
    powerup_list = pg.sprite.Group()
    # --- Player/Player Life Generation ---
    #player1 creation
    ship = Ship()
    player_list.add(ship)
    interactive_objects.add(ship)
    playerlife1 = Playerlife()
    playerlife2 = Playerlife()
    playerlife3 = Playerlife()
    playerlife1.rect.x, playerlife1.rect.y = 420, 20
    playerlife2.rect.x, playerlife2.rect.y = 440, 20
    playerlife3.rect.x, playerlife3.rect.y = 460, 20
    plife_list.add(playerlife1)
    plife_list.add(playerlife2)
    plife_list.add(playerlife3)
    noninteractive_objects.add(playerlife1)
    noninteractive_objects.add(playerlife2)
    noninteractive_objects.add(playerlife3)
    #player2 creation in 2 player mode
    if gamemode == 2:
        ship.rect.x, ship.rect.y = 125, 600 #shifts player1 position to accommodate player2
        ship2 = Ship()
        ship2.rect.x, ship2.rect.y = 275, 600
        player_list.add(ship2)
        interactive_objects.add(ship2)
        player2life1 = Playerlife()
        player2life2 = Playerlife()
        player2life3 = Playerlife()
        player2life1.rect.x, playerlife1.rect.y = 420, 40
        player2life2.rect.x, playerlife2.rect.y = 440, 40
        player2life3.rect.x, playerlife3.rect.y = 460, 40
        plife_list.add(player2life1)
        plife_list.add(player2life2)
        plife_list.add(player2life3)
        noninteractive_objects.add(player2life1)
        noninteractive_objects.add(player2life2)
        noninteractive_objects.add(player2life3)
    # --- Time/Score Generation ---
    score = 0
    time_elapsed_since_e1spawn = 0
    time_elapsed_since_smallmeteorspawn = 0
    time_elapsed_since_bigmeteorspawn = 0
    time_elapsed_since_starsspawn = 0
    time_elapsed_since_powerup1spawn = 0
    time_elapsed_since_powerup2spawn = 0
    time_elapsed_since_e2spawn = 0
    time_elapsed_since_score = 0
    time_elapsed_since_start = 0
    gameplay = True
    while gameplay == True: #loop while gameplay is still running
        for event in pg.event.get():
            if event.type == pg.QUIT: #quit game
                gameplay = False
        # --- Player Management ---
        keypressed = pg.key.get_pressed()
        #single player controls
        if gamemode == 1:
            if keypressed[pg.K_LEFT]: #player1 movement to left
                ship.moveLeft(5)
            if keypressed[pg.K_RIGHT]: #player1 movement to right
                ship.moveRight(5)
            if keypressed[pg.K_SPACE] and ship.health > 0: #player1 shoot
                ship.shoot()
        #two player controls
        if gamemode == 2:
            if keypressed[pg.K_LEFT]: #player1 movement to left
                ship.moveLeft(5)
            if keypressed[pg.K_RIGHT]: #player1 movement to right
                ship.moveRight(5)
            if keypressed[pg.K_KP3] and ship.health > 0: #player1 shoot
                ship.shoot()
            if keypressed[pg.K_a]: #player2 movement to left
                ship2.moveLeft(5)
            if keypressed[pg.K_d]: #player2 movement to right
                ship2.moveRight(5)
            if keypressed[pg.K_SPACE] and ship2.health > 0: #player2 shoot
                ship2.shoot()
        # --- Score Increment Management ---
        time_elapsed_since_score += dt #score increase
        if time_elapsed_since_score > 49:
            score+=1
            time_elapsed_since_score = 0
        # --- Spawn Time Management ---
        time_elapsed_since_start += dt
        starsspawntime = random.randint(75,105)
        smallmeteorspawntime = random.randint(600, 750)
        powerup1spawntime = random.randint(55000, 60000)
        powerup2spawntime = random.randint(85000, 90000)
        if time_elapsed_since_start < 60000:
            e1spawntime = random.randint(900, 1100)
            e2spawntime = random.randint(3000, 4000)
        elif time_elapsed_since_start >= 60000 and time_elapsed_since_start < 120000:
            e1spawntime = random.randint(900, 1000)
            e2spawntime = random.randint(2500, 3500)
        elif time_elapsed_since_start >= 120000:
            e1spawntime = random.randint(700, 850)
            e2spawntime = random.randint(2000, 2500)
        # --- Character Spawn Management ---
        time_elapsed_since_starsspawn += dt #stars spawn
        if time_elapsed_since_starsspawn > starsspawntime:
            stars = Stars()
            stars.spawn()
            time_elapsed_since_starsspawn = 0
        time_elapsed_since_e1spawn += dt #enemy 1 spawn
        if time_elapsed_since_e1spawn > e1spawntime:
            e1 = Enemy1()
            e1.spawn()
            time_elapsed_since_e1spawn = 0
        time_elapsed_since_e2spawn += dt #enemy 2 spawn
        if time_elapsed_since_e2spawn > e2spawntime:
            e2 = Enemy2()
            e2.spawn()
            time_elapsed_since_e2spawn = 0
        time_elapsed_since_smallmeteorspawn += dt #small meteor spawn
        if time_elapsed_since_smallmeteorspawn > smallmeteorspawntime:
            smallmeteor = Smallmeteor()
            smallmeteor.spawn()
            time_elapsed_since_smallmeteorspawn = 0
        time_elapsed_since_powerup1spawn += dt #powerup 1 spawn
        if time_elapsed_since_powerup1spawn > powerup1spawntime:
            powerup1 = Powerup1()
            powerup1.spawn()
            time_elapsed_since_powerup1spawn = 0
        time_elapsed_since_powerup2spawn += dt #powerup 2 spawn
        if time_elapsed_since_powerup2spawn > powerup2spawntime:
            powerup2 = Powerup2()
            powerup2.spawn()
            time_elapsed_since_powerup2spawn = 0
        # --- Collision Management ---
        # --- Bullet Collision with Enemy ---
        for enemy in enemy_list:
            enemyhits = pg.sprite.spritecollide(enemy, bullet_list, True)
            enemyhitsop = pg.sprite.spritecollide(enemy, opbullet_list, False)
            if (enemyhits or enemyhitsop) and (enemy.id == 0 or enemy.id == 2.1): #collision with enemy that has health = 1
                asteroidex = Asteroidex()
                asteroidex.rect.x = enemy.rect.x
                asteroidex.rect.y = enemy.rect.y
                interactive_objects.add(asteroidex)
                enemy.kill()
            elif (enemyhits or enemyhitsop) and (enemy.id == 1 or enemy.id == 2): #collision with enemy that has health > 1
                smallex = Smallex()
                smallex.rect.x = enemy.rect.x
                smallex.rect.y = enemy.rect.y
                interactive_objects.add(smallex)
                enemy.health -= 1
        # --- Player Collision with Enemy ---
        for player in player_list:
            playerhits = pg.sprite.spritecollide(player, enemy_list, True)
            if playerhits:
                pex = Pex()
                pex.rect.center = player.rect.center
                interactive_objects.add(pex)
                player.health -= 1
        # --- Player Collision with Power Up ---
        for powerup in powerup_list:
            poweruphits = pg.sprite.spritecollide(powerup, player_list, False)
            if poweruphits and powerup.id == 1:
                ship.consume()
                ship.powerupvalue = 1
                powerup.kill()
                #player2 gets powerup too in 2 player mode
                if gamemode == 2:
                    ship2.consume()
                    ship2.powerupvalue = 1
                    powerup.kill()
            elif poweruphits and powerup.id == 2:
                ship.consume()
                ship.powerupvalue = 2
                powerup.kill()
                #player2 gets powerup too in 2 player mode
                if gamemode == 2:
                    ship2.consume()
                    ship2.powerupvalue = 2
                    powerup.kill()
        # --- Player Life Management ---
        #player1 life management
        if ship.health == 2:
            playerlife1.kill()
        if ship.health == 1:
            playerlife2.kill()
        if ship.health <= 0:
            playerlife3.kill()
            ship.kill()
        #player2 life management in 2 player mode
        if gamemode == 2:
            if ship2.health == 2:
                player2life1.kill()
            if ship2.health == 1:
                player2life2.kill()
            if ship2.health <= 0:
                player2life3.kill()
                ship2.kill()
        # --- Updates/Draw The Screen ---
        screen.fill((0,0,0))
        noninteractive_objects.update()
        noninteractive_objects.draw(screen)
        interactive_objects.update()
        interactive_objects.draw(screen)
        plife_list.update()
        plife_list.draw(screen)
        if ship.powerupvalue > 0: #update player1 powerup if powerup is active
            ship.powerup()
        if gamemode == 2:
            if ship2.powerupvalue > 0: #update player2 powerup if powerup is active
                ship2.powerup()
        highscoreboard = score_font.render("High Score: " + str(highscore), True, white)
        scoreboard = score_font.render("Score: " + str(score), True, white)
        screen.blit(scoreboard, (20, 50))
        screen.blit(highscoreboard, (20, 20))
        pg.display.flip()
        clock.tick(60) #fps
        # --- Game Over Management ---
        #gameover condition for single player mode
        if gamemode == 1:
            if ship.health <= 0:
                gameplay = False
        #gameover condition for 2 player mode
        if gamemode == 2:
            if ship.health <= 0 and ship2.health <= 0:
                gameplay = False
    game_over(score, highscore)
# --- Game Over Loop ---
def game_over(score, highscore):
    """
    End loop that runs once game is over.
    Args:
        score: takes in current score
        highscore: takes in previous highscore to check against current score for new highscore
    """
    gameover = True
    while gameover == True: #loop while gameover is still running
        for event in pg.event.get():
            if event.type == pg.QUIT: #quit game
                gamemodeselect = False
                gameover = False
            mouse = pg.mouse.get_pos()
            if event.type == pg.MOUSEBUTTONDOWN and 230 > mouse[0] > 80 and 450 > mouse[1] > 400: #restart game
                gamemodeselect = True
                gameover = False
            if event.type == pg.MOUSEBUTTONDOWN and 430 > mouse[0] > 280 and 450 > mouse[1] > 400: #quit game
                gamemodeselect = False
                gameover = False
        # --- Draw The Screen ---       
        screen.fill((0,0,0))
        button("Play Again", 32, (255, 255, 255), 80, 400, 150, 50, dark_green, green)
        button("Quit", 32, (255, 255, 255), 280, 400, 150, 50, dark_red, red)
        gameover_text = gameover_text_font.render("Game Over!", True, red)
        gameover_text2 = gameover_text2_font.render("Your High Score is:", True, white)
        gameover_text3 = gameover_text3_font.render(str(score), True, yellow)
        screen.blit(gameover_text, (110, 200))
        screen.blit(gameover_text2, (155, 300))
        screen.blit(gameover_text3, (240, 350))
        # --- New High Score Management ---
        if score > highscore:
            highscore_text = highscore_text_font.render("You set a new highscore!", True, green)
            screen.blit(highscore_text, (50, 500))
        pg.display.flip()
    # --- Restart/Quit Management ---
    if score > highscore:
        highscore = score
    if gamemodeselect == True:
        gamemode_select(gamemodeselect, highscore)
    if gamemodeselect == False:
        pg.quit()
        sys.exit()
# --- General Set Up ---
clock = pg.time.Clock()
screen_x = 500
screen_y = 700
screen = pg.display.set_mode((screen_x, screen_y))
pg.display.set_caption("SpaceShips!")
# --- Fonts to be used ---
score_font = pg.font.SysFont("Times", 24)
gameintro_text1_font = pg.font.SysFont("Calibri", 32)
gameintro_text2_font = pg.font.SysFont("Comic Sans", 72)
gamemodeselect_text1_font = pg.font.SysFont("Comic Sans", 64)
gamemodeselect_instruction1_font = pg.font.SysFont("Calibri", 24)
gamemodeselect_instruction2_font = pg.font.SysFont("Times", 18)
gamemodeselect_instruction3_font = pg.font.SysFont("Comic Sans", 28)
gameover_text_font = pg.font.SysFont("Comic Sans", 72)
gameover_text2_font = pg.font.SysFont("Times", 24)
gameover_text3_font = pg.font.SysFont("Times", 30)
highscore_text_font = pg.font.SysFont("Times", 40)
# --- Colors to be used ---
white = (255, 255, 255)
red = (255, 0, 0)
dark_red = (102, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
dark_green = (0, 102, 0)
# --- Start ---
dt = 16.666 #1 second approximately 1000 ticks
game_intro()

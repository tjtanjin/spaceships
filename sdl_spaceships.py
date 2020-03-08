import sys, json, os
import pygame as pg
import random
from pygame.sdlmain_osx import InstallNSApplication
InstallNSApplication()
pg.init()
# --- Player-Related Classes ---
# --- Player Space Ship ---
class Ship(pg.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__()
        #player sprites/animation
        self.images = []
        self.images.append(pg.image.load('./Images/space-image_ship_1.png'))
        self.images.append(pg.image.load('./Images/space-image_ship_2.png'))
        self.images.append(pg.image.load('./Images/space-image_ship_3.png'))
        self.images.append(pg.image.load('./Images/space-image_ship_4.png'))
        self.images.append(pg.image.load('./Images/space-image_ship_5.png'))
        self.images.append(pg.image.load('./Images/space-image_ship_6.png'))
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
        self.time_elapsed_since_powerup4 = 0
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
        if self.time_elapsed_since_pshoot >= 140 and self.powerupvalue == 0: #player shoot with no powerup
            bullet = Bullet()
            bullet.rect.x, bullet.rect.y = self.rect.x + 30, self.rect.y + 10
            interactive_objects.add(bullet)
            bullet_list.add(bullet)
            bullet = Bullet()
            bullet.rect.x, bullet.rect.y = self.rect.x + 80, self.rect.y + 10
            interactive_objects.add(bullet)
            bullet_list.add(bullet)
            self.time_elapsed_since_pshoot = 0
        elif self.time_elapsed_since_pshoot >= 140 and self.powerupvalue == 1: #player shoot with powerup1
            bullet = Bullet()
            bullet.rect.x, bullet.rect.y = self.rect.x + 30, self.rect.y + 10
            interactive_objects.add(bullet)
            bullet_list.add(bullet)
            bullet = Bullet()
            bullet.rect.x, bullet.rect.y = self.rect.x + 80, self.rect.y + 10
            interactive_objects.add(bullet)
            bullet_list.add(bullet)
            bullet = Bullet()
            bullet.rect.x, bullet.rect.y = self.rect.x + 55, self.rect.y - 15
            interactive_objects.add(bullet)
            bullet_list.add(bullet)
            self.time_elapsed_since_pshoot = 0
        elif self.time_elapsed_since_pshoot >= 160 and self.powerupvalue == 2: #player shoot with powerup2
            pbullet2 = Pbullet2()
            pbullet2.rect.x, pbullet2.rect.y = self.rect.x + 31, self.rect.y - 620
            interactive_objects.add(pbullet2)
            opbullet_list.add(pbullet2)
            pbullet2 = Pbullet2()
            pbullet2.rect.x, pbullet2.rect.y = self.rect.x + 81, self.rect.y - 620
            interactive_objects.add(pbullet2)
            opbullet_list.add(pbullet2)
            self.time_elapsed_since_pshoot = 0
        elif self.time_elapsed_since_pshoot >= 140 and self.powerupvalue == 4: #player shoot with powerup4
            bullet = Bullet()
            bullet.rect.x, bullet.rect.y = self.rect.x + 30, self.rect.y + 10
            interactive_objects.add(bullet)
            bullet_list.add(bullet)
            bullet = Bullet()
            bullet.rect.x, bullet.rect.y = self.rect.x + 80, self.rect.y + 10
            interactive_objects.add(bullet)
            bullet_list.add(bullet)
            self.time_elapsed_since_pshoot = 0
            pbullet4 = Pbullet4()
            pbullet4.rect.x, pbullet4.rect.y = self.rect.x + 15, self.rect.y + 22
            interactive_objects.add(pbullet4)
            bullet_list.add(pbullet4)
            pbullet4 = Pbullet4()
            pbullet4.rect.x, pbullet4.rect.y = self.rect.x + 95, self.rect.y + 22
            interactive_objects.add(pbullet4)
            bullet_list.add(pbullet4)
            self.time_elapsed_since_pshoot = 0
    #player test shoot (on gamemode select screen)
    def testshoot(self):
        if self.time_elapsed_since_pshoot >= 140: #player test shoot in gamemode select screen
            bullet = Bullet()
            bullet.rect.x, bullet.rect.y = self.rect.x + 30, self.rect.y + 10
            test_list.add(bullet)
            bullet = Bullet()
            bullet.rect.x, bullet.rect.y = self.rect.x + 80, self.rect.y + 10
            test_list.add(bullet)
            self.time_elapsed_since_pshoot = 0
    #player powerups
    def powerup(self):
        if self.powerupvalue == 1: #powerup1
            self.time_elapsed_since_powerup2 = 0 #reset other active powerups
            self.time_elapsed_since_powerup4 = 0
            self.time_elapsed_since_powerup1 += dt
            if self.time_elapsed_since_powerup1 > 9000: #powerup1 duration (9sec)
                self.powerupvalue = 0
                self.time_elapsed_since_powerup1 = 0
        if self.powerupvalue == 2: #powerup2
            self.time_elapsed_since_powerup1 = 0 #reset other active powerups
            self.time_elapsed_since_powerup4 = 0
            self.time_elapsed_since_powerup2 += dt
            if self.time_elapsed_since_powerup2 > 7000: #powerup2 duration (7sec)
                self.powerupvalue = 0
                self.time_elapsed_since_powerup2 = 0
        if self.powerupvalue == 4: #powerup4
            self.time_elapsed_since_powerup1 = 0 #reset other active powerups
            self.time_elapsed_since_powerup2 = 0
            self.time_elapsed_since_powerup4 += dt
            if self.time_elapsed_since_powerup4 > 6000: #powerup4 duration (6sec)
                self.powerupvalue = 0
                self.time_elapsed_since_powerup4 = 0
    #sound played when player receives attack powerup
    def consume(self):
        pg.mixer.Channel(0).play(pg.mixer.Sound('./Sound/space-sound_powerup.wav'))
    #sound played when player receives healthpack
    def heal(self):
        pg.mixer.Channel(9).play(pg.mixer.Sound('./Sound/space-sound_heal.wav'))
# --- Player 2 Space Ship ---
#methods inherited from Ship() class with the difference being in sprites
class Ship2(Ship):
    def __init__(self):
        super(Ship2, self).__init__()
        #player2 sprites/animation
        self.images = []
        self.images.append(pg.image.load('./Images/space-image_ship2_1.png'))
        self.images.append(pg.image.load('./Images/space-image_ship2_2.png'))
        self.images.append(pg.image.load('./Images/space-image_ship2_3.png'))
        self.images.append(pg.image.load('./Images/space-image_ship2_4.png'))
        self.images.append(pg.image.load('./Images/space-image_ship2_5.png'))
        self.images.append(pg.image.load('./Images/space-image_ship2_6.png'))
        self.index = 0
        self.image = self.images[self.index]
# --- Player Main Bullet ---
class Bullet(pg.sprite.Sprite):
    def __init__(self):
        super(Bullet, self).__init__()
        #player bullet sprites/animation
        self.images = []
        self.images.append(pg.image.load('./Images/space-image_pbullet_1.png'))
        self.images.append(pg.image.load('./Images/space-image_pbullet_2.png'))
        self.images.append(pg.image.load('./Images/space-image_pbullet_3.png'))
        self.images.append(pg.image.load('./Images/space-image_pbullet_4.png'))
        self.images.append(pg.image.load('./Images/space-image_pbullet_5.png'))
        self.images.append(pg.image.load('./Images/space-image_pbullet_6.png'))
        self.index = 0
        self.image = self.images[self.index]
        #player bullet position
        self.rect = self.image.get_rect()
        #player bullet sound
        pg.mixer.Channel(1).play(pg.mixer.Sound('./Sound/space-sound_pbullet.wav'))
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
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_pbullet2_1.png'), (3, 650)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_pbullet2_2.png'), (3, 650)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_pbullet2_3.png'), (3, 650)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_pbullet2_4.png'), (3, 650)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_pbullet2_5.png'), (3, 650)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_pbullet2_6.png'), (3, 650)))
        self.index = 0
        self.image = self.images[self.index]
        #pbullet2  position
        self.rect = self.image.get_rect()
        #pbullet2 specific initial timer set to 0
        self.time_elapsed_since_pshoot2 = 0
        #pbullet2 sound
        pg.mixer.Channel(6).play(pg.mixer.Sound('./Sound/space-sound_pbullet2.wav'))
    #pbullet2 update at every frame
    def update(self):
        #pbullet2 animation update
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        #pbullet2 removed every 160 ticks to simulate tracing laser
        self.time_elapsed_since_pshoot2 += dt
        if self.time_elapsed_since_pshoot2 > 160:
            self.kill()
            self.time_elapsed_since_pshoot2 = 0
# --- Player Power Up 4 Bullet ---
class Pbullet4(pg.sprite.Sprite):
    def __init__(self):
        super(Pbullet4, self).__init__()
        #pbullet4 sprites/animation
        self.images = []
        self.images.append(pg.image.load('./Images/space-image_pbullet4_1.png'))
        self.images.append(pg.image.load('./Images/space-image_pbullet4_2.png'))
        self.images.append(pg.image.load('./Images/space-image_pbullet4_3.png'))
        self.images.append(pg.image.load('./Images/space-image_pbullet4_4.png'))
        self.images.append(pg.image.load('./Images/space-image_pbullet4_5.png'))
        self.images.append(pg.image.load('./Images/space-image_pbullet4_6.png'))
        self.index = 0
        self.image = self.images[self.index]
        #pbullet4 position
        self.rect = self.image.get_rect()
        #pbullet4 sound
        pg.mixer.Channel(1).play(pg.mixer.Sound('./Sound/space-sound_pbullet.wav'))
    #pbullet4 update at every frame
    def update(self):
        #pbullet4 animation update
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        #pbullet4 speed/direction
        self.rect.y -= 7
        #pbullet4 killed once it leaves screen
        if self.rect.y < 0:
            self.kill()
# --- Player 1 Life Display ---
class Playerlife(pg.sprite.Sprite):
    def __init__(self):
        super(Playerlife, self).__init__()
        #player life display sprites/animation
        self.images = []
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_plife.png'), (60, 36)))
        self.index = 0
        self.image = self.images[self.index]
        #player life display position
        self.rect = self.image.get_rect()
    #player life display update at every frame
    def update(self):
        None
# --- Player 2 Life Display ---
#methods inherited from Playerlife() class with the difference being in sprites
class Player2life(Playerlife):
    def __init__(self):
        super(Player2life, self).__init__()
        #player2 life display sprites/animation
        self.images = []
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_p2life.png'), (60, 36)))
        self.index = 0
        self.image = self.images[self.index]
# --- Power Up Classes ---
# --- PowerUp 1 ---
class Powerup1(pg.sprite.Sprite):
    def __init__(self):
        #powerup1 sprites/animation
        super(Powerup1, self).__init__()
        self.images = []
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_powerup1_1.png'), (40, 40)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_powerup1_2.png'), (40, 40)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_powerup1_3.png'), (40, 40)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_powerup1_4.png'), (40, 40)))
        self.index = random.randint(0,3) #randomize starting index(frame) to play
        self.image = self.images[self.index]
        #powerup1 position
        self.rect = self.image.get_rect()
        #powerup1 id
        self.id = 1
    #powerup1 update at every frame
    def update(self):
        #powerup1 animation update        
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        #powerup1 speed/direction
        self.rect.y += 6
        #powerup1 killed once it leaves screen
        if self.rect.y > screen_y:
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
        #powerup2 sprites/animation
        super(Powerup2, self).__init__()
        self.images = []
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_powerup2_1.png'), (40, 40)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_powerup2_2.png'), (40, 40)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_powerup2_3.png'), (40, 40)))
        self.index = random.randint(0,2) #randomize starting index(frame) to play
        self.image = self.images[self.index]
        #powerup2 position
        self.rect = self.image.get_rect()
        #powerup2 id
        self.id = 2
    #powerup2 update at every frame
    def update(self):
        #powerup2 animation update        
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        #powerup2 speed/direction
        self.rect.y += 6
        #powerup2 killed once it leaves screen
        if self.rect.y > screen_y:
            self.kill()
    #powerup2 spawn
    def spawn(self):
        self.rect.x = random.randint(0, 500)
        self.rect.y = -100    
        interactive_objects.add(self)
        powerup_list.add(self)
# --- PowerUp 3 ---
class Powerup3(pg.sprite.Sprite):
    def __init__(self):
        #powerup3 sprites/animation
        super(Powerup3, self).__init__()
        self.images = []
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_powerup3_1.png'), (40, 40)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_powerup3_2.png'), (40, 40)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_powerup3_3.png'), (40, 40)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_powerup3_4.png'), (40, 40)))
        self.index = random.randint(0,3) #randomize starting index(frame) to play
        self.image = self.images[self.index]
        #powerup3 position
        self.rect = self.image.get_rect()
        #powerup3 id
        self.id = 3
    #powerup3 update at every frame
    def update(self):
        #powerup3 animation update        
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        #powerup3 speed/direction
        self.rect.y += 6
        #powerup3 killed once it leaves screen
        if self.rect.y > screen_y:
            self.kill()
    #powerup3 spawn
    def spawn(self):
        self.rect.x = random.randint(0, 500)
        self.rect.y = -100    
        interactive_objects.add(self)
        powerup_list.add(self)
# --- PowerUp 4 ---
class Powerup4(pg.sprite.Sprite):
    def __init__(self):
        #powerup4 sprites/animation
        super(Powerup4, self).__init__()
        self.images = []
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_powerup4_1.png'), (40, 40)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_powerup4_2.png'), (40, 40)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_powerup4_3.png'), (40, 40)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_powerup4_4.png'), (40, 40)))
        self.index = random.randint(0,3) #randomize starting index(frame) to play
        self.image = self.images[self.index]
        #powerup4 position
        self.rect = self.image.get_rect()
        #powerup4 id
        self.id = 4
    #powerup4 update at every frame
    def update(self):
        #powerup4 animation update        
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        #powerup4 speed/direction
        self.rect.y += 6
        #powerup4 killed once it leaves screen
        if self.rect.y > screen_y:
            self.kill()
    #powerup4 spawn
    def spawn(self):
        self.rect.x = random.randint(0, 500)
        self.rect.y = -100    
        interactive_objects.add(self)
        powerup_list.add(self)
# --- Boss Enemy-Related Classes ---
# --- Boss Enemy 1 ---
class Bossenemy1(pg.sprite.Sprite):
    def __init__(self):
        super(Bossenemy1, self).__init__()
        #bossenemy1 sprites/animation
        self.images = []
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_boss1_1.png'), (417, 227)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_boss1_2.png'), (417, 227)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_boss1_3.png'), (417, 227)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_boss1_4.png'), (417, 227)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_boss1_5.png'), (417, 227)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_boss1_6.png'), (417, 227)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_boss1_7.png'), (417, 227)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_boss1_8.png'), (417, 227)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_boss1_9.png'), (417, 227)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_boss1_10.png'), (417, 227)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_boss1_11.png'), (417, 227)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_boss1_12.png'), (417, 227)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_boss1_13.png'), (417, 227)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_boss1_14.png'), (417, 227)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_boss1_15.png'), (417, 227)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_boss1_16.png'), (417, 227)))
        self.index = random.randint(0,7) #randomize starting index(frame) to play
        self.image = self.images[self.index]
        #bossenemy1 position
        self.rect = self.image.get_rect()
        #bossenemy1 specific initial timer set to 0
        self.time_elapsed_since_b1shoot1 = 0
        self.time_elapsed_since_b1shoot2 = 0
        self.time_elapsed_since_b1spawnenemy = 0
        #bossenemy1 initial health count
        self.initialhealth = 150
        #bossenemy1 actual health count
        self.health = 150
        #bossenemy1 id
        self.id = 100
        #bossenemy1 movement
        change_value = [-1,1]
        self.changex = random.choice(change_value)
        self.changey = 1
    #bossenemy1 update at every frame
    def update(self):
        #bossenemy1 animation update
        self.index += 1
        if self.health > self.initialhealth*0.46:
            if self.index >= 7:
                self.index = 0
        if self.health <= self.initialhealth*0.46:
            if self.index >= 15:
                self.index = 8
        self.image = self.images[self.index]
        #bossenemy1 speed/direction
        if self.rect.y < 0:
            self.rect.y += self.changey
        self.rect.x += self.changex
        self.rect.y += self.changey
        if self.rect.x <= 0 or self.rect.x >= 83:
            self.changex *= -1
        if self.rect.y == 0 or self.rect.y == 80:
            self.changey *= -1
        #bossenemy1 shoot
        self.time_elapsed_since_b1shoot1 += dt
        if self.time_elapsed_since_b1shoot1 > 650: #4 side guns
            b1bullet = Ebullet()
            b1bullet.rect.x, b1bullet.rect.y = self.rect.x + 74, self.rect.y + 200
            interactive_objects.add(b1bullet)
            enemy_list.add(b1bullet)
            b1bullet = Ebullet()
            b1bullet.rect.x, b1bullet.rect.y = self.rect.x + 122, self.rect.y + 200
            interactive_objects.add(b1bullet)
            enemy_list.add(b1bullet)
            b1bullet = Ebullet()
            b1bullet.rect.x, b1bullet.rect.y = self.rect.x + 328, self.rect.y + 200
            interactive_objects.add(b1bullet)
            enemy_list.add(b1bullet)
            b1bullet = Ebullet()
            b1bullet.rect.x, b1bullet.rect.y = self.rect.x + 280, self.rect.y + 200
            interactive_objects.add(b1bullet)
            enemy_list.add(b1bullet)
            self.time_elapsed_since_b1shoot1 = 0
        self.time_elapsed_since_b1shoot2 += dt
        if self.health <= self.initialhealth*0.33 and self.time_elapsed_since_b1shoot2 > 160: #main gun triggered below certain health
            b1bullet2 = Ebullet2()
            b1bullet2.rect.x, b1bullet2.rect.y = self.rect.x + 202, self.rect.y + 220
            interactive_objects.add(b1bullet2)
            enemyopbullet_list.add(b1bullet2)
            self.time_elapsed_since_b1shoot2 = 0
        #bossenemy1 spawn enemies
        self.time_elapsed_since_b1spawnenemy += dt
        if self.time_elapsed_since_b1spawnenemy > 6500:
            e2 = Enemy2() #spawn enemy2
            e2.rect.x = 65
            e2.rect.y = 50
            interactive_objects.add(e2)
            enemy_list.add(e2)
            e2 = Enemy2() #spawn enemy2
            e2.rect.x = 352
            e2.rect.y = 50
            interactive_objects.add(e2)
            enemy_list.add(e2)
            self.time_elapsed_since_b1spawnenemy = 0
        #bossenemy1 killed once health below 0
        if self.health <= 0:
            self.kill()
    #bossenemy1 spawn
    def spawn(self):
        self.rect.x = 41.5
        self.rect.y = -225
        interactive_objects.add(self)
        bossenemy_list.add(self)
# --- Boss Enemy 2 ---
#methods inherited from Bossenemy1() class with the difference being in health, bullet speed and enemy2 spawn speed
class Bossenemy2(Bossenemy1):
    def __init__(self):
        super(Bossenemy2, self).__init__()
        #bossenemy2 initial health count
        self.initialhealth = 175
        #bossenemy2 actual health count
        self.health = 175
        #bossenemy2 set initial timer
        self.time_elapsed_since_b2spawn = 0 #regeneration timer
    def update(self):
        #bossenemy2 animation update
        self.index += 1
        if self.health > self.initialhealth*0.46:
            if self.index >= 7:
                self.index = 0
        if self.health <= self.initialhealth*0.46:
            if self.index >= 15:
                self.index = 8
        self.image = self.images[self.index]
        #bossenemy2 speed/direction
        if self.rect.y < 0:
            self.rect.y += self.changey
        self.rect.x += self.changex
        self.rect.y += self.changey
        if self.rect.x <= 0 or self.rect.x >= 83:
            self.changex *= -1
        if self.rect.y == 0 or self.rect.y == 80:
            self.changey *= -1
        #bossenemy2 shoot
        self.time_elapsed_since_b1shoot1 += dt
        if self.time_elapsed_since_b1shoot1 > 500: #4 side guns
            b1bullet = Ebullet()
            b1bullet.rect.x, b1bullet.rect.y = self.rect.x + 74, self.rect.y + 200
            interactive_objects.add(b1bullet)
            enemy_list.add(b1bullet)
            b1bullet = Ebullet()
            b1bullet.rect.x, b1bullet.rect.y = self.rect.x + 122, self.rect.y + 200
            interactive_objects.add(b1bullet)
            enemy_list.add(b1bullet)
            b1bullet = Ebullet()
            b1bullet.rect.x, b1bullet.rect.y = self.rect.x + 328, self.rect.y + 200
            interactive_objects.add(b1bullet)
            enemy_list.add(b1bullet)
            b1bullet = Ebullet()
            b1bullet.rect.x, b1bullet.rect.y = self.rect.x + 280, self.rect.y + 200
            interactive_objects.add(b1bullet)
            enemy_list.add(b1bullet)
            self.time_elapsed_since_b1shoot1 = 0
        self.time_elapsed_since_b1shoot2 += dt
        if self.health <= self.initialhealth*0.33 and self.time_elapsed_since_b1shoot2 > 160: #main gun triggered below certain health
            b1bullet2 = Ebullet2()
            b1bullet2.rect.x, b1bullet2.rect.y = self.rect.x + 202, self.rect.y + 220
            interactive_objects.add(b1bullet2)
            enemyopbullet_list.add(b1bullet2)
            self.time_elapsed_since_b1shoot2 = 0
        #bossenemy2 spawn enemies
        self.time_elapsed_since_b1spawnenemy += dt
        if self.time_elapsed_since_b1spawnenemy > 6000:
            e3 = Enemy3() #spawn enemy3
            e3.rect.x = 65
            e3.rect.y = 50
            interactive_objects.add(e3)
            enemy_list.add(e3)
            e3 = Enemy3() #spawn enemy3
            e3.rect.x = 352
            e3.rect.y = 50
            interactive_objects.add(e3)
            enemy_list.add(e3)
            self.time_elapsed_since_b1spawnenemy = 0
        #bossenemy2 regenerate
        self.time_elapsed_since_b2spawn += dt
        if self.time_elapsed_since_b2spawn > 95:
            self.health += 0.2
            self.time_elapsed_since_b2spawn = 0
        if self.health > self.initialhealth:
            self.health = self.initialhealth
        #bossenemy2 killed once health below 0
        if self.health <= 0:
            self.kill()
# --- Boss Enemy 3 ---
#methods inherited from Bossenemy1() class with the difference being in health, bullet speed and enemy2 spawn speed
class Bossenemy3(Bossenemy1):
    def __init__(self):
        super(Bossenemy3, self).__init__()
        #bossenemy3 initial health count
        self.initialhealth = 200
        #bossenemy3 actual health count
        self.health = 200
        #bossenemy3 set initial timer
        self.time_elapsed_since_b3spawn = 0 #regeneration timer
    def update(self):
        #bossenemy3 animation update
        self.index += 1
        if self.health > self.initialhealth*0.46:
            if self.index >= 7:
                self.index = 0
        if self.health <= self.initialhealth*0.46:
            if self.index >= 15:
                self.index = 8
        self.image = self.images[self.index]
        #bossenemy3 speed/direction
        if self.rect.y < 0:
            self.rect.y += self.changey
        self.rect.x += self.changex
        self.rect.y += self.changey
        if self.rect.x <= 0 or self.rect.x >= 83:
            self.changex *= -1
        if self.rect.y == 0 or self.rect.y == 80:
            self.changey *= -1
        #bossenemy3 shoot
        self.time_elapsed_since_b1shoot1 += dt
        if self.time_elapsed_since_b1shoot1 > 400: #4 side guns
            b1bullet = Ebullet()
            b1bullet.rect.x, b1bullet.rect.y = self.rect.x + 74, self.rect.y + 200
            interactive_objects.add(b1bullet)
            enemy_list.add(b1bullet)
            b1bullet = Ebullet()
            b1bullet.rect.x, b1bullet.rect.y = self.rect.x + 122, self.rect.y + 200
            interactive_objects.add(b1bullet)
            enemy_list.add(b1bullet)
            b1bullet = Ebullet()
            b1bullet.rect.x, b1bullet.rect.y = self.rect.x + 328, self.rect.y + 200
            interactive_objects.add(b1bullet)
            enemy_list.add(b1bullet)
            b1bullet = Ebullet()
            b1bullet.rect.x, b1bullet.rect.y = self.rect.x + 280, self.rect.y + 200
            interactive_objects.add(b1bullet)
            enemy_list.add(b1bullet)
            self.time_elapsed_since_b1shoot1 = 0
        self.time_elapsed_since_b1shoot2 += dt
        if self.health <= self.initialhealth*0.33 and self.time_elapsed_since_b1shoot2 > 160: #main gun triggered below certain health
            b1bullet2 = Ebullet2()
            b1bullet2.rect.x, b1bullet2.rect.y = self.rect.x + 202, self.rect.y + 220
            interactive_objects.add(b1bullet2)
            enemyopbullet_list.add(b1bullet2)
            self.time_elapsed_since_b1shoot2 = 0
        #bossenemy3 spawn enemies
        self.time_elapsed_since_b1spawnenemy += dt
        if self.time_elapsed_since_b1spawnenemy > 5000:
            e4 = Enemy4() #spawn enemy4
            e4.rect.x = 65
            e4.rect.y = 50
            interactive_objects.add(e4)
            enemy_list.add(e4)
            e4 = Enemy4() #spawn enemy4
            e4.rect.x = 352
            e4.rect.y = 50
            interactive_objects.add(e4)
            enemy_list.add(e4)
            self.time_elapsed_since_b1spawnenemy = 0
        #bossenemy3 regenerate
        self.time_elapsed_since_b3spawn += dt
        if self.time_elapsed_since_b3spawn > 95:
            self.health += 0.5
            self.time_elapsed_since_b3spawn = 0
        if self.health > self.initialhealth:
            self.health = self.initialhealth
        #bossenemy3 killed once health below 0
        if self.health <= 0:
            self.kill()
# --- Boss Enemy 4 ---
#methods inherited from Bossenemy1() class with the difference being in health, bullet speed and enemy2 spawn speed
class Bossenemy4(Bossenemy1):
    def __init__(self):
        super(Bossenemy4, self).__init__()
        #bossenemy4 initial health count
        self.initialhealth = 225
        #bossenemy4 actual health count
        self.health = 225
        #bossenemy4 set initial timer
        self.time_elapsed_since_b4spawn = 0 #regeneration timer
    def update(self):
        #bossenemy4 animation update
        self.index += 1
        if self.health > self.initialhealth*0.46:
            if self.index >= 7:
                self.index = 0
        if self.health <= self.initialhealth*0.46:
            if self.index >= 15:
                self.index = 8
        self.image = self.images[self.index]
        #bossenemy4 speed/direction
        if self.rect.y < 0:
            self.rect.y += self.changey
        self.rect.x += self.changex
        self.rect.y += self.changey
        if self.rect.x <= 0 or self.rect.x >= 83:
            self.changex *= -1
        if self.rect.y == 0 or self.rect.y == 80:
            self.changey *= -1
        #bossenemy4 shoot
        self.time_elapsed_since_b1shoot1 += dt
        if self.time_elapsed_since_b1shoot1 > 300: #4 side guns
            b1bullet = Ebullet()
            b1bullet.rect.x, b1bullet.rect.y = self.rect.x + 74, self.rect.y + 200
            interactive_objects.add(b1bullet)
            enemy_list.add(b1bullet)
            b1bullet = Ebullet()
            b1bullet.rect.x, b1bullet.rect.y = self.rect.x + 122, self.rect.y + 200
            interactive_objects.add(b1bullet)
            enemy_list.add(b1bullet)
            b1bullet = Ebullet()
            b1bullet.rect.x, b1bullet.rect.y = self.rect.x + 328, self.rect.y + 200
            interactive_objects.add(b1bullet)
            enemy_list.add(b1bullet)
            b1bullet = Ebullet()
            b1bullet.rect.x, b1bullet.rect.y = self.rect.x + 280, self.rect.y + 200
            interactive_objects.add(b1bullet)
            enemy_list.add(b1bullet)
            self.time_elapsed_since_b1shoot1 = 0
        self.time_elapsed_since_b1shoot2 += dt
        if self.health <= self.initialhealth*0.33 and self.time_elapsed_since_b1shoot2 > 160: #main gun triggered below certain health
            b1bullet2 = Ebullet2()
            b1bullet2.rect.x, b1bullet2.rect.y = self.rect.x + 202, self.rect.y + 220
            interactive_objects.add(b1bullet2)
            enemyopbullet_list.add(b1bullet2)
            self.time_elapsed_since_b1shoot2 = 0
        #bossenemy4 spawn enemies
        self.time_elapsed_since_b1spawnenemy += dt
        if self.time_elapsed_since_b1spawnenemy > 5000:
            e3 = Enemy3() #spawn enemy3
            e3.rect.x = 65
            e3.rect.y = 50
            interactive_objects.add(e3)
            enemy_list.add(e3)
            e3 = Enemy3() #spawn enemy3
            e3.rect.x = 352
            e3.rect.y = 50
            interactive_objects.add(e3)
            enemy_list.add(e3)
            e4 = Enemy4() #spawn enemy4
            e4.rect.x = 65
            e4.rect.y = 50
            interactive_objects.add(e4)
            enemy_list.add(e4)
            e4 = Enemy4() #spawn enemy4
            e4.rect.x = 352
            e4.rect.y = 50
            interactive_objects.add(e4)
            enemy_list.add(e4)
            self.time_elapsed_since_b1spawnenemy = 0
        #bossenemy4 regenerate
        self.time_elapsed_since_b4spawn += dt
        if self.time_elapsed_since_b4spawn > 95:
            self.health += 0.8
            self.time_elapsed_since_b4spawn = 0
        if self.health > self.initialhealth:
            self.health = self.initialhealth
        #bossenemy4 killed once health below 0
        if self.health <= 0:
            self.kill()
class Bossenemy5(Bossenemy1):
    def __init__(self):
        super(Bossenemy5, self).__init__()
        #bossenemy5 initial health count
        self.initialhealth = 225
        #bossenemy5 actual health count
        self.health = 225
        #bossenemy5 set initial timer
        self.time_elapsed_since_b5spawn = 0 #regeneration timer
    def update(self):
        #bossenemy5 animation update
        self.index += 1
        if self.health > self.initialhealth*0.46:
            if self.index >= 7:
                self.index = 0
        if self.health <= self.initialhealth*0.46:
            if self.index >= 15:
                self.index = 8
        self.image = self.images[self.index]
        #bossenemy5 speed/direction
        if self.rect.y < 0:
            self.rect.y += self.changey
        self.rect.x += self.changex
        self.rect.y += self.changey
        if self.rect.x <= 0 or self.rect.x >= 83:
            self.changex *= -1
        if self.rect.y == 0 or self.rect.y == 80:
            self.changey *= -1
        #bossenemy5 shoot
        self.time_elapsed_since_b1shoot1 += dt
        if self.time_elapsed_since_b1shoot1 > 200: #4 side guns
            b1bullet = Ebullet()
            b1bullet.rect.x, b1bullet.rect.y = self.rect.x + 74, self.rect.y + 200
            interactive_objects.add(b1bullet)
            enemy_list.add(b1bullet)
            b1bullet = Ebullet()
            b1bullet.rect.x, b1bullet.rect.y = self.rect.x + 122, self.rect.y + 200
            interactive_objects.add(b1bullet)
            enemy_list.add(b1bullet)
            b1bullet = Ebullet()
            b1bullet.rect.x, b1bullet.rect.y = self.rect.x + 328, self.rect.y + 200
            interactive_objects.add(b1bullet)
            enemy_list.add(b1bullet)
            b1bullet = Ebullet()
            b1bullet.rect.x, b1bullet.rect.y = self.rect.x + 280, self.rect.y + 200
            interactive_objects.add(b1bullet)
            enemy_list.add(b1bullet)
            self.time_elapsed_since_b1shoot1 = 0
        self.time_elapsed_since_b1shoot2 += dt
        if self.health <= self.initialhealth*0.33 and self.time_elapsed_since_b1shoot2 > 160: #main gun triggered below certain health
            b1bullet2 = Ebullet2()
            b1bullet2.rect.x, b1bullet2.rect.y = self.rect.x + 202, self.rect.y + 220
            interactive_objects.add(b1bullet2)
            enemyopbullet_list.add(b1bullet2)
            self.time_elapsed_since_b1shoot2 = 0
        #bossenemy5 spawn enemies
        self.time_elapsed_since_b1spawnenemy += dt
        if self.time_elapsed_since_b1spawnenemy > 5000:
            e2 = Enemy2() #spawn enemy2
            e2.rect.x = 65
            e2.rect.y = 50
            interactive_objects.add(e2)
            enemy_list.add(e2)
            e2 = Enemy2() #spawn enemy2
            e2.rect.x = 352
            e2.rect.y = 50
            interactive_objects.add(e2)
            enemy_list.add(e2)
            e3 = Enemy3() #spawn enemy3
            e3.rect.x = 65
            e3.rect.y = 50
            interactive_objects.add(e3)
            enemy_list.add(e3)
            e3 = Enemy3() #spawn enemy3
            e3.rect.x = 352
            e3.rect.y = 50
            interactive_objects.add(e3)
            enemy_list.add(e3)
            e4 = Enemy4() #spawn enemy4
            e4.rect.x = 65
            e4.rect.y = 50
            interactive_objects.add(e4)
            enemy_list.add(e4)
            e4 = Enemy4() #spawn enemy4
            e4.rect.x = 352
            e4.rect.y = 50
            interactive_objects.add(e4)
            enemy_list.add(e4)
            self.time_elapsed_since_b1spawnenemy = 0
        #bossenemy5 regenerate
        self.time_elapsed_since_b5spawn += dt
        if self.time_elapsed_since_b5spawn > 95:
            self.health += 1.0
            self.time_elapsed_since_b5spawn = 0
        if self.health > self.initialhealth:
            self.health = self.initialhealth
        #bossenemy5 killed once health below 0
        if self.health <= 0:
            self.kill()
# --- Standard Enemy-Related Classes ---
# --- Enemy 1 ---
class Enemy1(pg.sprite.Sprite):
    def __init__(self):
        super(Enemy1, self).__init__()
        #enemy1 sprites/animation
        self.images = []
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e1_1.png'), (87, 90)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e1_2.png'), (87, 90)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e1_3.png'), (87, 90)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e1_4.png'), (87, 90)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e1_5.png'), (87, 90)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e1_6.png'), (87, 90)))
        self.index = random.randint(0,5) #randomize starting index(frame) to play
        self.image = self.images[self.index]
        #enemy1 position
        self.rect = self.image.get_rect()
        #enemy1 initial health count
        self.health = 2
        #enemy1 id
        self.id = 1
    #enemy1 update at every frame
    def update(self):
        #enemy1 animation update  
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        #enemy1 speed/direction
        self.rect.y += 5
        #enemy1 killed once it leaves screen
        if self.rect.y > screen_y:
            self.kill()
        #enemy1 killed once health below 0
        if self.health <= 0:
            self.kill()
    #enemy1 spawn
    def spawn(self):
        self.rect.x = random.randint(-20, 450)
        self.rect.y = -120
        interactive_objects.add(self)
        enemy_list.add(self)
# --- Enemy 2 ---
class Enemy2(pg.sprite.Sprite):
    def __init__(self):
        super(Enemy2, self).__init__()
        #enemy2 sprites/animation
        self.images = []
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e2_1.png'), (76, 100)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e2_2.png'), (76, 100)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e2_3.png'), (76, 100)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e2_4.png'), (76, 100)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e2_5.png'), (76, 100)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e2_6.png'), (76, 100)))
        self.index = random.randint(0,5) #randomize starting index(frame) to play
        self.image = self.images[self.index]
        #enemy2 position
        self.rect = self.image.get_rect()
        #enemy2 specific initial timer set to 0
        self.time_elapsed_since_e2shoot = 0
        #enemy2 initial health count
        self.health = 3
        #enemy2 id
        self.id = 2
    #enemy2 update at every frame
    def update(self):
        #enemy2 animation update  
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        #enemy2 speed/direction
        self.rect.y += 3
        #enemy2 killed once it leaves screen
        if self.rect.y > screen_y:
            self.kill()
        #enemy2 shoot
        self.time_elapsed_since_e2shoot += dt
        if self.time_elapsed_since_e2shoot > 550:
            e2bullet = Ebullet()
            e2bullet.rect.x, e2bullet.rect.y = self.rect.x + 30, self.rect.y + 80
            interactive_objects.add(e2bullet)
            enemy_list.add(e2bullet)
            self.time_elapsed_since_e2shoot = 0
        #enemy2 killed once health below 0
        if self.health <= 0:
            self.kill()
    #enemy2 spawn
    def spawn(self):
        self.rect.x = random.randint(-20, 450)
        self.rect.y = -120
        interactive_objects.add(self)
        enemy_list.add(self)
# --- Enemy 3 ---
class Enemy3(pg.sprite.Sprite):
    def __init__(self):
        super(Enemy3, self).__init__()
        #enemy3 sprites/animation
        self.images = []
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e3_1.png'), (90, 90)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e3_2.png'), (90, 90)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e3_3.png'), (90, 90)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e3_4.png'), (90, 90)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e3_5.png'), (90, 90)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e3_6.png'), (90, 90)))
        self.index = random.randint(0,5) #randomize starting index(frame) to play
        self.image = self.images[self.index]
        #enemy3 position
        self.rect = self.image.get_rect()
        #enemy3 specific initial timer set to 0
        self.time_elapsed_since_e3shoot = 0
        #enemy3 initial health count
        self.health = 4
        #enemy3 id
        self.id = 3
    #enemy3 update at every frame
    def update(self):
        #enemy3 animation update  
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        #enemy3 speed/direction
        self.rect.y += 4
        #enemy3 killed once it leaves screen
        if self.rect.y > screen_y:
            self.kill()
        #enemy3 shoot
        self.time_elapsed_since_e3shoot += dt
        if self.time_elapsed_since_e3shoot > 750:
            e3bullet = Ebullet()
            e3bullet.rect.x, e3bullet.rect.y = self.rect.x + 28, self.rect.y + 60
            interactive_objects.add(e3bullet)
            enemy_list.add(e3bullet)
            self.time_elapsed_since_e2shoot = 0
            e3bullet = Ebullet()
            e3bullet.rect.x, e3bullet.rect.y = self.rect.x + 45, self.rect.y + 60
            interactive_objects.add(e3bullet)
            enemy_list.add(e3bullet)
            self.time_elapsed_since_e3shoot = 0
        #enemy3 killed once health below 0
        if self.health <= 0:
            self.kill()
    #enemy3 spawn
    def spawn(self):
        self.rect.x = random.randint(-20, 450)
        self.rect.y = -120
        interactive_objects.add(self)
        enemy_list.add(self)
# --- Enemy 4 ---
class Enemy4(pg.sprite.Sprite):
    def __init__(self):
        super(Enemy4, self).__init__()
        #enemy4 sprites/animation
        self.images = []
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e4_1.png'), (76, 100)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e4_2.png'), (76, 100)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e4_3.png'), (76, 100)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e4_4.png'), (76, 100)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e4_5.png'), (76, 100)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e4_6.png'), (76, 100)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e4_7.png'), (76, 100)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e4_8.png'), (76, 100)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e4_9.png'), (76, 100)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e4_10.png'), (76, 100)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e4_11.png'), (76, 100)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e4_12.png'), (76, 100)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e4_13.png'), (76, 100)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e4_14.png'), (76, 100)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e4_15.png'), (76, 100)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e4_16.png'), (76, 100)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e4_17.png'), (76, 100)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_e4_18.png'), (76, 100)))
        self.index = random.randint(0,5) #randomize starting index(frame) to play
        self.image = self.images[self.index]
        #enemy4 position
        self.rect = self.image.get_rect()
        #enemy4 specific initial timer set to 0
        self.time_elapsed_since_e4spawn = 0
        self.time_elapsed_since_e4shoot = 0
        self.time_elapsed_since_e4shoot2 = 0
        #enemy4 initial health count
        self.health = 5
        #enemy4 id
        self.id = 4
    #enemy4 update at every frame
    def update(self):
        #enemy4 animation update  
        self.index += 1
        #time since enemy4 spawned (to trigger warning for main gun)
        self.time_elapsed_since_e4spawn += dt
        if self.time_elapsed_since_e4spawn <= 1500:
            if self.index >= 5:
                self.index = 0
        if self.time_elapsed_since_e4spawn > 1500:
            if self.index >= 17:
                self.index = 6
        self.image = self.images[self.index]
        #enemy4 speed/direction
        self.rect.y += 2
        #enemy4 killed once it leaves screen
        if self.rect.y > screen_y:
            self.kill()
        #enemy4 shoot
        self.time_elapsed_since_e4shoot += dt
        if self.time_elapsed_since_e4shoot > 450:
            e4bullet = Ebullet()
            e4bullet.rect.x, e4bullet.rect.y = self.rect.x + 42, self.rect.y + 80
            interactive_objects.add(e4bullet)
            enemy_list.add(e4bullet)
            self.time_elapsed_since_e4shoot = 0
        #enemy shoots laser after a period of time
        self.time_elapsed_since_e4shoot2 += dt
        if self.time_elapsed_since_e4spawn > 2750 and self.time_elapsed_since_e4shoot2 > 160:
            e4bullet2 = Ebullet2()
            e4bullet2.rect.x, e4bullet2.rect.y = self.rect.x + 36, self.rect.y + 100
            interactive_objects.add(e4bullet2)
            enemyopbullet_list.add(e4bullet2)
            self.time_elapsed_since_e4shoot2 = 0
        #enemy4 killed once health below 0
        if self.health <= 0:
            self.kill()
    #enemy4 spawn
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
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_meteor_small_1.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_meteor_small_2.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_meteor_small_3.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_meteor_small_4.png'), (sprite_size, sprite_size)))
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
        self.rect.y += 6
        #small meteor killed once it leaves screen
        if self.rect.y > screen_y:
            self.kill()
    #small meteor spawn
    def spawn(self):
        self.rect.x = random.randint(-20, 450)
        self.rect.y = -100    
        interactive_objects.add(self)
        enemy_list.add(self)
# --- Enemy Bullet Classes ---
class Ebullet(pg.sprite.Sprite):
    def __init__(self):
        super(Ebullet, self).__init__()
        #ebullet sprites/animation
        self.images = []
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_ebullet_1.png'), (16, 32)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_ebullet_2.png'), (16, 32)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_ebullet_3.png'), (16, 32)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_ebullet_4.png'), (16, 32)))
        self.index = 0
        self.image = self.images[self.index]
        #ebullet position
        self.rect = self.image.get_rect()
        #ebullet id
        self.id = 2.1
        #ebullet sound
        pg.mixer.Channel(7).play(pg.mixer.Sound('./Sound/space-sound_ebullet.wav'))
    #ebullet update at every frame
    def update(self):
        #ebullet animation update
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        #ebullet speed/direction
        self.rect.y += 7
        #ebullet killed once it leaves screen
        if self.rect.y > screen_y:
            self.kill()
class Ebullet2(pg.sprite.Sprite):
    def __init__(self):
        super(Ebullet2, self).__init__()
        #ebullet2 sprites/animation
        self.images = []
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_ebullet2_1.png'), (5, 650)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_ebullet2_2.png'), (5, 650)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_ebullet2_3.png'), (5, 650)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_ebullet2_4.png'), (5, 650)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_ebullet2_5.png'), (5, 650)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_ebullet2_6.png'), (5, 650)))
        self.index = 0
        self.image = self.images[self.index]
        #ebullet2  position
        self.rect = self.image.get_rect()
        #ebullet2 id
        self.id = 2.2
        #ebullet2 specific initial timer set to 0
        self.time_elapsed_since_ebullet2shoot = 0
        #ebullet2  sound
        pg.mixer.Channel(8).play(pg.mixer.Sound('./Sound/space-sound_ebullet2.wav'))
    #ebullet2  update at every frame
    def update(self):
        #ebullet2  animation update
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        #ebullet2 removed every 160 ticks to simulate tracing laser
        self.time_elapsed_since_ebullet2shoot += dt
        if self.time_elapsed_since_ebullet2shoot > 160:
            self.kill()
            self.time_elapsed_since_ebullet2shoot = 0
# --- Visual Effects Classes ---
# --- Player Explosion ---
class Pex(pg.sprite.Sprite):
    def __init__(self):
        super(Pex, self).__init__()
        #player explosion sprites/animation
        self.images = []
        sprite_size = random.randint(90, 120) #randomize player explosion size
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_pex_1.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_pex_2.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_pex_3.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_pex_4.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_pex_5.png'), (sprite_size, sprite_size)))
        self.index = 0
        self.image = self.images[self.index]
        #player explosion position
        self.rect = self.image.get_rect()
        #player explosion sound
        pg.mixer.Channel(2).play(pg.mixer.Sound('./Sound/space-sound_pdamage.wav'))
    #player explosion update at every frame
    def update(self):
        #player explosion animation update
        self.index += 1
        self.image = self.images[self.index]
        #player explosion killed once animation ends
        if self.index == 4:
            self.kill()
# --- Boss Explosion ---
class Bossex(pg.sprite.Sprite):
    def __init__(self):
        super(Bossex, self).__init__()
        #boss explosion sprites/animation
        self.images = []
        sprite_size = random.randint(90, 120) #randomize boss explosion size
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_bossex_1.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_bossex_2.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_bossex_3.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_bossex_4.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_bossex_5.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_bossex_6.png'), (sprite_size, sprite_size)))
        self.index = 0
        self.image = self.images[self.index]
        #boss explosion position
        self.rect = self.image.get_rect()
        #boss explosion sound
        pg.mixer.Channel(3).play(pg.mixer.Sound('./Sound/space-sound_bossdamage.wav'))
    #boss explosion update at every frame
    def update(self):
        #boss explosion animation update
        self.index += 1
        self.image = self.images[self.index]
        #boss explosion killed once animation ends
        if self.index == 5:
            self.kill()
# --- Small Explosion ---
class Smallex(pg.sprite.Sprite):
    def __init__(self):
        super(Smallex, self).__init__()
        #small explosion sprites/animation
        self.images = []
        sprite_size = random.randint(56, 96) #randomize small explosion size
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_smallex_1.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_smallex_2.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_smallex_3.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_smallex_4.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_smallex_5.png'), (sprite_size, sprite_size)))
        self.index = 0
        self.image = self.images[self.index]
        #small explosion position
        self.rect = self.image.get_rect()
        #small explosion sound
        pg.mixer.Channel(4).play(pg.mixer.Sound('./Sound/space-sound_smallex.wav'))
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
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_asteroidex_1.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_asteroidex_2.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_asteroidex_3.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_asteroidex_4.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_asteroidex_5.png'), (sprite_size, sprite_size)))
        self.index = 0
        self.image = self.images[self.index]
        #asteroid explosion position
        self.rect = self.image.get_rect()
        #asteroid explosion sound
        pg.mixer.Channel(5).play(pg.mixer.Sound('./Sound/space-sound_meteorex.wav'))
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
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_stars_1.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_stars_2.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_stars_3.png'), (sprite_size, sprite_size)))
        self.images.append(pg.transform.scale(pg.image.load('./Images/space-image_stars_4.png'), (sprite_size, sprite_size)))
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
        self.rect.y += 1
        #stars killed once it leaves screen
        if self.rect.y > screen_y:
            self.kill()
    #stars spawn
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
    buttontext_font = pg.font.Font("./Fonts/font.ttf", text_s) #text font
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
    gamemodeselect = False
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
        screen.blit(gameintro_text2, (67, 250))
        pg.display.flip()
        clock.tick(24)
    #launch to gamemode select/exit game base on choice
    if gamemodeselect == True:
        gamemode_select(gamemodeselect)
    if gamemodeselect == False:
        pg.quit()
        sys.exit()
def gamemode_select(gamemodeselect):
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
    testship2 = Ship2()
    testship.rect.x, testship.rect.y = 190, 170
    testship2.rect.x, testship2.rect.y = 190, 415
    test_list.add(testship)
    test_list.add(testship2)
    gamemodeselect = True
    while gamemodeselect == True: #loop while gamemodeselect is still running
        for event in pg.event.get():
            if event.type == pg.QUIT: #quit game
                gamemodeselect = False
                gameplay = False
            mouse = pg.mouse.get_pos() #check mouse position
            if event.type == pg.MOUSEBUTTONDOWN and 348 > mouse[0] > 148 and 550 > mouse[1] > 500: #gamemode 1
                gamemode = 1
                gamemodeselect = False
                gameplay = True
            if event.type == pg.MOUSEBUTTONDOWN and 348 > mouse[0] > 148 and 610 > mouse[1] > 560: #gamemode 2
                gamemode = 2
                gamemodeselect = False
                gameplay = True
        keypressed = pg.key.get_pressed()
        if keypressed[pg.K_LEFT]: #player1 movement to left
            testship.moveLeft(5)
        if keypressed[pg.K_RIGHT]: #player1 movement to right
            testship.moveRight(5)
        if (keypressed[pg.K_KP3] and testship.health > 0) or (keypressed[pg.K_p] and testship.health > 0): #player1 shoot
            testship.testshoot()
        if keypressed[pg.K_a]: #player2 movement to left
            testship2.moveLeft(5)
        if keypressed[pg.K_d]: #player2 movement to right
            testship2.moveRight(5)
        if keypressed[pg.K_SPACE] and testship2.health > 0: #player2 shoot
            testship2.testshoot()
        # --- Draw The Screen ---
        screen.fill((0,0,0))
        button("Single Player", 28, (255, 255, 255), 148, 500, 200, 50, dark_green, green)
        button("Two Player", 28, (255, 255, 255), 148, 560, 200, 50, dark_green, green)
        gamemodeselect_text1 = gamemodeselect_text1_font.render("Controls", True, yellow)
        gamemodeselect_text2 = gamemodeselect_instruction1_font.render("Single Player", True, white)
        gamemodeselect_text3 = gamemodeselect_instruction1_font.render("Two Player", True, white)
        gamemodeselect_text3_1 = gamemodeselect_instruction1_font.render("Player 1", True, white)
        gamemodeselect_text3_2 = gamemodeselect_instruction1_font.render("Player 2", True, white)
        gamemodeselect_text4 = gamemodeselect_instruction2_font.render("<- Left Arrow                Right Arrow ->", True, white)
        gamemodeselect_text5 = gamemodeselect_instruction2_font.render("<- A                D ->", True, white)
        gamemodeselect_text6 = gamemodeselect_instruction2_font.render("Space                   Bar", True, white)
        gamemodeselect_text7 = gamemodeselect_instruction2_font.render("Num                   3", True, white)
        gamemodeselect_text8 = gamemodeselect_instruction3_font.render("MOVE", True, green)
        gamemodeselect_text9 = gamemodeselect_instruction3_font.render("SHOOT", True, green)
        test_list.update()
        test_list.draw(screen)
        screen.blit(gamemodeselect_text1, (127, 50))
        screen.blit(gamemodeselect_text2, (180, 100))
        screen.blit(gamemodeselect_text3, (185, 245))
        screen.blit(gamemodeselect_text3_1, (205, 270))
        screen.blit(gamemodeselect_text3_2, (205, 343))
        screen.blit(gamemodeselect_text4, (97, 128))
        screen.blit(gamemodeselect_text4, (97, 297))
        screen.blit(gamemodeselect_text5, (181, 369))
        screen.blit(gamemodeselect_text6, (158, 155))
        screen.blit(gamemodeselect_text6, (158, 397))
        screen.blit(gamemodeselect_text7, (170, 321))
        screen.blit(gamemodeselect_text8, (218, 125))
        screen.blit(gamemodeselect_text8, (218, 293))
        screen.blit(gamemodeselect_text8, (218, 366))
        screen.blit(gamemodeselect_text9, (218, 152))
        screen.blit(gamemodeselect_text9, (215, 318))
        screen.blit(gamemodeselect_text9, (215, 393))
        pg.display.flip()
        clock.tick(60)
    #set initial highscore
    if gameplay == True:
        with open("./Stats/stats.json", "r") as file:
            stats = json.load(file)
            if gamemode == 1:
                highscore = int(stats["single_player_highscore"])
            else:
                highscore = int(stats["two_player_highscore"])
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
    global interactive_objects, noninteractive_objects, bullet_list, opbullet_list, enemy_list, bossenemy_list,  enemyopbullet_list, powerup_list #main lists for interactions
    interactive_objects = pg.sprite.Group()
    noninteractive_objects = pg.sprite.Group()
    enemy_list = pg.sprite.Group()
    bossenemy_list = pg.sprite.Group()
    enemyopbullet_list = pg.sprite.Group()
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
    plife_list.add(playerlife1)
    plife_list.add(playerlife2)
    plife_list.add(playerlife3)
    noninteractive_objects.add(playerlife1)
    noninteractive_objects.add(playerlife2)
    noninteractive_objects.add(playerlife3)
    #player2 creation in 2 player mode
    if gamemode == 2:
        ship.rect.x, ship.rect.y = 275, 600 #shifts player1 position to accommodate player2
        ship2 = Ship2()
        ship2.rect.x, ship2.rect.y = 125, 600
        player_list.add(ship2)
        interactive_objects.add(ship2)
        player2life1 = Player2life()
        player2life2 = Player2life()
        player2life3 = Player2life()
        plife_list.add(player2life1)
        plife_list.add(player2life2)
        plife_list.add(player2life3)
        noninteractive_objects.add(player2life1)
        noninteractive_objects.add(player2life2)
        noninteractive_objects.add(player2life3)
    # --- Time/Score Generation ---
    score = 0
    time_elapsed_since_smallmeteorspawn = 0
    time_elapsed_since_e1spawn = 0
    time_elapsed_since_e2spawn = 0
    time_elapsed_since_e3spawn = 0
    time_elapsed_since_e4spawn = 0
    time_elapsed_since_powerup1spawn = 0
    time_elapsed_since_powerup2spawn = 0
    time_elapsed_since_powerup3spawn = 0
    time_elapsed_since_powerup4spawn = 0
    time_elapsed_since_starsspawn = 0
    time_elapsed_since_score = 0
    time_elapsed_since_start = 0
    bosstime = False
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
            if (keypressed[pg.K_KP3] and ship.health > 0) or (keypressed[pg.K_p] and ship.health > 0): #player1 shoot
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
        # --- Spawn Time/Difficulty Management ---
        time_elapsed_since_start += dt
        starsspawntime = random.randint(120,150)
        smallmeteorspawntime = random.randint(600, 750)
        if time_elapsed_since_start < 35000:
            powerup1spawntime = random.randint(52500, 57500)
            powerup2spawntime = random.randint(82500, 87500)
            powerup3spawntime = random.randint(72500, 77500)
            powerup4spawntime = random.randint(117500, 127500)
            e1spawntime = random.randint(800, 900)
            #nospawn e2spawntime
            #nospawn e3spawntime
            #nospawn e4spawntime
        elif time_elapsed_since_start >= 35000 and time_elapsed_since_start < 95000:
            powerup1spawntime = random.randint(52500, 57500)
            powerup2spawntime = random.randint(82500, 87500)
            powerup3spawntime = random.randint(72500, 77500)
            powerup4spawntime = random.randint(117500, 127500)
            e1spawntime = random.randint(750, 850)
            e2spawntime = random.randint(2500, 3500)
            #nospawn e3spawntime
            #nospawn e4spawntime
        elif time_elapsed_since_start >= 95000 and time_elapsed_since_start < 180000: #boss 1 spawns at 130000
            powerup1spawntime = random.randint(47500, 52500)
            powerup2spawntime = random.randint(77500, 82500)
            powerup3spawntime = random.randint(67500, 72500)
            powerup4spawntime = random.randint(107500, 117500)
            e1spawntime = random.randint(700, 800)
            e2spawntime = random.randint(2200, 2700)
            e3spawntime = random.randint(4500, 5500)
            #nospawn e4spawntime
        elif time_elapsed_since_start >= 180000 and time_elapsed_since_start < 300000: #boss2 spawns at 260000
            powerup1spawntime = random.randint(42500, 47500)
            powerup2spawntime = random.randint(72500, 77500)
            powerup3spawntime = random.randint(62500, 67500)
            powerup4spawntime = random.randint(97500, 107500)
            e1spawntime = random.randint(700, 800)
            e2spawntime = random.randint(2000, 2400)
            e3spawntime = random.randint(4250, 5250)
            e4spawntime = random.randint(7000, 8000)
        elif time_elapsed_since_start >= 300000 and time_elapsed_since_start < 425000: #boss3 spawns at 380000
            powerup1spawntime = random.randint(37500, 42500)
            powerup2spawntime = random.randint(67500, 72500)
            powerup3spawntime = random.randint(57500, 62500)
            powerup4spawntime = random.randint(87500, 97500)
            e1spawntime = random.randint(650, 750)
            e2spawntime = random.randint(1800, 2200)
            e3spawntime = random.randint(3750, 4750)
            e4spawntime = random.randint(6000, 7000)
        elif time_elapsed_since_start >= 425000 and time_elapsed_since_start < 550000: #boss 4 spawns at 500000
            powerup1spawntime = random.randint(32500, 37500)
            powerup2spawntime = random.randint(62500, 67500)
            powerup3spawntime = random.randint(52500, 57500)
            powerup4spawntime = random.randint(82500, 92500)
            e1spawntime = random.randint(550, 650)
            e2spawntime = random.randint(1600, 2000)
            e3spawntime = random.randint(3000, 4000)
            e4spawntime = random.randint(5000, 6000)
        if time_elapsed_since_start >= 550000 and time_elapsed_since_start < 600000:
            powerup1spawntime = random.randint(30000, 35000)
            powerup2spawntime = random.randint(55000, 60000)
            powerup3spawntime = random.randint(45000, 50000)
            powerup4spawntime = random.randint(75000, 85000)
            e1spawntime = random.randint(500, 500)
            e2spawntime = random.randint(1400, 1700)
            e3spawntime = random.randint(2500, 3000)
            e4spawntime = random.randint(4000, 4500)
        if time_elapsed_since_start >= 600000 and time_elapsed_since_start < 650000: #boss 5 spawns at 625000
            powerup1spawntime = random.randint(30000, 35000)
            powerup2spawntime = random.randint(55000, 60000)
            powerup3spawntime = random.randint(45000, 50000)
            powerup4spawntime = random.randint(75000, 85000)
            e1spawntime = random.randint(350, 400)
            e2spawntime = random.randint(1200, 1400)
            e3spawntime = random.randint(2000, 2200)
            e4spawntime = random.randint(3000, 3500)
        if time_elapsed_since_start >= 650000:
            powerup1spawntime = random.randint(30000, 35000)
            powerup2spawntime = random.randint(55000, 60000)
            powerup3spawntime = random.randint(45000, 50000)
            powerup4spawntime = random.randint(75000, 85000)
            e1spawntime = random.randint(250, 300)
            e2spawntime = random.randint(1000, 1000)
            e3spawntime = random.randint(1200, 1400)
            e4spawntime = random.randint(2000, 2500)
        # --- Standard Character Spawn Management ---
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
        if time_elapsed_since_start >= 35000:
            time_elapsed_since_e2spawn += dt #enemy 2 spawn
            if time_elapsed_since_e2spawn > e2spawntime:
                e2 = Enemy2()
                e2.spawn()
                time_elapsed_since_e2spawn = 0
        if time_elapsed_since_start >= 150000:
            time_elapsed_since_e3spawn += dt #enemy 3 spawn
            if time_elapsed_since_e3spawn > e3spawntime:
                e3 = Enemy3()
                e3.spawn()
                time_elapsed_since_e3spawn = 0
        if time_elapsed_since_start >= 220000:
            time_elapsed_since_e4spawn += dt #enemy 4 spawn
            if time_elapsed_since_e4spawn > e4spawntime:
                e4 = Enemy4()
                e4.spawn()
                time_elapsed_since_e4spawn = 0 
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
        time_elapsed_since_powerup3spawn += dt #powerup3 spawn
        if time_elapsed_since_powerup3spawn > powerup3spawntime:
            powerup3 = Powerup3()
            powerup3.spawn()
            time_elapsed_since_powerup3spawn = 0
        time_elapsed_since_powerup4spawn += dt #powerup3 spawn
        if time_elapsed_since_powerup4spawn > powerup4spawntime:
            powerup4 = Powerup4()
            powerup4.spawn()
            time_elapsed_since_powerup4spawn = 0
        # --- Boss Enemy Spawn Management ---
        if time_elapsed_since_start > 129990 and time_elapsed_since_start < 130000: #boss1 spawn
            bossenemy = Bossenemy1()
            bossenemy.spawn()
            bosstime = True
        if time_elapsed_since_start > 259980 and time_elapsed_since_start < 260000: #boss2 spawn
            bossenemy = Bossenemy2()
            bossenemy.spawn()
            bosstime = True
        if time_elapsed_since_start > 379980 and time_elapsed_since_start < 380000: #boss3 spawn
            bossenemy = Bossenemy3()
            bossenemy.spawn()
            bosstime = True
        if time_elapsed_since_start > 499990 and time_elapsed_since_start < 500000: #boss4 spawn
            bossenemy = Bossenemy4()
            bossenemy.spawn()
            bosstime = True
        if time_elapsed_since_start > 624990 and time_elapsed_since_start < 625000: #boss5 spawn
            bossenemy = Bossenemy5()
            bossenemy.spawn()
            bosstime = True
        if bosstime == True:
            #disable other enemies from spawning
            time_elapsed_since_smallmeteorspawn = 0
            time_elapsed_since_e1spawn = 0
            time_elapsed_since_e2spawn = 0
            time_elapsed_since_e3spawn = 0
            time_elapsed_since_e4spawn = 0
            hpsurface = pg.Surface((bossenemy.initialhealth*2,20)) #draw boss healthbar
            pg.draw.rect(hpsurface, green, pg.Rect(0, 0, bossenemy.health*2, 20))
            if bossenemy.health <= 0:
                #spawn one healthpack when boss dies
                powerup3 = Powerup3()
                powerup3.spawn()
                #boss big explosions when dead
                bossex = Bossex()
                bossex.rect.x, bossex.rect.y = bossenemy.rect.x + 200, bossenemy.rect.y + 110
                interactive_objects.add(bossex)
                bossex = Bossex()
                bossex.rect.x, bossex.rect.y = bossenemy.rect.x + 250, bossenemy.rect.y + 160
                interactive_objects.add(bossex)
                bossex = Bossex()
                bossex.rect.x, bossex.rect.y = bossenemy.rect.x + 270, bossenemy.rect.y + 180
                interactive_objects.add(bossex)
                bossex = Bossex()
                bossex.rect.x, bossex.rect.y = bossenemy.rect.x + 310, bossenemy.rect.y + 60
                interactive_objects.add(bossex)
                bossex = Bossex()
                bossex.rect.x, bossex.rect.y = bossenemy.rect.x + 170, bossenemy.rect.y + 90
                interactive_objects.add(bossex)
                bossex = Bossex()
                bossex.rect.x, bossex.rect.y = bossenemy.rect.x + 150, bossenemy.rect.y + 120
                interactive_objects.add(bossex)
                bossex = Bossex()
                bossex.rect.x, bossex.rect.y = bossenemy.rect.x + 135, bossenemy.rect.y + 200
                interactive_objects.add(bossex)
                bossex = Bossex()
                bossex.rect.x, bossex.rect.y = bossenemy.rect.x + 80, bossenemy.rect.y + 20
                interactive_objects.add(bossex)
                bossex = Bossex()
                bossex.rect.x, bossex.rect.y = bossenemy.rect.x + 60, bossenemy.rect.y + 135
                interactive_objects.add(bossex)
                #resume normal enemy spawn
                bosstime = False
        # --- Collision Management ---
        # --- Player Bullet Collision with Enemy ---
        for enemy in enemy_list:
            enemyhits = pg.sprite.spritecollide(enemy, bullet_list, True)
            enemyhitsop = pg.sprite.spritecollide(enemy, opbullet_list, False)
            if (enemyhits or enemyhitsop) and (enemy.id == 0 or enemy.id == 2.1): #collision with enemy that has health = 1
                asteroidex = Asteroidex()
                asteroidex.rect.x, asteroidex.rect.y = enemy.rect.x, enemy.rect.y
                interactive_objects.add(asteroidex)
                enemy.kill()
            if (enemyhits or enemyhitsop) and (enemy.id == 1 or enemy.id == 2 or enemy.id == 3 or enemy.id == 4): #collision with enemy that has health > 1
                smallex = Smallex()
                smallex.rect.x, smallex.rect.y = enemy.rect.x, enemy.rect.y
                interactive_objects.add(smallex)
                enemy.health -= 1
        # --- Player Bullet Collision with Boss Enemy ---
        for bullet in bullet_list:
            bullethits = pg.sprite.spritecollide(bullet, bossenemy_list, False)
            if bullethits: #collision with boss enemy
                bossex = Bossex()
                bossex.rect.x, bossex.rect.y = bullet.rect.x, bullet.rect.y - 100
                interactive_objects.add(bossex)
                bossenemy.health -= 1
                bullet.kill()
        for opbullet in opbullet_list:
            opbullethits = pg.sprite.spritecollide(opbullet, bossenemy_list, False)
            if opbullethits: #collision with boss enemy
                bossex = Bossex()
                bossex.rect.x, bossex.rect.y = bullet.rect.x, bullet.rect.y - 100
                interactive_objects.add(bossex)
                bossenemy.health -= 1/20
        # --- Player Bullet/Player Collision with Enemy OP Bullet ---
        for bullet in bullet_list:
            bullethits = pg.sprite.spritecollide(bullet, enemyopbullet_list, False)
            if bullethits: #player bullet collision with enemy op bullet
                asteroidex = Asteroidex()
                asteroidex.rect.x, asteroidex.rect.y = bullet.rect.x, bullet.rect.y
                interactive_objects.add(asteroidex)
                bullet.kill()
        for player in player_list:
            playerhits = pg.sprite.spritecollide(player, enemyopbullet_list, False)
            if playerhits: #player collision with enemy op bullet
                pex = Pex()
                pex.rect.center = player.rect.center
                interactive_objects.add(pex)
                player.health -= 1/30 #full health player dies in 1.5 seconds in laser
        # --- Player Collision with Enemy ---
        for player in player_list:
            playerhits = pg.sprite.spritecollide(player, enemy_list, True)
            if playerhits: #player collision with enemy
                pex = Pex()
                pex.rect.center = player.rect.center
                interactive_objects.add(pex)
                player.health -= 1
        # --- Player Collision with Power Up ---
        for powerup in powerup_list:
            poweruphits = pg.sprite.spritecollide(powerup, player_list, False)
            if poweruphits and powerup.id == 1: #player collision with powerup1
                ship.consume()
                ship.powerupvalue = 1
                powerup.kill()
                #player2 gets powerup too in 2 player mode
                if gamemode == 2:
                    ship2.consume()
                    ship2.powerupvalue = 1
                    powerup.kill()
            if poweruphits and powerup.id == 2: #player collision with powerup2
                ship.consume()
                ship.powerupvalue = 2
                powerup.kill()
                #player2 gets powerup too in 2 player mode
                if gamemode == 2:
                    ship2.consume()
                    ship2.powerupvalue = 2
                    powerup.kill()
            if poweruphits and powerup.id == 3: #player collision with powerup3
                ship.heal()
                if ship.health > 0: #prevent the dead from healing
                    ship.health += 1
                if ship.health > 3: #prevent overhealing
                    ship.health = 3
                powerup.kill()
                if gamemode == 2:
                    ship2.heal()
                    if ship2.health > 0: #prevent the dead from healing
                        ship2.health += 1
                    if ship2.health > 3: #prevent overhealing
                        ship2.health = 3
                    powerup.kill()
            if poweruphits and powerup.id == 4: #player collision with powerup 3
                ship.consume()
                ship.powerupvalue = 4
                powerup.kill()
                #player2 gets powerup too in 2 player mode
                if gamemode == 2:
                    ship2.consume()
                    ship2.powerupvalue = 4
                    powerup.kill()
        # --- Player Life Management ---
        #player1 life display management
        if ship.health >= 3: #display 3 life
            playerlife1.rect.x, playerlife1.rect.y = 402, 20
            playerlife2.rect.x, playerlife2.rect.y = 422, 20
            playerlife3.rect.x, playerlife3.rect.y = 442, 20
        if ship.health <= 2 and ship.health > 1: #display 2 life
            playerlife1.rect.x, playerlife1.rect.y = 402, -100
            playerlife2.rect.x, playerlife2.rect.y = 422, 20
            playerlife3.rect.x, playerlife3.rect.y = 442, 20
        if ship.health <= 1 and ship.health > 0: #display 1 life
            playerlife1.rect.x, playerlife1.rect.y = 402, -100
            playerlife2.rect.x, playerlife2.rect.y = 422, -100
            playerlife3.rect.x, playerlife3.rect.y = 442, 20
        if ship.health <= 0: #kill player
            ship.health = 0
            playerlife1.kill()
            playerlife2.kill()
            playerlife3.kill()
            ship.kill()
        #player2 life display management in 2 player mode
        if gamemode == 2:
            if ship2.health >= 3: #display 3 life
                player2life1.rect.x, player2life1.rect.y = 402, 45
                player2life2.rect.x, player2life2.rect.y = 422, 45
                player2life3.rect.x, player2life3.rect.y = 442, 45
            if ship2.health <= 2 and ship2.health > 1: #display 2 life
                player2life1.rect.x, player2life1.rect.y = 402, -100
                player2life2.rect.x, player2life2.rect.y = 422, 45
                player2life3.rect.x, player2life3.rect.y = 442, 45
            if ship2.health <= 1 and ship2.health > 0: #display 1 life
                player2life1.rect.x, player2life1.rect.y = 402, -100
                player2life2.rect.x, player2life2.rect.y = 422, -100
                player2life3.rect.x, player2life3.rect.y = 442, 45
            if ship2.health <= 0: #kill player
                ship2.health = 0
                player2life1.kill()
                player2life2.kill()
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
        if bosstime == True: #draw boss healthbar
            screen.blit(hpsurface, ((screen_x-bossenemy.initialhealth*2)/2, 20))
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
    game_over(score, highscore, gamemode)
# --- Game Over Loop ---
def game_over(score, highscore, gamemode):
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
        button("Play Again", 28, (255, 255, 255), 80, 400, 150, 50, dark_green, green)
        button("Quit", 28, (255, 255, 255), 280, 400, 150, 50, dark_red, red)
        gameover_text = gameover_text_font.render("Game Over!", True, red)
        gameover_text2 = gameover_text2_font.render("Your High Score is:", True, white)
        gameover_text3 = gameover_text3_font.render(str(score), True, yellow)
        screen.blit(gameover_text, (90, 200))
        screen.blit(gameover_text2, (155, 300))
        screen.blit(gameover_text3, (240, 350))
        # --- New High Score Management ---
        if score > highscore:
            highscore_text = highscore_text_font.render("You set a new highscore!", True, green)
            screen.blit(highscore_text, (35, 500))
        pg.display.flip()
    # --- Restart/Quit Management ---
    if score > highscore:
        highscore = score
        with open("./Stats/stats.json", "r") as file:
            stats = json.load(file)
        with open("./Stats/stats.json", "w+") as file:
            if gamemode == 1:
                stats["single_player_highscore"] = score
            else:
                stats["two_player_highscore"] = score
            json.dump(stats, file)
    if gamemodeselect == True:
        gamemode_select(gamemodeselect)
    if gamemodeselect == False:
        pg.quit()
        sys.exit()
# --- Notifications set up ---      
def notify(title, text, sound):
    os.system("""
        osascript -e 'display notification "{}" with title "{}" sound name "{}"'
        """.format(text, title, sound))
# --- General Set Up ---
notify('SpaceShips Alert',
    'Hello there, if your Macbook supports retina display, please run the application in low resolution.',
    'default')
clock = pg.time.Clock()
dt = 16.666 #1 second approximately 1000 ticks
screen_x = 500 #screen width
screen_y = 700 #screen height
screen = pg.display.set_mode((screen_x, screen_y)) #screen game is played on
pg.display.set_caption("SpaceShips!") #display at top of screen
pg.mixer.set_num_channels(12) #12 channels for sound
# --- Fonts to be used ---
score_font = pg.font.Font("./Fonts/font.ttf", 24)
gameintro_text1_font = pg.font.Font("./Fonts/font.ttf", 32)
gameintro_text2_font = pg.font.Font("./Fonts/font.ttf", 72)
gamemodeselect_text1_font = pg.font.Font("./Fonts/font.ttf", 64)
gamemodeselect_instruction1_font = pg.font.Font("./Fonts/font.ttf", 24)
gamemodeselect_instruction2_font = pg.font.Font("./Fonts/font.ttf", 18)
gamemodeselect_instruction3_font = pg.font.Font("./Fonts/font.ttf", 28)
gameover_text_font = pg.font.Font("./Fonts/font.ttf", 72)
gameover_text2_font = pg.font.Font("./Fonts/font.ttf", 24)
gameover_text3_font = pg.font.Font("./Fonts/font.ttf", 30)
highscore_text_font = pg.font.Font("./Fonts/font.ttf", 40)
# --- Colors to be used ---
white = (255, 255, 255)
red = (255, 0, 0)
dark_red = (102, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
dark_green = (0, 102, 0)
# --- Start ---
game_intro()

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
        self.rect.x = 175
        self.rect.y = 600
        #player initial health count
        self.phealth = 3
        #player power up count
        self.powerup = 0
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
    #player move right
    def moveRight(self, pixels):
        self.rect.x += pixels
    #player move left
    def moveLeft(self, pixels):
        self.rect.x -= pixels
    #player health minus one if damage taken
    def health(self, damage):
        if damage == True:
            self.phealth -= 1
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
    #play life display update at every frame
    def update(self):
        None
# --- Enemy-Related Classes ---
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
# --- Enemy 1 ---
class Enemy1(pg.sprite.Sprite):
    def __init__(self):
        super(Enemy1, self).__init__()
        #enemy 1 sprites/animation
        self.images = []
        self.images.append(pg.transform.scale(pg.image.load('space-image_e1_1.png'), (96, 100)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_e1_2.png'), (96, 100)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_e1_3.png'), (96, 100)))
        self.images.append(pg.transform.scale(pg.image.load('space-image_e1_4.png'), (96, 100)))
        self.index = random.randint(0,3) #randomize starting index(frame) to play
        self.image = self.images[self.index]
        #Enemy 1 position
        self.rect = self.image.get_rect()
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
        #powerup1 position
        self.rect = self.image.get_rect()
        self.x = 200
        self.y = 200
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
    #powerup1 action once consumed
    def consume(self):
        pg.mixer.Channel(1).play(pg.mixer.Sound('space-sound_powerup1.wav'))
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
    gameintro = True
    while gameintro == True: #loop while gameintro is still running
        for event in pg.event.get():
            if event.type == pg.QUIT: #quit game
                gameintro = False
            mouse = pg.mouse.get_pos() #check mouse position
            if event.type == pg.MOUSEBUTTONDOWN and 298 > mouse[0] > 198 and 450 > mouse[1] > 400: #start game
                gameintro = False
                gameplay = True
            if event.type == pg.MOUSEBUTTONDOWN and 298 > mouse[0] > 198 and 510 > mouse[1] > 460: #quit game
                gameintro = False
                gameplay = False
        # --- Draw The Screen ---
        screen.fill((0,0,0))
        button("Start", 32, (255, 255, 255), 198, 400, 100, 50, dark_green, green)
        button("Quit", 32, (255, 255, 255), 198, 460, 100, 50, dark_red, red)
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
    #initial highscore set to 0
    highscore = 0
    #launch/exit game base on choice
    if gameplay == True:
        game_play(gameplay, highscore)
    if gameplay == False:
        pg.quit()
        sys.exit()
# --- Game Play Loop ---
def game_play(gameplay, highscore):
    """
    Game loop that runs during actual gameplay.
    Args:
        gameplay: Loop if true
        highscore: Check and include previous attempt highscores if applicable
    """
    # --- Initial Setup ---
    # --- Sprite Groups Generation ---
    noninteractive_objects = pg.sprite.Group()
    interactive_objects = pg.sprite.Group()
    player_list = pg.sprite.Group()
    bullet_list = pg.sprite.Group()
    plife_list = pg.sprite.Group()
    enemy_list = pg.sprite.Group()
    enemy_e1_list = pg.sprite.Group()
    enemy_smallmeteor_list = pg.sprite.Group()
    powerup1_list = pg.sprite.Group()
    # --- Player/Player Life Generation ---
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
    damage = False
    # --- Time/Score Generation ---
    score = 0
    time_elapsed_since_pbullet = 0
    time_elapsed_since_e1spawn = 0
    time_elapsed_since_smallmeteorspawn = 0
    time_elapsed_since_bigmeteorspawn = 0
    time_elapsed_since_starsspawn = 0
    time_elapsed_since_powerup1spawn = 0
    time_elapsed_since_powerup1consume = 0
    gameplay = True
    while gameplay == True: #loop while gameplay is still running
        for event in pg.event.get():
            if event.type == pg.QUIT: #quit game
                gameplay = False
        # --- Player Management ---
        keypressed = pg.key.get_pressed() #player movement
        if keypressed[pg.K_LEFT]:
            ship.moveLeft(5)
        if keypressed[pg.K_RIGHT]:
            ship.moveRight(5)
        time_elapsed_since_pbullet += dt 
        if keypressed[pg.K_SPACE] and ship.phealth > 0 and time_elapsed_since_pbullet > 1500 and ship.powerup == 0: #player shoot without powerup
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
        elif keypressed[pg.K_SPACE] and ship.phealth > 0 and time_elapsed_since_pbullet > 1500 and ship.powerup == 1: #player shoot with powerup1
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
            bullet = Bullet()
            bullet.rect.x = ship.rect.x + 55
            bullet.rect.y = ship.rect.y - 20
            interactive_objects.add(bullet)
            bullet_list.add(bullet)
            time_elapsed_since_pbullet = 0
        # --- Spawn Management ---
        time_elapsed_since_starsspawn += dt #stars spawn
        if time_elapsed_since_starsspawn > random.randint(700, 1000):
            stars = Stars()
            stars.rect.x = random.randint(-20, 520)
            stars.rect.y = -100
            noninteractive_objects.add(stars)
            time_elapsed_since_starsspawn = 0
        time_elapsed_since_e1spawn += dt #enemy 1 spawn
        if time_elapsed_since_e1spawn > random.randint(8500, 10000):
            e1 = Enemy1()
            e1.rect.x = random.randint(-20, 520)
            e1.rect.y = -120
            interactive_objects.add(e1)
            enemy_list.add(e1)
            enemy_e1_list.add(e1)
            time_elapsed_since_e1spawn = 0
        time_elapsed_since_smallmeteorspawn += dt #small meteor spawn
        if time_elapsed_since_smallmeteorspawn > random.randint(5500, 7000):
            smallmeteor = Smallmeteor()
            smallmeteor.rect.x = random.randint(-20, 520)
            smallmeteor.rect.y = -100    
            interactive_objects.add(smallmeteor)
            enemy_list.add(smallmeteor)
            enemy_smallmeteor_list.add(smallmeteor)
            time_elapsed_since_smallmeteorspawn = 0
        time_elapsed_since_powerup1spawn += dt #powerup 1 spawn
        if time_elapsed_since_powerup1spawn > random.randint(480000, 550000):
            powerup1 = Powerup1()
            powerup1.rect.x = random.randint(0, 500)
            powerup1.rect.y = -100    
            interactive_objects.add(powerup1)
            powerup1_list.add(powerup1)
            time_elapsed_since_powerup1spawn = 0
        # --- Power Up Management ---
        if ship.powerup == 1:
            time_elapsed_since_powerup1consume += dt
            if time_elapsed_since_powerup1consume > 100000: #powerup1 duration
                ship.powerup = 0
                time_elapsed_since_powerup1consume = 0
        # --- Collision Management ---
        for hits in interactive_objects:
            meteorhits = pg.sprite.groupcollide(bullet_list, enemy_smallmeteor_list, True, True)  
            e1hits = pg.sprite.groupcollide(bullet_list, enemy_e1_list, True, True)
            playerhit = pg.sprite.groupcollide(player_list, enemy_list, False, True)
            powerup1hit = pg.sprite.groupcollide(player_list, powerup1_list, False, True)
            # --- Bullet Collision with Enemy ---
            for bullet_hit in meteorhits:
                asteroidex = Asteroidex()
                asteroidex.rect.x = bullet_hit.rect.x - 40
                asteroidex.rect.y = bullet_hit.rect.y - 50
                interactive_objects.add(asteroidex)
                score += 1
            for bullet_hit in e1hits:
                smallex = Smallex()
                smallex.rect.x = bullet_hit.rect.x - 30
                smallex.rect.y = bullet_hit.rect.y - 100
                interactive_objects.add(smallex)
                score += 5
            # --- Player Collision with Enemy ---
            for damage_taken in playerhit:
                pex = Pex()
                pex.rect.center = ship.rect.center
                interactive_objects.add(pex)
                damage = True
                ship.health(damage)
            # --- Player Collision with Power Up ---
            for playercontact in powerup1hit:
                powerup1.consume()
                ship.powerup = 1
        # --- Player Life Management ---
        if ship.phealth == 2:
            playerlife1.kill()
        if ship.phealth == 1:
            playerlife2.kill()
        if ship.phealth == 0:
            playerlife3.kill()
            ship.kill()
            e1.kill()
            smallmeteor.kill()
        # --- Draw The Screen ---
        screen.fill((0,0,0))
        noninteractive_objects.update()
        noninteractive_objects.draw(screen)
        interactive_objects.update()
        interactive_objects.draw(screen)
        plife_list.update()
        plife_list.draw(screen)
        highscoreboard = score_font.render("High Score: " + str(highscore), True, white)
        scoreboard = score_font.render("Score: " + str(score), True, white)
        screen.blit(scoreboard, (20, 50))
        screen.blit(highscoreboard, (20, 20))
        pg.display.flip()
        clock.tick(60) # 1 second = 9000 ticks
        # --- Game Over Management ---
        if ship.phealth <= 0:
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
                gameplay = False
                gameover = False
            mouse = pg.mouse.get_pos()
            if event.type == pg.MOUSEBUTTONDOWN and 230 > mouse[0] > 80 and 450 > mouse[1] > 400: #restart game
                gameplay = True
                gameover = False
            if event.type == pg.MOUSEBUTTONDOWN and 430 > mouse[0] > 280 and 450 > mouse[1] > 400: #quit game
                gameplay = False
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
    if gameplay == True:
        game_play(gameplay, highscore)
    if gameplay == False:
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
gameintro_instruction_font = pg.font.SysFont("Times", 18)
gameintro_instruction2_font = pg.font.SysFont("Comic Sans", 28)
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
dt = clock.tick()
game_intro()

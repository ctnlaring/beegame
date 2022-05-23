#collin and tobis bee game. 2022

#imports
import pygame, sys, random, os
from pygame.locals import *
from map_1 import map1

#pygame/screen setup
pygame.init()
screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption('Bee game')
pygame.key.set_repeat(100, 100)

#textures
grass = pygame.image.load("img/grass.png")
water = pygame.image.load("img/water.png")
mountian = pygame.image.load("img/mountian.png")

#map
terrains = [{"sprite": grass, "passable": True}, {"sprite": water, "passable": True}, {"sprite": mountian, "passable": False}]
themap = [[-1 for y in range(150)] for x in range (150)]
for x in range (0,150):
    for y in range (0,150):
        themap[y][x] = terrains[map1[y][x]]

#Passable -- rework to non-boolean for upgrades probably
def is_passable(map_x, map_y):
	return themap[int(map_y)][int(map_x)]["passable"]


#Bee class
class Bee(pygame.sprite.Sprite):
    def __init__(self):
        super(Bee, self).__init__()
        self.image = pygame.image.load('img/bee.png')
        self.rect = self.image.get_rect(
            center=(random.randint(0,1600),random.randint(0,900)))

    #Move randomly  
    def update(self):
        moves=[-64, 0, 64]
        self.rect.move_ip(random.choice(moves), random.choice(moves))

#Player class        
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('img/bee.png')
        self.rect = self.image.get_rect(
            center=(96,96))

    #Keys - will be redone
    def update(self, key):
        global yshift
        global xshift
        
        if key==1073741904: #Left
            if self.rect.left <= 64:
                self.rect.left=64
                xshift+=64
                playerx=self.rect.left-xshift
                playery=self.rect.top-yshift
                if not is_passable(playerx/64,playery/64):
                    xshift-=64           
            else:
                self.rect.move_ip(-64, 0)
                playerx=self.rect.left-xshift
                playery=self.rect.top-yshift
                if not is_passable(playerx/64,playery/64):
                    self.rect.move_ip(64,0)

                    
        if key==1073741903: #Right
            if self.rect.right >= 1600-64:
                self.rect.right=1600-64
                xshift-=64
                playerx=self.rect.left-xshift
                playery=self.rect.top-yshift
                if not is_passable(playerx/64,playery/64):
                    xshift+=64
            else:
                self.rect.move_ip(64, 0)
                playerx=self.rect.left-xshift
                playery=self.rect.top-yshift
                if not is_passable(playerx/64,playery/64):
                    self.rect.move_ip(-64,0)

                    
        if key==1073741906: #Up
            if self.rect.top <=64:
                self.rect.top = 64
                yshift+=64
                playerx=self.rect.left-xshift
                playery=self.rect.top-yshift
                if not is_passable(playerx/64,playery/64):
                    yshift-=64
            else:
                self.rect.move_ip(0, -64)
                playerx=self.rect.left-xshift
                playery=self.rect.top-yshift
                if not is_passable(playerx/64,playery/64):
                    self.rect.move_ip(0,64)

                    
        if key==1073741905: #Down
            if self.rect.bottom>=900-64:
                self.rect.bottom=900-64
                yshift-=64
                playerx=self.rect.left-xshift
                playery=self.rect.top-yshift
                if not is_passable(playerx/64,playery/64):
                    yshift+=64
            else:
                self.rect.move_ip(0, 64)
                playerx=self.rect.left-xshift
                playery=self.rect.top-yshift
                if not is_passable(playerx/64,playery/64):
                    self.rect.move_ip(0,-64)

        #beekeys
        if key==98: #B
            new_bee = Bee()
            all_sprites.add(new_bee)
            bees.add(new_bee)

        if key==107: #K
            for bee in bees:
                bee.kill()

#Setup sprite groups
all_sprites = pygame.sprite.Group()
bees = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
yshift=0
xshift=0

#Main loop
while True:
    pygame.time.delay(20)
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE: #Quit
                pygame.quit()
                sys.exit()
                os.exit()
                quit()
                exit()
            else:
                player.update(event.key) #Send keys to player.update
                                                
        elif event.type == QUIT: #Quit
            pygame.quit()
            sys.exit()
            os.exit()
            quit()
            exit()

    #update bees
    for bee in bees:
        bee.update()
        
    #collisions



    #Display map
    for x in range (0,150):
        for y in range (0,150):
            screen.blit(themap[y][x]["sprite"], [x*64+xshift,y*64+yshift])

    #render entities    
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        
    #flip
    pygame.display.flip()

#створи гру "Лабіринт"!
from pygame import *
from pygame.sprite import collide_rect
from pygame.transform import scale, flip
from pygame.image import load
from random import randint


class GameSprite(sprite.Sprite):
    def __init__(self, image, x, y, speed):
        super().__init__()
        self.image = load(image)
        self.image = scale(self.image, [60,60])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        
    def drow(self):
        window.blit(self.image,[self.rect.x,self.rect.y])
        
        
class Player(GameSprite):
    def move(self):
        keys =key.get_pressed() 
        if keys[K_UP]:
            self.rect.y -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed
        
    
class Enemy(GameSprite):
    direction = 'left'
    def move(self):
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        if self.rect.x <= 350:
            self.direction ='right'
        if self.rect.x >=600:
            self.direction = 'left'
        
    
    
mixer.init()
mixer.music.load("Logika/m5/maze/jungles.ogg")
mixer.music.play(-1)


width = 700
height = 500
window = display.set_mode([width,height])
background = load("Logika/m5/maze/background.jpg")
background = scale(background, [width,height])
clock = time.Clock()
FPS = 60

hero = Player("Logika/m5/maze/hero.png", 0, 0, 5)
cyborg = Enemy("Logika/m5/maze/cyborg.png", 550, 250, 5)
gold = GameSprite("Logika/m5/maze/treasure.png",550, 400, 0 )



game = True
while game == True:
    for e in event.get():
        if e.type== QUIT:
            game = False

    if collide_rect(hero, gold):
        print("you win")
        game = False
    
    if collide_rect(hero, cyborg):
        print("you lose")
        game = False

    window.blit(background,[0,0])
    hero.move()
    cyborg.move()
    hero.drow()
    cyborg.drow()
    gold.drow()
    display.update()
    clock.tick(60)

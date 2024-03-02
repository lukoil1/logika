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
game = True
while game == True:
    for e in event.get():
        if e.type== QUIT:
            game = False


    window.blit(background,[0,0])
    display.update()
    clock.tick(60)

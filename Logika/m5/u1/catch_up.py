from pygame import *

window = display.set_mode([700,500])
background = image.load("Logika/m5/u1/background.png")
background = transform.scale(background, [700,500])

sprite1= image.load("Logika/m5/u1/sprite1.png")
sprite1 = transform.scale(sprite1 , [100,100])
y1 = 350
x1 = 100
sprite2 = image.load("Logika/m5/u1/sprite2.png")
sprite2 = transform.scale(sprite2 , [100,100])
y2 = 350
x2 = 300  
clock = time.Clock()
FPS = 60
running=True
while running:
    for e in event.get(): 
        if e.type==QUIT:
            running=False
            quit()
    window.blit(background, [0,0])
    window.blit(sprite1,[x1,y1])
    window.blit(sprite2,[x2,y2])
    keys = key.get_pressed()
    if keys[K_UP]:
        y1 -= 10
    if keys[K_DOWN]:
        y1 += 10
    if keys[K_LEFT]:
        x1 -= 10
    if keys[K_RIGHT]:
        x1 += 10
            
    if keys[K_w]:
        y2 -= 10
    if keys[K_s]:
        y2 += 10
    if keys[K_a]:
        x2 -= 10
    if keys[K_d]:
        x2 += 10
        
    
    display.update()
    clock.tick(FPS)
    
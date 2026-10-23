import os

import pygame as pg

### SET-UP

os.chdir(os.path.dirname(os.path.abspath(__file__)))
pg.init()

#skjerm
pg.display.set_caption('IT2 spill-mal')
WIDTH = 500
HEIGHT = 500
# screen = pg.display.set_mode((0,0),pg.FULLSCREEN)
screen = pg.display.set_mode((WIDTH,HEIGHT))

#oppdateringsrate
FPS = 60
clock = pg.time.Clock()

#hoved-spill-løkke
run = True
lose = False
game_objects = []


### KLASSER

class GameObject:
    def __init__(self, x_pos=0, y_pos=0, color=(250,0,0)):
        self.x_size = 50    #piksler
        self.y_size = 50    #piksler

        self.img = pg.transform.scale(
            pg.image.load(
                'assets/space_invaders_ship.png'),
            (self.x_size,self.y_size))

        self.x_pos = x_pos
        self.y_pos = y_pos

        self.color = color  #RGB

        self.rect = pg.Rect(self.x_pos,self.y_pos,self.x_size, self.y_size)
    def draw(self):
        global screen

        self.rect.x = self.x_pos
        self.rect.y = self.y_pos
        
        #rect
        pg.draw.rect(screen, self.color, self.rect)

        #image
        screen.blit(self.img,(self.x_pos,self.y_pos))


### FUNKSJONER
def ai_actions():
    pass

def actions():
    global run
    events = pg.event.get()
    keys = pg.key.get_pressed()
    mouse_buttons = pg.mouse.get_pressed()
    mouse_pos = pg.mouse.get_pos()

    #player-actions
    if keys[pg.K_d]:
        p1.x_pos += 5
    if keys[pg.K_a]:
        p1.x_pos -= 5
    if keys[pg.K_s]:
        p1.y_pos += 5
    if keys[pg.K_w]:
        p1.y_pos -= 5

    #system shutdown
    if keys[pg.K_ESCAPE]:
        run = False

    for event in events:
        if event.type == pg.QUIT:
            run = False

def draw():
    global screen, game_objects

    screen.fill((45,60,100))

    for object in game_objects:
        object.draw()

    pg.display.update()

def win_con():
    global lose, p1
    if p1.rect.colliderect(cpu1):
        print("collision!")
        lose = True
    else:
        print("no collision")

### IN-GAME OBJECTS

cpu1 = GameObject(color=(0,250,0))

p1 = GameObject(100,100)

game_objects.append(p1)
game_objects.append(cpu1)


### GAME-LOOP

while run:
    ai_actions()
    
    actions()

    win_con()

    draw()

    clock.tick(FPS)

### TODO

#1) Lag sånn at man kan gå "alle" retninger med WASD
#2) Fix sånn at man ikke kan gå utenfor skjermen

#3A) Legg inn tyngdekraft, hvor man "hopper" med SPACE

#3B-1) Lag ett GameObject til: en "fiende" som bruker CPU-logikk til å 
#      prøve å fange spilleren
#3B-2) Lag ett condition for "du tapte" hvis du blir fanget av CPUen

#BONUS: FIXME normalisere hastigheten når man beveger seg diagonalt
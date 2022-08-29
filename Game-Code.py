import pgzrun                       # import pgzrun library
from random import randint          # import randint function we will use it to place Thanos ramdomly on screen


# Screen size
HEIGHT =500
WIDTH = 600

# Play background music
music.play("ironmantheme")

# define Actors
# Images of Actors should be stored in "images" folder
p = Actor("ironman", pos=(100,100))
c = Actor("thanos2",)

# Placing Thanos randomly on screen
c.x = randint(64, WIDTH-64)
c.y = randint(64, HEIGHT-64)
score = 0     # initializing score 0
speed = 5     # speed of Ironman


def draw():                 
    screen.clear()
    p.draw()          # draw Ironman
    c.draw()          # draw Thanos
    screen.draw.text(f'score:{score}',{WIDTH-80,10})    # draw text - score

def update():
    player_control()
    update_score()

def update_score():     # function to update score when Actors p and c collide
    global score
    if p.colliderect(c):
        sounds.shoot.play()
        score += 1
        c.pos = (randint(64,WIDTH-64),randint(64,HEIGHT-64))    # changing position after collision
        sounds.thanoslaugh.play()




def player_control():       # function to define Ironman movements
    print("updating")
    if keyboard.RIGHT and not p.right > WIDTH:
        p.angle=-10
        p.x += speed
    elif keyboard.LEFT and not p.left < 0:
        p.x += -speed
        p.angle=10
    elif keyboard.DOWN and not p.bottom > HEIGHT:
        p.y += speed
    elif keyboard.UP and not p.top < 0:
        p.y -= speed
    else:
        p.angle = 0

#outside function the fuction
pgzrun.go()

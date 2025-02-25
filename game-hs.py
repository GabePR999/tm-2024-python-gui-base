import pyglet
from pyglet.shapes import Rectangle, Circle
from pyglet.window import key
from random import randint

#windows config
window_width = 800
window_height = 600
window = pyglet.window.Window(width=window_width, height=window_height, caption="Foo Bar")

#color constants
GRAY = (169,169,169)
GREEN = (34,139,34)
WHITE = (255,255,255)
RED = (255,0,0,)
#player config
player_radius = 40
player_x = window_width / 2
player_y = 100
player_speed = 150

#This handles keyboard input
keys = key.KeyStateHandler()
window.push_handlers(keys)

player = Circle(player_x, player_y, player_radius, color=WHITE)


obstacle_size = 60
obstacle_speed = 200 
obstacles = []

def add_obstacle():
    x = randint(path_x, path_x + path_width - obstacle_size)
    obstacle = Rectangle (200, window_height-obstacle_size, obstacle_size, obstacle_size, RED)
    obstacles.apped (obstacle)

path_width = 400
path_x = (window_width - path_width)/2

background = Rectangle(0,0,window_width, window_height, GREEN )

path = Rectangle(path_x,0,path_width,window_height,GRAY)
dir = 'right'
def update(dt):

    if keys[key.LEFT]:
        player.x -= player_speed * dt
    if keys[key.RIGHT]:
        player.x += player_speed * dt

    if player.x > path_width+path_x-player_radius:
        player.x = path_width+path_x-player_radius

    if player.x < path_x+player_radius:
        player.x = path_x + player_radius

for obstacle in obstacles [:]:
    obstacle.y -= obstacle_speed * dt
    
    if obstacle.y + obstacle_size <0:
        obstacle.delete()
        obstacles.remove(obstacle)


obstacle_size = 60
obstacle_speed = 200 

obstacle = Rectangle (200, window_height-obstacle_size, obstacle_size, obstacle_size, RED)


#This moves the player left and right
    # if dir == 'right':
    #     player.x = player.x + player_speed * dt
    # elif dir == 'left':
    #     player.x = player.x - player_speed * dt

    # if player.x > path_width+path_x-player_radius and dir == 'right':
    #     dir = 'left'
    # elif player.x < path_x+player_radius and dir =='left':
    #     dir = 'right'

@window.event
def on_draw():
    window.clear()
    player.draw()    
    path.draw()  
    background.draw()
    for obstacle in obstacles[:]:
        obstacle.draw()

pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()
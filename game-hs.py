import pyglet
from pyglet.shapes import Rectangle, Circle
from pyglet.window import key
from pyglet.text import Label
from pyglet.sprite import Sprite
from pyglet.image import loadImage

from random import randint

#windows config
window_width = 800
window_height = 600
window = pyglet.window.Window(width=window_width, height=window_height, caption="My Game")

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

player_image = loadImage("./assets/tnka")

# This handles keyboard input
keys = key.KeyStateHandler()
window.push_handlers(keys)

player = Circle(player_x, player_y, player_radius, color=WHITE)
player_image = loadImage("./assets/tile_0048.png")
player = Sprite(player_image,x=player_x, y=player_y)
obstacle_size = 60
obstacle_speed = 200 
obstacles = []

obstacle_image = loadImage ("./assets/ tile_289.png")
def add_obstacle(dt):
    x = randint(int(path_x), int(path_x + path_width - obstacle_size))
    obstacle = Rectangle(x, window_height-obstacle_size,obstacle_size,obstacle_size,RED)
    obstacles.append(obstacle)

def check_collision():
    for obstacle in obstacles:
        if (player.x - player_radius < obstacle.x + obstacle.width and
            player.x + player_radius > obstacle.x and
            player.y - player_radius < obstacle.y + obstacle.height and
            player.y + player_radius > obstacle.y):
                return obstacle
    return None


path_width = 400
path_x = (window_width - path_width)/2

background = Rectangle(0,0,window_width, window_height, GREEN )

path = Rectangle(path_x,0,path_width,window_height,GRAY)

game_over_label = Label(
    'Game Over'
    font_size=36,
    x=window_width / 2,
    y=window_hight / 2,
    color=(255,0,0)
)

game_over = False

points_label = Label(
    'Points: 0',
    font_name='Arial',
    font_size=18,x=10,y=window_height-30
)


health = 100
health_label = Label(f"Health: {health}",
                    font_name="Arial",
                    font_size=18, x=10,y=window_height-60)

points = 0 
def update_points(dt):
    global points
    points += 1
    points_label.text = f'Points: {points}'

def update(dt):
    if keys[key.LEFT]:
        player.x -= player_speed * dt
    if keys[key.RIGHT]:
        player.x += player_speed * dt

    if player.x > path_width+path_x-player_radius:
        player.x = path_width+path_x-player_radius

    if player.x < path_x+player_radius:
        player.x = path_x + player_radius

    for obstacle in obstacles[:]:
        obstacle.y -= obstacle_speed * dt

        if obstacle.y + obstacle_size < 0:
            obstacle.delete()
            obstacles.remove(obstacle) 

    obstacle_hit = check_collision()
    if obstacle_hit:
        global health
        health -= 10
        health_label.text = f'Health: {health}'
        obstacles.remove (obstacle_hit)
        obstacle_hit.delete()
        if health <= 0:
            global game_over 
            game_over = True
@window.event
def on_draw():
    global game_over
    if game_over:
        game_over_label.draw

    window.clear()
    player.draw()    
    path.draw()  
    background.draw()
    for obstacle in obstacles[:]:
        obstacle.draw()
    points_label.draw()
    health_label.draw()

pyglet.clock.schedule_interval(update_points,1)
pyglet.clock.schedule_interval(add_obstacle, 2)
pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()
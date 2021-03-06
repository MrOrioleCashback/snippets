"""
3/11/16
Coursera, An Introduction to Interactive Programming in Python (Part 2), Rice University
Mini-project #7 - 'Spaceship'

copy code to http://www.codeskulptor.org/
"""

import simplegui, random, math 

# globals for user interface
SCREEN = (800, 600)
score = 0
lives = 3
time = 0

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated
    
# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        canvas.draw_image(ship_image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        ship_thrust_sound.pause(), ship_thrust_sound.rewind()
        if self.thrust:
            thrust_image_center = [self.image_center[0] + 90, self.image_center[1]]
            canvas.draw_image(ship_image, thrust_image_center, self.image_size, self.pos, self.image_size, self.angle)
            
    def update(self):
        self.angle += self.angle_vel
        for x in range(2): #keep in x, y range of screen
            self.pos[x] = (self.pos[x] + self.vel[x]) % SCREEN[x]
        self.vel = map(lambda x: x * .99, self.vel) #1% friction constant to x, y
        if self.thrust:
            for x in range(2):  #apply 25% thrust to x, y
                self.vel[x] += .25* angle_to_vector(self.angle)[x]
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.pause(), ship_thrust_sound.rewind()

    def shooty(self):
        global a_missile
        nose = angle_to_vector(self.angle)
        shot_nose_pos = [self.pos[0] + (self.radius * nose[0]), self.pos[1] + (self.radius * nose[1])] 
        shot_vel = [(nose[0] * 10) + self.vel[0], (nose[1] * 10) + self.vel[1]]
        shot_vector = math.atan2(shot_vel[1], shot_vel[0])
        a_missile = Sprite(shot_nose_pos, shot_vel, shot_vector, 0, missile_image, missile_info, missile_sound)
    
    def ship_angle_vel(self, x):
        my_ship.angle_vel = x

    def ship_thrust(self, x):
        my_ship.thrust = x
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind(), sound.play()
   
    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        
    def update(self):
        self.angle += self.angle_vel
        for x in range(2): #keep in x, y range of screen
            self.pos[x] = (self.pos[x] + self.vel[x]) % SCREEN[x]  

def draw(canvas):
    global time
    # animiate background
    time += 1
    wtime = (time / 4) % SCREEN[0]
    center, size = debris_info.get_center(), debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [SCREEN[0] / 2, SCREEN[1] / 2], [SCREEN[0], SCREEN[1]])
    canvas.draw_image(debris_image, center, size, (wtime - SCREEN[0] / 2, SCREEN[1] / 2), (SCREEN[0], SCREEN[1]))
    canvas.draw_image(debris_image, center, size, (wtime + SCREEN[0] / 2, SCREEN[1] / 2), (SCREEN[0], SCREEN[1]))

    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    a_missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    a_rock.update()
    a_missile.update()
    
    #draw score and lives 
    canvas.draw_text(str(score), (SCREEN[0] - 50, 50), 50, '#ffff00')
    canvas.draw_text(str(lives), (50, 50), 50, '#ffff00')
    
# timer handler that spawns a rock    
def rock_spawner():
    global a_rock
    rand_rock_pos = [SCREEN[0] * random.random(), SCREEN[1] * random.random()]
    rand_rock_vel = [random.random() * random.choice([1, -1]), random.random() * random.choice([1, -1])]
    a_rock = Sprite(rand_rock_pos, rand_rock_vel, 0, random.random()/10, asteroid_image, asteroid_info)

#controls
INPUTS = {'left': (lambda: my_ship.ship_angle_vel(-.08), lambda: my_ship.ship_angle_vel(0)), 
          'right': (lambda: my_ship.ship_angle_vel(.08), lambda: my_ship.ship_angle_vel(0)), 
          'up': (lambda: my_ship.ship_thrust(True), lambda: my_ship.ship_thrust(False)), 
          'space': (lambda: my_ship.shooty(), lambda: None)}

def keydown(key):
    for i in INPUTS:
        if key == simplegui.KEY_MAP[i]:
            INPUTS[i][0]()

def keyup(key):
    for i in INPUTS:
        if key == simplegui.KEY_MAP[i]:
            INPUTS[i][1]()

# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim

# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_brown.png")

# nebula images - nebula_brown.png, nebula_blue.png, nebula_blue.f2014.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_brown.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

#pulse 1 & 2 / missile image - shot1.png, shot2.png, shot3.png
pulse_info = ImageInfo([5,5], [10, 10], 3, 50) #<= shot1.png, shot2.png
pulse_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")
missile_info = ImageInfo([10,10], [20, 20], 3, 50) #<= shot3.png
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot3.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_brown.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.2)

ship_thrust_sound = simplegui.load_sound("http://giladayalonvegan.vkav.org/Python/thrust.mp3") 
ship_thrust_sound.set_volume(.4)
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
#soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# initialize ship and two sprites
my_ship = Ship([SCREEN[0] / 2, SCREEN[1] / 2], [0, 0], 0, ship_image, ship_info)
a_rock = Sprite([SCREEN[0] / 3, SCREEN[1] / 3], [1, 1], 0, .08, asteroid_image, asteroid_info)
a_missile = Sprite([-1, -1], [0,0], 0, 0, missile_image, missile_info)

# initialize frame
frame = simplegui.create_frame("Asteroids 4: Extreme Fatal Impact of Fury", SCREEN[0], SCREEN[1])

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()

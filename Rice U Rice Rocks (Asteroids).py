"""
3/16/16
Coursera, An Introduction to Interactive Programming in Python (Part 1), Rice University
Mini-project #8 - RiceRocks (Asteroids)
"""

import simplegui, random, math 

SCREEN = (800, 600)
started = False
EXPLOSION_CENTER = [64, 64]
EXPLOSION_SIZE = [128, 128]
EXPLOSION_DIM = 24
count = 0

def new_game():
    global rock_group, missile_group, explosion_group, my_ship, score, lives, time, soundtrack
    my_ship = Ship([SCREEN[0] / 2, SCREEN[1] / 2], [0, 0], 0, ship_image, ship_info)
    rock_group = set([])
    missile_group = set([])
    explosion_group = set([])
    score = 0
    lives = 3
    time = 0
    
class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False, ani_center = None, ani_size = None, ani_dim = None):
        self.center = center
        self.size = size
        self.radius = radius
        self.lifespan = lifespan if lifespan else float('inf')
        self.animated = animated
        self.ani_center = ani_center
        self.ani_size = ani_size
        self.ani_dim = ani_dim

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
    
    def get_ani_center(self):
        return self.ani_center

    def get_ani_size(self):
        return self.ani_size

    def get_ani_dim(self):
        return self.ani_dim
    
# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

def group_collide(group, other_object):
    global lives, explosion_group
    for item in set(group):
        if item.collide(other_object):
            explosion_group.add(Sprite(item.get_position(), (0,0), 0, 0, explosion_image, explosion_info, explosion_sound))
            group.remove(item)
            return True
        
def group_group_collide(group1, group2):
        for item in group1:
            if group_collide(group2, item):
                group1.remove(item)
                return True
            
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
        
    def get_position(self):
        return (self.pos[0], self.pos[1])
    
    def get_radius(self):
        return self.radius        
        
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
        missile_group.add(Sprite(shot_nose_pos, shot_vel, shot_vector, 0, missile_image, missile_info, missile_sound))
    
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
        self.ani_center = info.get_ani_center()
        self.ani_size = info.get_ani_size()
        self.ani_dim = info.get_ani_dim()
        self.age = 0
        if sound:
            sound.rewind(), sound.play()

    def get_position(self):
        return (self.pos[0], self.pos[1]) 
    
    def get_radius(self):
        return self.radius
   
    def draw(self, canvas):
        global count
        if self.animated:
            index = (count % self.ani_dim) // 1
            current_center = [self.ani_center[0] +  index * self.ani_size[0], self.ani_center[1]]
            canvas.draw_image(self.image, current_center, self.ani_size, self.pos, self.ani_size)
            count += 1
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    
    def update(self):
        self.angle += self.angle_vel
        for x in range(2): #keep in x, y range of screen
            self.pos[x] = (self.pos[x] + self.vel[x]) % SCREEN[x]
        self.age += 1
        return False if self.age < self.lifespan else True

    def collide(self, other_object):
        return dist(self.pos, other_object.pos) <= (self.radius + other_object.radius)          

def draw(canvas):
    global time, lives, score, started
    # animiate background
    time += 1
    wtime = (time / 4) % SCREEN[0]
    center, size = debris_info.get_center(), debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [SCREEN[0] / 2, SCREEN[1] / 2], [SCREEN[0], SCREEN[1]])
    canvas.draw_image(debris_image, center, size, (wtime - SCREEN[0] / 2, SCREEN[1] / 2), (SCREEN[0], SCREEN[1]))
    canvas.draw_image(debris_image, center, size, (wtime + SCREEN[0] / 2, SCREEN[1] / 2), (SCREEN[0], SCREEN[1]))
    
    def process_sprite_group(group):
        for item in group:
            item.draw(canvas)
            if item.update():
                group.remove(item)
    
    #collision results
    if group_collide(rock_group, my_ship):
        lives -= 1
        if lives == 0:
            started = False
            for item in rock_group:
                rock_group.remove(item)
        
    if group_group_collide(missile_group, rock_group):
        score += 100        

    # update/draw ship and sprites
    my_ship.draw(canvas)
    my_ship.update()
    process_sprite_group(explosion_group)
    process_sprite_group(missile_group)    
    process_sprite_group(rock_group)
    
    #draw score and lives 
    canvas.draw_text("Lives", [50, 50], 22, "Silver", "monospace")
    canvas.draw_text("Score", [680, 50], 22, "Silver", "monospace")
    canvas.draw_text(str(lives), [50, 80], 22, "Silver", "monospace")
    canvas.draw_text(str(score), [680, 80], 22, "Silver", "monospace")
    
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [SCREEN[0] / 2, SCREEN[1] / 2], 
                          splash_info.get_size())    
            
# timer handler that spawns a rock    
def rock_spawner():
    global rock_group
    if len(rock_group) < 12 and started:
        rand_rock_pos = [SCREEN[0] * random.random(), SCREEN[1] * random.random()]
        if dist(rand_rock_pos, my_ship.get_position()) > 80:
            rand_rock_vel = [random.random() * random.choice([1, -1]), random.random() * random.choice([1, -1])]
            rock_group.add(Sprite(rand_rock_pos, rand_rock_vel, 0, random.random()/10, asteroid_image, asteroid_info))

#controls
INPUTS = {'left': (lambda: my_ship.ship_angle_vel(-.08), lambda: my_ship.ship_angle_vel(0)), 
          'right': (lambda: my_ship.ship_angle_vel(.08), lambda: my_ship.ship_angle_vel(0)), 
          'up': (lambda: my_ship.ship_thrust(True), lambda: my_ship.ship_thrust(False)), 
          'space': (lambda: my_ship.shooty(), lambda: None)
         }

def keydown(key):
    for i in INPUTS:
        if key == simplegui.KEY_MAP[i]:
            INPUTS[i][0]()

def keyup(key):
    for i in INPUTS:
        if key == simplegui.KEY_MAP[i]:
            INPUTS[i][1]()

def click(pos):
    global started
    center = [SCREEN[0] / 2, SCREEN[1] / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        soundtrack.rewind(), soundtrack.play()
        new_game()
        
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
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True, [64, 64], [128, 128], 24)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_orange.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
soundtrack.set_volume(.4)
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.2)
ship_thrust_sound = simplegui.load_sound("http://giladayalonvegan.vkav.org/Python/thrust.mp3") 
ship_thrust_sound.set_volume(.6)
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")
explosion_sound.set_volume(.4)

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
#soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# initialize frame
frame = simplegui.create_frame("Asteroids 4: Extreme Fatal Impact of Fury", SCREEN[0], SCREEN[1])

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)
timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
new_game()
"""
2/20/16
Coursera, An Introduction to Interactive Programming in Python (Part 1), Rice University
Mini-project #4 - "Pong"
"""

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600 
HEIGHT = 400       
BALL_RADIUS = 5
PAD_WIDTH = 8
PAD_HEIGHT = 80

# spawn ball, initial velocity upwards towards the winner (scalable)
def spawn_ball(direction):
    global ball_pos, ball_vel
    if direction == 'left':
        ball_pos = [WIDTH/2, random.randrange(HEIGHT/2 - HEIGHT/8, HEIGHT/2 + HEIGHT/8)]
        ball_vel = [-random.randrange(2, 3), -random.randrange(1, 3)]
    elif direction == 'right':
        ball_pos = [WIDTH/2, random.randrange(HEIGHT/2 - HEIGHT/8, HEIGHT/2 + HEIGHT/8)]
        ball_vel = [random.randrange(2, 3), -random.randrange(1, 3)]

# define event handlers (scalable)
def new_game():
    rand_start = ('left', 'right')
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2, single_count, single_color, single_player, score1_color, score2_color
    spawn_ball(rand_start[random.randrange(0,2)])
    paddle1_pos = [5, HEIGHT/2 - PAD_HEIGHT/2] 
    paddle1_vel = [0, 0]
    paddle2_pos = [WIDTH - 5, HEIGHT/2 - PAD_HEIGHT/2]
    paddle2_vel = [0, 0]
    score1_color = '#FBDE03'
    score2_color = '#FBDE03'
    score1, score2, single_count = 0, 0, 0
    single_color = '#8c8c8c'
    single_player = False
                                 
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, single_count, score1_color, score2_color
    
    #canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest)
    canvas.draw_image(image, (600/2, 400/2), (600, 400), (WIDTH/2, HEIGHT/2), (WIDTH, HEIGHT)) 
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "#3F362A")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "#3F362A")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "#3F362A")
    
    # draw scores
    canvas.draw_text(str(score1),(WIDTH/2 - WIDTH/6, HEIGHT/5), 40, score1_color)
    canvas.draw_text(str(score2),(WIDTH/2 + WIDTH/6, HEIGHT/5), 40, score2_color)
    canvas.draw_text(str(single_count),(WIDTH/8, HEIGHT - HEIGHT/8), 40, single_color)    

    # draw ball
    canvas.draw_circle((ball_pos), BALL_RADIUS, 2, "#FEF596", "#FEF596")
    
    # draw paddles 
    canvas.draw_line((paddle1_pos[0], paddle1_pos[1]), (paddle1_pos[0], paddle1_pos[1] + PAD_HEIGHT), PAD_WIDTH, "#FEF596")
    canvas.draw_line((paddle2_pos[0], paddle2_pos[1]), (paddle2_pos[0], paddle2_pos[1] + PAD_HEIGHT), PAD_WIDTH, "#FEF596")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # update paddle's vertical position, keep paddle on the screen
    if 0 < paddle1_pos[1] + paddle1_vel[1] and paddle1_pos[1] + PAD_HEIGHT + paddle1_vel[1] < HEIGHT:
        paddle1_pos[1] += paddle1_vel[1]
    
    if 0 < paddle2_pos[1] + paddle2_vel[1] and paddle2_pos[1] + PAD_HEIGHT + paddle2_vel[1] < HEIGHT:
        paddle2_pos[1] += paddle2_vel[1]
    
    # single player cpu paddle tracking
    if single_player == True:
        paddle2_pos[1] = ball_pos[1] - PAD_HEIGHT / 2
        
    # determine whether paddle and ball collide
    hitsound = (hit1,hit2,hit3)
    if ball_pos[1] >= paddle1_pos[1] and ball_pos[1] <= paddle1_pos[1] + PAD_HEIGHT and ball_pos[0] - BALL_RADIUS - abs(ball_vel[0]) <= PAD_WIDTH + 2:
        hit1.rewind(), hit2.rewind(), hit3.rewind(), hitsound[random.randrange(0, 3)].play()
        ball_vel[0] = -1.1 * (ball_vel[0])
        #track single player hits
        if single_player == True:   			
            single_count += 1
        
    if ball_pos[1] >= paddle2_pos[1] and ball_pos[1] <= paddle2_pos[1] + PAD_HEIGHT and ball_pos[0] + BALL_RADIUS + abs(ball_vel[0]) >= WIDTH - PAD_WIDTH - 2:
        hit1.rewind(), hit2.rewind(), hit3.rewind(), hitsound[random.randrange(0, 3)].play()
        ball_vel[0] = -1.1 * (ball_vel[0])
    
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        wall.rewind(), wall.play()
        ball_vel[1] = - ball_vel[1]
        
    # track if player scores
    if ball_pos[0] < BALL_RADIUS + PAD_WIDTH:			#2 scores	
        score.rewind(), score.play()
        score2 += 1
        score1_color = '#E7450D' if score2 >= score1 +5 else score1_color
        score2_color = '#FBDE03' if score1 <= score2 +5 else score2_color
        spawn_ball('right')

    if ball_pos[0] > WIDTH - BALL_RADIUS - PAD_WIDTH:	#1 scores
        score.rewind(), score.play()
        score1 += 1
        score2_color = '#E7450D' if score1 >= score2 +5 else score2_color
        score1_color = '#FBDE03' if score2 <= score1 +5 else score1_color
        spawn_ball('left')
        
def reset():
    new_game()
    
def single_player():
    global single_player, single_color, single_count
    if single_player == True:
        single_player = False
        singlebutt.set_text("Start Single Player")
        single_color = '#8c8c8c'
        single_count = 0
    else:
        single_player = True
        single_color = '#FBDE03'
        singlebutt.set_text("Stop Single Player")

def keydown(key):
    speed = 5
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['W']:
        paddle1_vel[1] = -speed
    if key == simplegui.KEY_MAP['S']:
        paddle1_vel[1] = speed
    if key == simplegui.KEY_MAP['up']:    
        paddle2_vel[1] = -speed
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel[1] = speed

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['W'] or key == simplegui.KEY_MAP['S']:
        paddle1_vel[1] = 0
    if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']:    
        paddle2_vel[1] = 0
    
# create frame
frame = simplegui.create_frame("Pong 3: The A-Pong-alypse", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.add_button('Reset', reset, 200)
singlebutt = frame.add_button("Start Single Player", single_player, 200)

image = simplegui.load_image('http://i.imgur.com/Mb3cpmT.png')

frame.add_label('')
frame.add_label("Left Player Controls:")
frame.add_label("'W' & 'S' to move up and down.")
frame.add_label('')
frame.add_label("Right Player Controls:")
frame.add_label("'Up' & 'Down' arrows to move up and down.")

hit1 = simplegui.load_sound("https://freesound.org/data/previews/4/4383_4948-lq.mp3")
hit1.set_volume(0.4)
hit2 = simplegui.load_sound("https://freesound.org/data/previews/4/4384_4948-lq.mp3")
hit2.set_volume(0.4)
hit3 = simplegui.load_sound("https://freesound.org/data/previews/4/4377_4948-lq.mp3")
hit3.set_volume(0.4)
wall = simplegui.load_sound("https://www.freesound.org/data/previews/82/82242_661496-lq.mp3")
wall.set_volume(0.1)
score = simplegui.load_sound("https://www.freesound.org/data/previews/126/126422_1666767-lq.mp3")
score.set_volume(0.9)

# start frame
new_game()
frame.start()
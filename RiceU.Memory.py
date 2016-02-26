"""
2/25/16
Coursera, An Introduction to Interactive Programming in Python (Part 2), Rice University
Mini-project # 5 - 'Memory'
"""

import simplegui
import random

def new_game():
    global cards, exposed, state, turn, card1, card2, click1, click2, tick, match
    cards = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
    random.shuffle(cards)
    exposed = [False for i in range(16)]
    state, turn, card1, card2, click1, click2, tick = 0, 0, 0, 0, 0, 0, 0
    match = False
     
def mouseclick(pos):
    global exposed, state, card1, card2, click1, click2, turn, match
    click_index = pos[0]/50 + (pos[1]/100*4)
    if state == 0:      #game start
        click1 = click_index
        card1 = cards[click1]
        exposed[click1] = True
        state = 1
    elif state == 1 and not exposed[click_index]:
        click2 = click_index
        card2 = cards[click2]
        if card2 == card1:
            match = True
        exposed[click2] = True
        state = 2
        turn += 1
    elif not exposed[click_index]:
        if card1 != card2:
            exposed[click1] = False
            exposed[click2] = False
            exposed[click_index] = True
        click1 = click_index
        card1 = cards[click1]
        exposed[click1] = True
        state = 1
        
def draw(canvas):
    global cards, exposed, tick, match
    for i in range(16):
        if 0 <= i <= 3:     #if card in 1st row
            x, y = i, 0
        if 4 <= i <= 7:     #if card in 2nd row
            x, y = i-4, 100
        if 8 <= i <= 11:    #if card in 3rd row
            x, y = i-8, 200
        if 12 <= i <= 15:   #if card in 4th row
            x, y = i-12, 300
        canvas.draw_polyline(((50*x, y), (50*x, 100+y), (50*x + 50, 100+y), (50*x + 50, y)), 1, 'Black')
        if exposed[i]:
            canvas.draw_text(str(cards[i]), (50*x+15, 65+y), 40, 'Black')
        else:
            canvas.draw_polygon(((50*x, y), (50*x, 100+y), (50*x + 50, 100+y), (50*x + 50, y)), 2, 'Black', 'Grey')
            canvas.draw_polygon(((50*x+5, 50+y), (50*x+25, 90+y), (50*x + 45, 50+y), (50*x +25, 10+y)), 1, 'Black', 'Red')
            canvas.draw_text('M', (50*x+12, 60+y), 30, 'Black')
    label.set_text('Turn: ' + str(turn))
    #Splash on a successful 'match'
    if match and tick < 100:    
        timer.start()
        canvas.draw_text('Match!', (20, 220), 60, 'Yellow')
    elif match:
        timer.stop()
        tick = 0
        match = False
    #end-screen pop-up w/ total turns    
    if exposed == [True for i in range(16)]:
        canvas.draw_polygon(((10, 135), (10, 265), (190, 265), (190, 135)), 3, 'Black', 'White')
        canvas.draw_text('Turns:', (20, 185), 60, 'Black')
        canvas.draw_text(str(turn), (70, 255), 60, 'Black')
#timer for splash        
def timer():
    global tick
    tick += 1      

frame = simplegui.create_frame('Memory 2: MEMORY HARDER!', 200, 400)
label = frame.add_label('')
timer = simplegui.create_timer(10, timer)
frame.add_button('Reset', new_game)
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
frame.set_canvas_background('White')

new_game()
frame.start()
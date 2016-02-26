"""
2/25/16
Coursera, An Introduction to Interactive Programming in Python (Part 2), Rice University
Mini-project # 5 - "Memory"
"""

import simplegui
import random

def new_game():
    global cards, exposed, state, turn, card1, card2, click1, click2
    cards = [1,2,3,4,5,6,7,8]+[1,2,3,4,5,6,7,8]
    random.shuffle(cards)
    exposed = [False for i in range(16)]
    state, turn, card1, card2, click1, click2 = 0, 0, 0, 0, 0, 0
     
def mouseclick(pos):
    global exposed, state, card1, card2, click1, click2, turn
    if state == 0:
        card1 = cards[pos[0]/50]
        exposed[pos[0]/50] = True
        click1 = pos[0]/50
        state = 1
    elif state == 1:
        if not exposed[pos[0]/50]:
            card2 = cards[pos[0]/50]
            exposed[pos[0]/50] = True
            click2 = pos[0]/50
            state = 2
            turn += 1
    else:
        if not exposed[pos[0]/50]:
            if card1 == card2:
                pass
            else:
                exposed[click1] = False
                exposed[click2] = False
                exposed[pos[0]/50] = True
            card1 = cards[pos[0]/50]
            exposed[pos[0]/50] = True
            click1 = pos[0]/50
            state = 1
            
def draw(canvas):
    global cards, exposed
    for i in range(16):
        canvas.draw_polyline([[50*i, 0], [50*i, 100], [50*i + 50, 100], [50*i + 50, 0]], 1, 'Black')
        if exposed[i]:
            canvas.draw_text(str(cards[i]), (50*i+10, 65), 40, 'Black')
        else:
            canvas.draw_polygon([[50*i, 0], [50*i, 100], [50*i + 50, 100], [50*i + 50, 0]], 2, 'Black', 'Grey')
            canvas.draw_polygon([[50*i+5, 50], [50*i+25, 90], [50*i + 45, 50], [50*i +25, 10]], 1, 'Black', 'Red')
            canvas.draw_text('M', (50*i+12, 60), 30, 'Black')
    label.set_text("Turn: " + str(turn)) 
        
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
frame.set_canvas_background('White')

new_game()
frame.start()
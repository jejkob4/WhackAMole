from microbit import *
import time
import random
import music

# jednou (bez mezer bo to jebe kod do pici)
display.scroll('WAM!')

buttonA = Image('00700:'
                '09000:'
                '99987:'
                '09000:'
                '00700')

buttonB = Image('00700:'
                '00090:'
                '78999:'
                '00090:'
                '00700')

endgame = ('Game Over!')

element_list = [button_a, button_b]
       

def game_over(end):
    display.scroll(end)   

def odpocet_3():
        display.show('3')
        time.sleep(1)
        display.show('2')
        time.sleep(1)
        display.show('1')
        time.sleep(1)

def success_press():
            display.clear()
            display.show(Image.SKULL)
            time.sleep(2)
            display.clear()
    
def show_directions(img):
    display.show(img)
    time.sleep(2)

count = 0

#pořád
while True:
    display.scroll('Press logo to start!')
    music.play(music.ODE)
# game start (je to take dojebane no, delay je tu na picu)
# musis zmacknut logo
    if pin_logo.is_touched():
        while (count <3): 
            count = count + 1
            
            display.show(Image.HEART)
            time.sleep(1)
            display.clear()
            time.sleep(1)

            x = (random.choice(element_list))
        
            if x == button_a:
                y = buttonA
                show_directions(y)
            if x == button_b:
                y = buttonB
                show_directions(y)
            
            odpocet_3()
        
            if x.was_pressed():
                success_press()
        else:
            game_over(endgame)

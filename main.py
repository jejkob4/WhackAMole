from microbit import *
import time

# jednou (bez mezer bo to jebe kod do pici)
buttonA = Image('00700:'
                '09000:'
                '99987:'
                '09000:'
                '00700')

endgame = ('Game Over!')

display.scroll('Whack A Mole!')
def start_game(ximage):
    display.show(ximage)
#    if button_a
   
def game_over(end):
    display.scroll(end)    


#pořád
while True:
    if pin_logo.is_touched():
        display.show(Image.HEART)
        time.sleep(1)
        display.clear()
        time.sleep(1)
        start_game(buttonA)

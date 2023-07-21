import display
import time


screen = display.Screen(30, 20, True)
sprite = ["0 ██%0 ██€",0,0]
sprite_2 = ["1 █%0 ███€", 0,5]

x_velocity = 1
y_velocity = 0

while True:
    screen.start_frame()

    key = screen.get_key_pressed()
    if key == chr(27):
        screen.end_screen()
        break
    
    screen.add_sprite(sprite)
    screen.add_sprite(sprite_2)
    screen.show()
    screen.clear()
    if x_velocity != 0:
        sprite[1] = sprite[1] + x_velocity
        if sprite[1] == 28:
            x_velocity = 0
            y_velocity = 1
        elif sprite[1] == 0:
            x_velocity = 0
            y_velocity = -1

    elif y_velocity != 0:
        sprite[2] = sprite[2] + y_velocity
        if sprite[2] == 18:
            y_velocity = 0
            x_velocity = -1
        elif sprite[2] == 0:
            y_velocity = 0
            x_velocity = 1

    screen.end_frame()
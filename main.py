import display
import time

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = ["1 ▄%0 ▀▀▀€", self.x, self.y]
        self.bullets = []
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_sprite(self):
        return self.sprite
    
    def get_bullets(self):
        return self.bullets
    
    def add_bullet(self):
        self.bullets.append(Bullet(self.x + 1,self.y -1 ))
    
    def update_bullets(self):
        for i in self.bullets:
            i.move()
            if i.get_y() < 0:
                self.bullets.remove(i)
                del i
    
    def update_sprite(self):
        self.sprite[1] = self.x
        self.sprite[2] = self.y
    
    def move(self, direction):
        if direction == "LEFT":
                self.x -= 1

        elif direction == "RIGHT":
            self.x += 1

        self.update_sprite()


class Bullet:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = ["0 |€", self.x, self.y]
        self.velocity = 1

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def get_sprite(self):
        return self.sprite

    def update_sprite(self):
        self.sprite[1] = self.x
        self.sprite[2] = self.y

    def move(self):
        self.y -= 1
        self.update_sprite()



screen = display.Screen(48, 24, True)

if __name__ == "__main__":

    player = Player(23, 22)

    while True:
        screen.start_frame()

        key = screen.get_key_pressed()
        if key:
            if key == chr(27):
                screen.end_screen()
                break

            elif key in ["a","A"]:
                if player.get_x() > 0:
                    player.move("LEFT")

            elif key in ["d","D"]:
                if player.get_x() < 45:
                    player.move("RIGHT")

            elif key in ["w","W"]:
                if len(player.get_bullets()) < 1:
                    player.add_bullet()

        
        screen.add_sprite(player.get_sprite())

        for i in player.get_bullets():
            screen.add_sprite(i.get_sprite())

        player.update_bullets()
        
        screen.show()
        screen.clear()

        screen.end_frame()
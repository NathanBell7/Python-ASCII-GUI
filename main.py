import display
import time

class Enemies:

    def __init__(self, number_enemies):
        self.enemies_array = []
        for i in range(number_enemies):
            self.enemies_array.append(Enemy(4, 4))


    def get_enemies(self):
        return self.enemies_array
    
    def delete_enemy(self, enemy):
        self.enemies_array.remove(enemy)
        del enemy


class Enemy:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = ["0 ▄▄▄%0 ▀▀▀€", self.x, self.y]

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def get_sprite(self):
        return self.sprite
    
    

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

    def delete_bullet(self, bullet):
        self.bullets.remove(bullet)
        del bullet
    
    def update_bullets(self):
        for i in self.bullets:
            i.move()
            if i.get_y() < 4:
                self.delete_bullet(i)
    
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


def collision(bullets, enemies):
    for i in bullets:
        for j in enemies:
            if i.get_x() >= j.get_x() and i.get_x() <= j.get_x() + 2 and i.get_y() <= j.get_y() + 1 and i.get_y() >= j.get_y():
                return i, j
    return None

screen = display.Screen(48, 24, True)

if __name__ == "__main__":

    player = Player(23, 22)

    enemies = Enemies(1)

    score = 0

    score_bar = ["0 ┌──────────────────────────────────────────────┐%0 │                                              │%0 └──────────────────────────────────────────────┘€", 0, 0]

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

        screen.add_sprite(score_bar)

        screen.add_sprite(["0 " + str(score) + "€", 1, 1])

        screen.add_sprite(player.get_sprite())

        for i in player.get_bullets():
            screen.add_sprite(i.get_sprite())

        for i in enemies.get_enemies():
            screen.add_sprite(i.get_sprite())


        player.update_bullets()

        check_collision = collision(player.get_bullets(), enemies.get_enemies())

        if check_collision:
            player.delete_bullet(check_collision[0])
            enemies.delete_enemy(check_collision[1])
            score += 1
        
        screen.show()
        screen.clear()

        screen.end_frame()
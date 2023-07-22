import display
import time

class Enemies:

    def __init__(self, number_enemies, FUM = 120):
        self.enemies_array = []

        self.left_boundary = 0
        
        self.right_boundary = 44

        self.FUM = FUM# Frames until move

        self.move_counter = self.FUM

        self.velocity = 1

        

        self.enemies_fill(number_enemies)

    def enemies_fill(self, number_enemies):
        self.highest_right = 42
        self.lowest_left = 2
        x = 2
        y = 4
        for i in range(number_enemies):
            self.enemies_array.append(Enemy(x, y))
            x += 8
            if x == 50:
                x = 2
                y += 4

    def get_enemies(self):
        return self.enemies_array
    
    def get_move_counter(self):
        return self.move_counter
    
    def decrease_move_counter_max(self):
        if self.FUM > 10:
            self.FUM -= 3
    
    #TODO implement updating new lowest left and highest right when enemy is killed
    def delete_enemy(self, enemy):
        self.enemies_array.remove(enemy)
        del enemy
        lowest = 100000
        highest = -1
        
        for i in self.enemies_array:
            if i.get_x() < lowest:
                lowest = i.get_x()
            if i.get_x() > highest:
                highest = i.get_x()

        self.lowest_left = lowest
        self.highest_right = highest

    def move_enemies(self):
        if self.velocity == 1:
            if self.highest_right != self.right_boundary:
                for i in self.enemies_array:
                    i.move_x(self.velocity)
                self.highest_right += self.velocity
                self.lowest_left += self.velocity
            else:
                self.velocity = -1
                for i in self.enemies_array:
                    i.move_y(1)

        elif self.velocity == -1:
            if self.lowest_left != self.left_boundary:
                for i in self.enemies_array:
                    i.move_x(self.velocity)
                self.highest_right += self.velocity
                self.lowest_left += self.velocity
            else:
                self.velocity = 1
                for i in self.enemies_array:
                    i.move_y(1)

    def reset_move_counter(self):
        self.move_counter = self.FUM

    def update_move_counter(self):
        self.move_counter -= 1


class Enemy:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = ["0 ▄▄▄▄%0 ▀▀▀▀€", self.x, self.y]

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def get_sprite(self):
        return self.sprite
    
    def update_sprite(self):
        self.sprite[1] = self.x
        self.sprite[2] = self.y

    def move_x(self, velocity):
        self.x += velocity
        self.update_sprite()

    def move_y(self, velocity):
        self.y += velocity
        self.update_sprite()
    
    

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
                self.x -= 2

        elif direction == "RIGHT":
            self.x += 2

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
            if i.get_x() >= j.get_x() and i.get_x() <= j.get_x() + 3 and i.get_y() <= j.get_y() + 1 and i.get_y() >= j.get_y():
                return i, j
    return None

screen = display.Screen(48, 24, True)

if __name__ == "__main__":

    player = Player(23, 22)

    enemies = Enemies(12, 30)

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
            if len(enemies.get_enemies()) == 0:
                enemies.enemies_fill(12)
                enemies.decrease_move_counter_max()
                enemies.reset_move_counter()


        if enemies.get_move_counter() == 0:
            enemies.move_enemies()
            enemies.reset_move_counter()
        
        screen.show()
        screen.clear()

        enemies.update_move_counter()
        screen.end_frame()
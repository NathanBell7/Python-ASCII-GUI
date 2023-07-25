import os
import cursor
import time
import msvcrt

class Screen:

    def __init__(self, width, height, border, FPS = 120):
        self.width = width
        self.height = height
        self.boundary_string_top = "┌"
        self.boundary_string_bottom = "└"
        self.empty_background_row = ""
        self.return_string = ""
        self.display = []
        self.border = border
        self.FPS = FPS
        self.time_per_frame = 1/self.FPS
        self.timer = 0
        self.terminal_width = os.get_terminal_size().columns
        self.terminal_height = os.get_terminal_size().lines
        os.system("clear")
        cursor.hide()
        print(" ")

        for i in range(self.width):
            self.boundary_string_top += "─"
            self.boundary_string_bottom += "─"
            self.empty_background_row += " "
        if self.border == True:
            for i in range(self.height + 3):
                self.return_string += "\033[A"
        else:
            for i in range(self.height + 1):
                self.return_string += "\033[A"

        self.boundary_string_top += "┐        "
        self.boundary_string_bottom += "┘"

        for i in range(self.height):
            self.display.append(self.empty_background_row)


    def show(self):
        new_terminal_width = os.get_terminal_size().columns
        if new_terminal_width != self.terminal_width:
            os.system("clear")
            print(" ")
            self.terminal_width = new_terminal_width

        new_terminal_height = os.get_terminal_size().lines
        if new_terminal_height != self.terminal_height:
            os.system("clear")
            print(" ")
            self.terminal_height = new_terminal_height

        if self.border != True:
            for i in range(len(self.display)):
                print(self.display[i][:self.terminal_width])
                if i >= self.terminal_height - 3:
                    break
            print(self.return_string)
        else:
            print(self.boundary_string_top[:self.terminal_width])
            for i in range(len(self.display)):
                print(("│" + self.display[i][:self.width] + "│")[:self.terminal_width])
                if i >= self.terminal_height - 5:
                    break
            print(self.boundary_string_bottom[:self.terminal_width])
            print(self.return_string[:self.terminal_height*5])


    def clear(self):
        pos = 0
        for i in range(len(self.display)):
            self.display[pos] = self.empty_background_row
            pos += 1

    
    def add_sprite(self, sprite):
        pointer = 0
        sprite_string = sprite[0]
        x_offset = sprite[1]
        y_offset = sprite[2]
        adding_sprite = True
        while adding_sprite:
            pointer_buffer = ""
            getting_offset = True
            while getting_offset:
                if sprite_string[pointer] != " ":
                    pointer_buffer += sprite_string[pointer]
                    pointer += 1
                else:
                    pointer += 1
                    getting_offset = False
            offset = int(pointer_buffer)

            pointer_buffer = ""
            getting_printable = True
            while getting_printable:
                if sprite_string[pointer] not in ["%", "€"]:
                    pointer_buffer += sprite_string[pointer]
                    pointer += 1
                else:
                    getting_printable = False
                    if sprite_string[pointer] == "€":
                        adding_sprite = False
                    pointer += 1
            if y_offset < len(self.display):
                self.display[y_offset] = self.display[y_offset][0:x_offset+offset] + pointer_buffer +  self.display[y_offset][x_offset+offset+len(pointer_buffer):]
            y_offset += 1


    def start_frame(self):
        self.timer = time.perf_counter()


    def end_frame(self):
        waiting = True
        while waiting:
            if time.perf_counter() - self.timer >= self.time_per_frame:
                waiting = False
            else:
                pass
        return True
    

    #TODO Only works on windows atm, add linux support
    def get_key_pressed(self):
        if msvcrt.kbhit():
            try:
                return bytes.decode(msvcrt.getch())
            except UnicodeDecodeError:
                return None
        return None
        

    def end_screen(self):
        os.system("clear")
        cursor.show()


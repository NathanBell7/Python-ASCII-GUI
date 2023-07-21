# ASCII GUI for Python

## This project is a simple python text based GUI that can be integrated into a variety of projects

&nbsp;

## __Features:__

### - It can display to the screen via the use of a custom sprite format
### - It has been designed to be as easy to understand as possible for the user
### - It can get non buffered keyboard inputs
### - It can be displayed bordered or borderless
### - It can lock loops to a given framerate

&nbsp;

## __Classes:__

### - Screen(width, height, border, FPS)

&nbsp;

## __Functions:__

### - add_sprite(sprite)
>### Adds a sprite to the screen buffer to be printed on the next show() function call.
>&nbsp;
>### Sprite structure [sprite_string, x_position, y_position]:
>### - sprite_string - The sprite itself
>>### The sprite_string, as implied by the name, is a string representation of the sprite.
>>### Here is an example of a sprite string("1 █%0 ███€") and its resut when printed:
>>### 
>>### &ensp;&ensp;&ensp;&ensp;█
>>### &ensp;&ensp;&ensp;███
>>### The sprite is read in "rows"
>>### The number at the start of each "row" tells the screen how many characters offset from the x this row should start printing
>>### The space after the number tells the screen to start looking for the characters to print
>>### In this case the character to print on row one is █
>>### Then the final character of a row is % to mark the end of the row, unless it's the final row, in which case it should be ended with a €
>### - x_position - The x position of the sprite(left to right)
>### - y_position - The y position of the sprite(top to bottom)

### - show()
>### Prints out the current state of the screen

### - clear()
>### Clears the screen buffer

### - start_frame()
>### Marks the start of the current frame(should be used at the start of a loop)

### - end_frame()
>### Marks the end of the current frame(should be used at the end of a loop)

### - get_key_pressed() - Currently Windows only
>### Returns the key pressed in a given frame when called

### - end_screen()
>### Clears screen and returns console to normal, should be called before exiting the program in which the screen has been used
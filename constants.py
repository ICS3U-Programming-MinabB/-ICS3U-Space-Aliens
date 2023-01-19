#!/usr/bin/env python3

# Created by: Minab Berhane
# Created on: Dec. 14, 2022

#storage of all important numbers
SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_ALIENS = 5
TOTAL_NUMBER_OF_LASERS = 5
SHIP_SPEED = 3
ALIEN_SPEED = 1
LASER_SPEED = 2
OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
OFF_TOP_SCREEN = -1 * SPRITE_SIZE
OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE
FPS = 60

# makes sure that the sprite can only move ant one grid per input
SPRITE_MOVEMENT_SPEED = 1
 
# for button state
button_state = { "button_up": "up",
"button_just_pressed": "just pressed",
"button_still_pressed": "still_pressed",
"button_released": "released"
 
}
RED_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
 
              b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
 

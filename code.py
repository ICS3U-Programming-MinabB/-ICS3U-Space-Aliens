#!/usr/bin/env python3

# Created by: Minab Berhane
# Created on: Dec. 14, 2022
# This program is for space alien in the PyBadge

import ugame
import stage


def game_scene():
    # this is the main scene for space alien

    #image bank for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    #set the background to image 0 in the image bank
    #   and the size
    background = stage.Grid(image_bank_background, 23, 8)

    #create a stage for the background to show up on
    #   and set the frame rate to 60 fps
    game = stage.Stage(ugame.display, 60)
    #set the layers of all the sprites, items show up in order
    game.layer = [background]
    #render all sprites
    game.render_block()

    #repeat forever game loop
    while True:
        pass

if __name__ == "__main__":
    game_scene()
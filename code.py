#!/usr/bin/env python3
 
# Created by: Minab Berhane
# Created on: Dec. 14, 2022
# This program is for space alien in the PyBadge
 
import ugame
import stage

import constant

def menu_scene():
    # main menu scene 

    #image bank for the pybadge
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    # text that is to be shown in menu scene 
    #intro screen
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constant.RED_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("Deadly Mouse Studios")
    text.append(text1)
    #Options menu
    text2 = stage.Text(width=29, height=12, font=None, palette=constant.RED_PALETTE, buffer=None)
    text2.move(30, 60)
    text2.text("Space Bomber")
    text.append(text2)
    text3 = stage.Text(width=29, height=12, font=None, palette=constant.RED_PALETTE, buffer=None)
    text3.move(40, 110)
    text3.text("Press start")
    text.append(text3)
    #set the background to image 0 in the image bank and the size (10x8 tiles of size 16)

    background = stage.Grid(image_bank_background, constant.SCREEN_GRID_X, constant.SCREEN_GRID_Y)

    #set the frame rate to 60 fps
    game = stage.Stage(ugame.display, constant.FPS)
    #set the layers of all the sprites, items show up in order
    game.layers = text + [background]
    #render all sprites
    game.render_block()

    #repeat forever game loop
    while True:
        #get user input
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_START:
            game_scene()
        game.tick()

 
def game_scene():
    # this is the main scene for space alien

    #buttons you want to keep information on
    a_button = constant.button_state["button_up"]
    b_button = constant.button_state["button_up"]
    start_button = constant.button_state["button_up"]
    select_button = constant.button_state["button_up"]
 
    #get sound ready
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

 
    #image bank for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprite = stage.Bank.from_bmp16("space_aliens.bmp")
 
    #set the background to image 0 in the image bank
    #   and the size
    background = stage.Grid(image_bank_background, constant.SCREEN_GRID_X, constant.SCREEN_GRID_Y)
 
    #a sprite that will update every frame
    ship = stage.Sprite(image_bank_sprite, 5, 75, constant.SCREEN_Y - (2 * constant.SPRITE_SIZE))
    alien = stage.Sprite(image_bank_sprite, 9, int(constant.SCREEN_X / 2 - constant.SPRITE_SIZE / 2 ), 16)
 
    #create a stage for the background to show up on
    #   and set the frame rate to 60 fps
    game = stage.Stage(ugame.display, constant.FPS)
    #set the layers of all the sprites, items show up in order
    game.layers = [ship]+ [alien] + [background]
    #render all sprites
    game.render_block()
 
    #repeat forever game loop
    while True:
        #get user input
        keys = ugame.buttons.get_pressed()

        #A button to fire
        if keys & ugame.K_X != 0:
            if a_button == constant.button_state["button_up"]:
                a_button = constant.button_state["button_just_pressed"]
            elif a_button == constant.button_state["button_just_pressed"]:
                a_button = constant.button_state["button_still_pressed"]
        else:
            if a_button == constant.button_state["button_still_pressed"]:
                a_button = constant.button_state["button_released"]
            else:
                a_button = constant.button_state["button_up"]
        # B button
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            print("Start")
        if keys & ugame.K_SELECT:
            print("Select")
        #input to make the sprite move
        if keys & ugame.K_RIGHT:
            if ship.x <= constant.SCREEN_X - constant.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(constant.SCREEN_X - constant.SPRITE_SIZE, ship.y)
        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass
 
 
        #update game logic
        #play a sound in A was just pressed
        if a_button == constant.button_state["button_just_pressed"]:
            sound.play(pew_sound)
        #redraw sprite
        game.render_sprites([ship] + [alien])
        game.tick()        
 
if __name__ == "__main__":
    menu_scene()
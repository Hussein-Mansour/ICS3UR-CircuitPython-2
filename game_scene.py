#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Mon/May3/2021
# This program is the "space aliens" on the pyBadge


import ugame
import stage


def game_scene():
    # this function is the main game game_scene

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # set the background to image 0 in the image bank
    # and the size (10x8 titels of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)

    # create a stage for the background to show up on
    # set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layer of all sprites, items show up in order
    game.layers = [background]

    # render all sprites
    # most likely you will only render the background once per gaem scene
    game.render_block()

    # repeat for ever, loop
    while True:
        pass


if __name__ == "__main__":
    game_scene()

from picraft import World, Vector, Block, O, X, Y, Z, line, lines, filled
from time import sleep, time
from random import randint,choice


import ConfigParser


config = ConfigParser.ConfigParser()

config.read('config.properties')
hostname = config.get('PiCraft','hostname');

w = World(host=hostname)

#allow time to go back to the game
sleep(3)

origin = Vector(45,7,-9);

## Build stares

base_of_stairs = [origin, origin + 3*X]

w.blocks[origin+2*Y] = Block("sponge")
for y in range(0, 10):
    left_stair = base_of_stairs[0] + y*Z + y*Y
    right_stair = base_of_stairs[1] + y*Z + y*Y
    stairs = list(line(left_stair, right_stair))
    w.blocks[stairs] = Block("planks")

    w.blocks[left_stair, right_stair] = Block("stone")
    w.blocks[left_stair + 1*Y, right_stair + 1*Y] = Block("fence")
    w.blocks[left_stair + 2*Y, right_stair + 2*Y] = Block("glowstone")



pos_queue = []
while(True):
    ## add X/Z restrictions too

    if(w.player.tile_pos.y > 17):
        pos = w.player.tile_pos - (w.player.tile_pos.y - 16)*Y
        positions = [
        pos,
        pos + 1*X,
        pos - 1*X,
        pos + 1*Z,
        pos - 1*Z,
        pos + 1*X + 1*Z,
        pos + 1*X - 1*Z,
        pos - 1*X + 1*Z,
        pos - 1*X - 1*Z,
        pos + 2*X,
        pos - 2*X,
        pos + 2*Z,
        pos - 2*Z]
        pos_queue.append(positions)

        w.blocks[positions] = Block("ice")

        num_blocks = len(positions) + 30


        print(str(len(pos_queue)) + " > " + str(num_blocks))

        while(len(pos_queue) > num_blocks):
            w.blocks[pos_queue.pop(0)] = Block("air")

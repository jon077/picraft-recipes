from picraft import World, Vector, Block, O, X, Y, Z, line, lines, filled
from time import sleep

import ConfigParser


config = ConfigParser.ConfigParser()

config.read('config.properties')
hostname = config.get('PiCraft','hostname');

w = World(host=hostname)


#allow time to go back to the game
sleep(3)


def eyes(player_pos):
    height = player_pos + 15*Y
    left_eye = height + -3*Z
    right_eye = height + 3*Z


    for eye in (right_eye,left_eye):
        yield list(filled([
            eye,
            eye + -1*Y,
            eye + 1*Z,
            eye + 1*Z + -1*Y]))

def smile(player_pos):
    print("smile")

    height = player_pos + 9*Y

    left_anchor = height - 3*Z
    right_anchor = height + 4*Z

    yield list(line(left_anchor, right_anchor))
    yield list(line(left_anchor, left_anchor - 2*Z + 2*Y))
    yield list(line(right_anchor, right_anchor + 2*Z + 2*Y))


## render list of blocks
blocks = list(eyes(w.player.tile_pos))
blocks.extend(smile(w.player.tile_pos))


## Render

w.say('Don\'t worry.  Be Happy!')
print("Rendering blocks: " + str(blocks))
with w.connection.batch_start():
    for p in blocks:
        w.blocks[p] = Block('gold_block')

##sleep 10 seconds
sleep(10)

## erase
print("Erasing blocks: " + str(blocks))
with w.connection.batch_start():
    for p in blocks:
        w.blocks[p] = Block('air')

w.say('See you next time!')

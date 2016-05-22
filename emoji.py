from picraft import World, Vector, Block, O, X, Y, Z, line, lines, filled
from time import sleep
from random import randint

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
    height = player_pos + 9*Y

    left_anchor = height - 3*Z
    right_anchor = height + 4*Z

    yield list(line(left_anchor, right_anchor))
    yield list(line(left_anchor, left_anchor - 2*Z + 2*Y))
    yield list(line(right_anchor, right_anchor + 2*Z + 2    *Y))




## Render
def render(blocks):
    with w.connection.batch_start():
        for p in blocks:
            w.blocks[p] = Block('gold_block')


def erase(blocks):
    ## erase
    with w.connection.batch_start():
        for p in blocks:
            w.blocks[p] = Block('air')



#location to put genie
pos = Vector(22,7,-3)
print("pos: " + str(pos))

##define bounds
low_corner = pos - 5*X - 5*Z
high_corner = pos + 5*X + 5*Z

ran_x = 0
ran_z = 0

state = "UNKNOWN"

print("low_corner: " + str(low_corner))
print("high_corner: " + str(high_corner))


blocks = list(eyes(pos))
blocks.extend(smile(pos))


while(True):

    ### Determine how to know if a host player exists
    player_pos = w.player.tile_pos
    print(player_pos)
    if(low_corner.x < player_pos.x and
       low_corner.z < player_pos.z and
       high_corner.x > player_pos.x and
       high_corner.z > player_pos.z ):

       render(blocks)

       if(state == "HIDDEN"):
           print("[%s,%s] [%s,%s]" % (ran_x, ran_z, player_pos.x, player_pos.z ))

           if(player_pos.x == ran_x and player_pos.z == ran_z):
               w.say("Congratulations!  Enjoy.  Come back soon!")
               w.blocks[player_pos - Y] = Block('diamond_block')

               erase(blocks)
               state = "UNKNOWN"
               sleep(120)

       if(state == "ASK"):
           w.say("I've hidden a treat nearby.  Look for it.")
           ran_x = randint(low_corner.x+1,high_corner.x-1)
           ran_z = randint(low_corner.z+1,high_corner.z-1)

           state = "HIDDEN"

       if(state == "UNKNOWN"):
           w.say("Hello.  Would you like a gift?")
           state = "ASK"

           sleep(3)

       print "[" + str(w.player.tile_pos) +  "]: " + state

    else:
        if(state == "HIDDEN"):
            w.say("Better luck next time.")
        elif(state != "UNKNOWN"):
            w.say("See ya later, alligator.")

        erase(blocks)
        state = "UNKNOWN"
        sleep(1)

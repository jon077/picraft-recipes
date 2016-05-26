from picraft import World, Vector, Block, O, X, Y, Z, line, lines, filled
from time import sleep, time
from random import randint,choice
import ConfigParser

config = ConfigParser.ConfigParser()

config.read('config.properties')
hostname = config.get('PiCraft','hostname');

w = World(host=hostname)


count = 0
for i in reversed(range(0,30)):
    origin = Vector(67,-2,128) + count*Y + count*X + count*Z;
    print("o: %s" % str(origin))
    side = (2*i)
    print("side: %s" % side)

    corner1 = origin + side*X
    corner2 = origin + side*X + side*Z
    corner3 = origin + side*Z
    corners = [origin, corner1, corner2, corner3]

    count = count + 1

    row = lines(corners)

    if(True):
        w.blocks[row] = Block("sandstone")
        w.blocks[corners] = Block("iron_block")
    else:
        w.blocks[row] = Block("air")

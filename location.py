from picraft import World, Vector, Block, O, X, Y, Z, line, lines, filled
from time import sleep, time
from random import randint,choice
import ConfigParser

config = ConfigParser.ConfigParser()

config.read('config.properties')
hostname = config.get('PiCraft','hostname');

w = World(host=hostname)

while(True):
    print(w.player.tile_pos)

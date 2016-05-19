import ConfigParser
from picraft import *

config = ConfigParser.ConfigParser()

config.read('config.properties')
hostname = config.get('PiCraft','hostname');




world = World(host=hostname)

world.say('Hello World!') 

print 'Done.'

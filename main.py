# Dungeon Crawler
# Ver 0.0.4
# 2013.05.01
# Authors: Michel Rouly
#          Adam Wood

from tile import Tile
from inputhandler import *
from item import Item
from util import *


current_tile = init_map("init.tile")

def parse_system_command( command, args ):
  global current_tile
  
  # COMMAND: HELP
  # Prints out the list of all interpretable commands.
  # todo: help <command>
  if command == HELP:
    try:
      target = args[0]
      if target in known_commands:
        print( "Help for <%s>." % target )
      else:
        print( "Unknown target command <%s>." % target )
    except IndexError:
      print( "Known commands:" )
      for cmd in known_commands:
        print( "\t", cmd )
  
  # COMMAND: QUIT
  # Halts execution.
  # todo: prompt if you're sure or not
  if command == QUIT:
    exit()

def parse_environment_command( action, args ):
  global current_tile
  
  # COMMAND: LOOK
  # Gives the player a more in depth description of the tile.
  # This is done by providing an item list. Don't forget to 
  # look around at your surroundings!
  if action == LOOK:
    print( current_tile.getDescription() )
  
  # COMMAND: GO
  # Basically a prefix for a direction command.
  if action == GO:
    try:
      direction = args[0]
      parse_direction_command( direction )
    except IndexError:
      print( "Usage: go <direction>" )

def parse_direction_command( direction ):
  global current_tile
  
  # COMMAND: NORTH / SOUTH / EAST / WEST
  # Traverse the tiles in the targeted direction.
  # todo: on-travel updates (ie. item spawn, actors move, etc.)
  # todo: notify tile that the player is in it
  if direction in direction_commands:
    current_tile,successful = current_tile.getLinkedTile( direction )
    if successful:
      print( current_tile.desc )
    else:
      print( "There is no way to go that direction" )
  else:
    print( "I don't know where that is." )





# Main execution thread.
# todo: include tile update timing / actor movement / etc.
print( current_tile.desc )
while True:
  # Get a command and arguments from the user.
  action,args = nextCommand()
  
  # Manage invalid commands.
  if action == UNKNOWN:
    print( UNKNOWN )
    continue
  
  # Manage system commands (eg. quit, help)
  if action in system_commands:
    parse_system_command( action, args )
    continue

  # Manage directions commands (eg. north, south)
  if action in direction_commands:
    parse_direction_command( action )
    continue
  
  # Manage environment interaction commands (eg. look around)
  if action in environmental_commands:
    parse_environment_command( action, args )
    continue


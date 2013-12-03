# Dungeon Crawler
# Ver 0.0.4
# 2013.05.01
# Authors: Michel Rouly
#          Adam Wood

import readline

# LIST OF ALL KNOWN COMMANDS
# todo: include aliases / synonyms for commands
NORTH = "north"
SOUTH = "south"
EAST = "east"
WEST = "west"
UP = "up"
DOWN = "down"
direction_commands = [NORTH, SOUTH, EAST, WEST, UP, DOWN]

LOOK = "look"
GO = "go"
environmental_commands = [LOOK, GO]

HELP = "help"
QUIT = "quit"
system_commands = [HELP, QUIT]

known_commands = []
known_commands.extend( direction_commands )
known_commands.extend( environmental_commands )
known_commands.extend( system_commands )

UNKNOWN = "I don't know how to do that."

# This function will prompt the user and grab raw input.
def nextLine():
  user_in = str( input("> ") ).lower()
  return user_in

# This function will split user input as: command <arg>...
# todo: argument recognition
# todo: argument aliasing
def nextCommand():
  user_input = nextLine()
  
  split = user_input.split()
  command = split[0]
  args = []
  if( len(split) > 1 ):
    args = split[1:]
  
  if command in known_commands:
    return command, args
  else:
    return UNKNOWN, None

# Dungeon Crawler
# Ver 0.0.4
# 2013.05.01
# Authors: Michel Rouly
#          Adam Wood

# todo: include any utility functions here

import configparser
from tile import Tile
from item import Item
from inputhandler import *


# This procedure will run over an init file and generate a map,
# returning a reference to whichever tile is the start tile.
def init_map( file_ptr ):
  
  current_tile = None
  
  # read from the configuration file
  config = configparser.ConfigParser()
  config.read( file_ptr )
  if len( config.sections() ) == 0:
    raise IOException( "File not found." )
  
  tile_record = dict()
  
  sections = config.sections()
  for section in sections:
    
    tile = Tile()
    
    try:
      description = config.get( section, "description" )
      tile.setDescription( description )
    except (KeyError, configparser.NoOptionError):
      pass
    
    try:
      itemlist = config.get( section, "items" )
      itemlist = itemlist.split(" & ")
      for item in itemlist:
        atoms = item.split(" ")
        item_name = atoms[-1].strip()
        item_modifier = ' '.join( atoms[:-1] ).strip()
        
        item_obj = Item(item_name, item_modifier)
        tile.addItem( item_obj )
    except (KeyError, configparser.NoOptionError):
      pass
    
    try:
      actorlist = config.get( section, "actors" )
      actorlist = actorlist.split(", ")
      for actor in actorlist:
        print( "Actors currently unsupported!" )
        pass
    except (KeyError, configparser.NoOptionError):
      pass
    
    try:
      currentflag = config.get( section, "start" )
      if current_tile != None:
        print("Multiple start tiles detected!")
      current_tile = tile
    except (KeyError, configparser.NoOptionError):
      pass
    
    tile_record[ section ] = tile
  
  for section in sections:
    try:
      north_target = config.get( section, "north" )
      if north_target in tile_record.keys():
        north_target = tile_record[ north_target ]
        tile_record[ section ].linkTile( north_target, NORTH )
      else:
        print( "Link target %s not found." % north_target )
    except (KeyError, configparser.NoOptionError):
      pass
    
    try:
      south_target = config.get( section, "south" )
      if south_target in tile_record.keys():
        south_target = tile_record[ south_target ]
        tile_record[ section ].linkTile( south_target, SOUTH )
      else:
        print( "Link target %s not found." % south_target )
    except (KeyError, configparser.NoOptionError):
      pass
    
    try:
      east_target = config.get( section, "east" )
      if east_target in tile_record.keys():
        east_target = tile_record[ east_target ]
        tile_record[ section ].linkTile( east_target, EAST )
      else:
        print( "Link target %s not found." % east_target )
    except (KeyError, configparser.NoOptionError):
      pass
    
    try:
      west_target = config.get( section, "west" )
      if west_target in tile_record.keys():
        west_target = tile_record[ west_target ]
        tile_record[ section ].linkTile( west_target, WEST )
      else:
        print( "Link target %s not found." % west_target )
    except (KeyError, configparser.NoOptionError):
      pass
    
    try:
      up_target = config.get( section, "up" )
      if up_target in tile_record.keys():
        up_target = tile_record[ up_target ]
        tile_record[ section ].linkTile( up_target, UP )
      else:
        print( "Link target %s not found." % up_target )
    except (KeyError, configparser.NoOptionError):
      pass
    
    try:
      down_target = config.get( section, "down" )
      if down_target in tile_record.keys():
        down_target = tile_record[ down_target ]
        tile_record[ section ].linkTile( down_target, DOWN )
      else:
        print( "Link target %s not found." % down_target )
    except (KeyError, configparser.NoOptionError):
      pass
  
  if current_tile == None:
    print("No start tile detected!")
  return current_tile





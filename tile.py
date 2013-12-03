# Dungeon Crawler
# Ver 0.0.4
# 2013.05.01
# Authors: Michel Rouly
#          Adam Wood

from item import Item
from actor import Actor
from inputhandler import *

# This class represents a "Tile" or "Room" of the environment.
# The spatial constraints are unlimited, and can be anything from an
# open field to a confined crawlspace.
class Tile:
  def __init__( 
      self, 
      description="N/A", # a description of this tile
      itemlist=[],       # a list of items contained in this tile
      actorlist=[],      # a list of actors contained in this tile
      north=None,
      east=None,
      south=None,
      west=None,
      up=None,
      down=None ):
    
    self.setDescription( description )
    
    self.clearItemList()
    for item in itemlist:
      self.addItem( item )
    
    self.clearActorList()
    for actor in actorlist:
      self.addActor( actor )
    
    self.north = north
    self.east = east
    self.south = south
    self.west = west
    self.up = up
    self.down = down
  
  # This function sets a new textual description of this tile.
  def setDescription( self, newDescription ):
    assert isinstance( newDescription, str ), "Description not a string!"
    self.desc = newDescription
  
  # This function returns a nicely formatted description, including 
  # a list of any items or actors found.
  def getDescription( self ):
    desc = [self.desc]  # include the basic description
    
    # if there are any items listed, include them.
    if len(self.items) > 0:
      desc.append( "\n\nYou can see that the room contains " )
      for item in self.items:
        itemname = item.getName()
        
        # Generate the appropriate indefinite article (a / an).
        desc.append( "a" )
        if itemname[0] in "aeiou":
          desc.append("n ")
        else:
          desc.append(" ")
        
        desc.append(itemname)
        desc.append( ", " )
      # delete any final comma, and insert a final "and"
      del desc[-1]
      if len(self.items) > 1:
        desc.insert( -3, "and " )
      desc.append(".")
    
    return ''.join( desc )
  
  
  def clearItemList( self ):
    self.items = []
  
  
  def addItem( self, newItem ):
    assert isinstance( newItem, Item ), "New Item not an Item!"
    self.items.append( newItem )
  
  
  def delItem( self, target ):
    assert isinstance( target, Item ), "Target Item not an Item!"
    self.items.remove( target )
  
  
  def clearActorList( self ):
    self.actors = []
  
  
  def addActor( self, newActor ):
    assert isinstance( newActor, Actor ), "New Actor not an Actor!"
    self.actors.append( newActor )
  
  
  def delActor( self, target ):
    assert isinstance( target, Actor ), "Target actor not an Actor!"
    self.actors.remove( target )
  
  
  # This function will mutually link this Tile to another Tile, in 
  # the specified direction.
  # todo: unlinking tiles, singly linked tiles (one-way portals?)
  def linkTile( self, target, direction ):
    assert isinstance(target, Tile), "Link target invalid!"
    assert direction in direction_commands, "Invalid linking direction!"
    if direction == NORTH:
      self.north = target
      target.south = self
    if direction == SOUTH:
      self.south = target
      target.north = self
    if direction == EAST:
      self.east = target
      target.west = self
    if direction == WEST:
      self.west = target
      target.east = self
    if direction == UP:
      self.up = target
      target.down = self
    if direction == DOWN:
      self.down = target
      target.up = self
  
  
  # This function accesses the linked tile in the specified direction.
  def getLinkedTile( self, direction ):
    assert direction in direction_commands, "Invalid linking direction!"
    
    if direction == NORTH:
      if self.north != None:
        return self.north, True
      else:
        return self, False
    
    elif direction == SOUTH:
      if self.south != None:
        return self.south, True
      else:
        return self, False
    
    elif direction == EAST:
      if self.east != None:
        return self.east, True
      else:
        return self, False
    
    elif direction == WEST:
      if self.west != None:
        return self.west, True
      else:
        return self, False
    
    elif direction == UP:
      if self.up != None:
        return self.up, True
      else:
        return self, False
    
    elif direction == DOWN:
      if self.down != None:
        return self.down, True
      else:
        return self, False
  

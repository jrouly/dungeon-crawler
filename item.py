# Dungeon Crawler
# Ver 0.0.4
# 2013.05.01
# Authors: Michel Rouly
#          Adam Wood

# todo: item properties
# todo: manipulating items

class Item:
  def __init__( 
      self, 
      name="Item",
      modifier="" ):
    
    self.name = name
    self.setModifier( modifier )
  
  # This function will print out the name of this item, including any
  # modifiers (eg. angry, rusty, old, charred)
  def getName( self ):
    out = []
    if len(self.mod) > 0:
      out.append( self.mod )
      out.append( " " )
    out.append( self.name )
    return ''.join( out )
  
  def setModifier( self, newModifier ):
    assert isinstance( newModifier, str ), "Modifier not a string!"
    self.mod = newModifier


from entities import *
from settings import *

# Tile Manager
class TileManager():
    def __init__(self,entitymanager):
        self.EntityManager = entitymanager
        self.tiles = []
        self.__id = 1000

    def makeTile(self, tiletype, pos = [0,0], hasTexture = True):
        id = self.registerId()
        size = TILE_SIZE,TILE_SIZE
        texture = self.EntityManager.getTexture(tiletype)
        t = Tiles(id,pos,size,texture,tiletype)
        self.EntityManager.entities[id] = t
        self.EntityManager.groups['tile'][id] = t
        return t

    def registerId(self):
        id = "Tile" + str(self.__id)
        self.__id+=1
        return id
    
# Tiles
class Tiles(Entity):
    def __init__(self,id,pos,size,texture,texturename):
        Entity.__init__(self,id,pos,size,'tile',texture,texturename)

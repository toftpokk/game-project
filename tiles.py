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
        t = self.EntityManager.makeEntity(id,pos=pos,size=size,group='tile',hasTexture=hasTexture,texturename=tiletype)
        self.tiles.append(t)
        return t

    def registerId(self):
        id = "Tile" + str(self.__id)
        self.__id+=1
        return id
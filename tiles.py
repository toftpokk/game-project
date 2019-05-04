from entities import *
from settings import *
from alldict import *

# Tile Manager
class TileManager():
    def __init__(self,entitymanager):
        self.EntityManager = entitymanager
        self.tiles = [] # index -> Entity
        self.colliders = [] #index -> Entity
        self.tile_array = [] # index -> Name
        self.collidibles = {}  # Name -> Bool
        self.__id = 1000
    
    def loadTiles(self):
        for i in TILES:
            self.tile_array.append(i)
            self.collidibles[i] = False
        for i in COLLIDE:
            self.collidibles[i] = True

    def makeTile(self, tiletype, pos = [0,0], hasTexture = True):
        id = self.registerId()
        size = TILE_SIZE,TILE_SIZE
        t = self.EntityManager.makeTile(id,isCollidable=self.collidibles[tiletype],pos=pos,size=size,group='tile',hasTexture=hasTexture,texturename=tiletype)
        self.tiles.append(t)
        if self.collidibles[tiletype]:
            self.colliders.append(t)
        return t

    def registerId(self):
        id = "Tile" + str(self.__id)
        self.__id+=1
        return id

    def setMap(self,map,map_w,map_h):
        for i in range(0,map_h):
            for j in range(0,map_w):
                ID = map[j+(map_w*i)]
                tiletype = self.tile_array[ID]
                self.makeTile(tiletype,pos=[j*TILE_SIZE,i*TILE_SIZE])
        
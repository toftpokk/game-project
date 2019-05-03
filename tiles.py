from entities import *
from settings import *
from alldict import *

# Tile Manager
class TileManager():
    def __init__(self,entitymanager):
        self.EntityManager = entitymanager
        self.tiles = [] # index -> Entity
        self.tile_array = [] # index -> Name
        self.collide_array = [] # index -> Bool
        self.__id = 1000
    
    def loadTiles(self):
        for i in TILES:
            self.tile_array.append(i)
            self.collide_array.append(False)
        for i in COLLIDE:
            self.collide_array[i] = True

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

    def setMap(self,map,map_w,map_h):
        for i in range(0,map_h):
            for j in range(0,map_w):
                ID = map[j+(map_w*i)]
                tiletype = self.tile_array[ID]
                self.makeTile(tiletype,pos=[i*TILE_SIZE,j*TILE_SIZE])
        
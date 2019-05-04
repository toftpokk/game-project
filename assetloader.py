import pygame
from alldict import *
# import map here

#Asset Manager
class AssetManager():
    def __init__(self):
        self.texture_dict = {}
        # Array of Dictionaries
        self.dict_array = [PLAYERS,TILES]
        self.map_h = None
        self.map_w = None
        self.map = []
    
    def initAllDict(self):
        # init map
        for csv in MAP_METAS:
            MAPS[csv] = []
            stream = open(MAP_METAS[csv][0])
            string = ""
            w = 0
            h = 0
            for line in stream:
                w = len(line)/2
                for char in line:
                    if char != ',' and char != '\n':
                        MAPS[csv].append(int(char))
                h+=1
            MAP_METAS[csv].append(int(w))
            MAP_METAS[csv].append(int(h))        

    def loadTexture(self,name,path):
        self.texture_dict[name] = pygame.image.load(path)

    def loadDict(self,dic):
        for d in dic:
            self.texture_dict[d] = pygame.image.load(dic[d])

    def loadAll(self):
        for d in self.dict_array:
            self.loadDict(d)

    def loadMap(self,name):
        self.map = MAPS[name]
        self.map_w = MAP_METAS[name][1]
        self.map_h = MAP_METAS[name][2]
        return self.map
        

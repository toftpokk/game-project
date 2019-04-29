import pygame

playerTextures = {
    'player' : 'assets/player.png'
}
tiles = {
    'grass' : 'assets/grass.png'
}

#Asset Manager
class AssetManager():
    def __init__(self):
        self.texture_dict = {}
        # Array of Dictionaries
        self.dict_array = [playerTextures,tiles]

    def loadTexture(self,name,path):
        self.texture_dict[name] = pygame.image.load(path)

    def loadDict(self,dic):
        for d in dic:
            self.texture_dict[d] = pygame.image.load(dic[d])

    def loadAll(self):
        for d in self.dict_array:
            self.loadDict(d)

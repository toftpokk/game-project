import pygame,sys
from settings import *
from assetloader import AssetManager
from entities import EntityManager
from tiles import TileManager

class Game():
    def __init__(self):
        # Init pygame
        pygame.init()

        # Screen
        self.screen = pygame.display.set_mode(SCREEN_SIZE)

        # Assets
        self.assets = AssetManager()
        self.assets.initAllDict() # initiate all dict
        self.assets.loadAll() # load all textures
        MAP = self.assets.loadMap("test1")
        MAP_W = self.assets.map_w
        MAP_H = self.assets.map_h

        # Entities
        self.entities = EntityManager(self.assets)
        self.player = self.entities.makeCreature("player",group="player",hasTexture=True)
        self.entities.makeCreature("enemy",group="enemy")

        # Tiles
        self.tiles = TileManager(self.entities)
        self.tiles.loadTiles()
        self.tiles.setMap(MAP,MAP_W,MAP_H)
        

        # Start Game
        self.in_game = True

        # Player Values
        self.player_pos = [0,0]
        self.player_speed = 0.5

    def runGame(self):
        while self.in_game:
            for event in pygame.event.get():
                key = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    self.in_game = False
            if key[pygame.K_LEFT] and self.player_pos[0]>0: 
                self.player_pos[0] -= self.player_speed
            if key[pygame.K_RIGHT] and self.player_pos[0]<WIDTH: 
                self.player_pos[0] += self.player_speed
            if key[pygame.K_UP] and self.player_pos[1]>0:
                self.player_pos[1] -= self.player_speed
            if key[pygame.K_DOWN] and self.player_pos[1]<HEIGHT:
                self.player_pos[1] += self.player_speed
            self.player.rect.x = int(self.player_pos[0])
            self.player.rect.y = int(self.player_pos[1])
            self.screen.fill((0,0,0))
            self.entities.blitGroups("tile",self.screen)
            self.entities.blitGroups("player",self.screen)
            pygame.display.flip()
        pygame.quit()
        sys.exit()
    
if __name__ == "__main__":
    game = Game()
    game.runGame()
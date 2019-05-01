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
        self.assets.loadAll()

        # Entities
        self.entities = EntityManager(self.assets)
        self.entities.makeCreature("player")

        # Tiles
        self.tiles = TileManager(self.entities)
        self.tiles.makeTile("grass")
        self.tiles.loadMap("")

        # Start Game
        self.in_game = True

    def runGame(self):
        self.entities.blitGroups("tile",self.screen)
        while self.in_game:
            for event in pygame.event.get():
                key = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    self.in_game = False
                """if key[pygame.K_LEFT] and self.pos[0]>0: 
                    self.pos[0] -= 1"""
            self.screen.fill((0,0,0))
            self.entities.blitGroups("tile",self.screen)
            pygame.display.flip()
        pygame.quit()
        sys.exit()
    
if __name__ == "__main__":
    game = Game()
    game.runGame()
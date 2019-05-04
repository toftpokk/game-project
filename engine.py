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
        MAP = self.assets.loadMap("test2")
        MAP_W = self.assets.map_w
        MAP_H = self.assets.map_h

        # Entities
        self.entities = EntityManager(self.assets)
        self.player = self.entities.makeCreature("player",group="player",hasTexture=True,size=[TILE_SIZE,TILE_SIZE])
        self.entities.makeCreature("enemy",group="enemy")

        # Tiles
        self.tiles = TileManager(self.entities)
        self.tiles.loadTiles()
        self.tiles.setMap(MAP,MAP_W,MAP_H)
        

        # Start Game
        self.in_game = True

        # Player Values
        self.player_pos = [0,0]
        self.player_speed = 0.9

    def runGame(self):
        while self.in_game:
            for event in pygame.event.get():
                key = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    self.in_game = False
            if key[pygame.K_LEFT] and self.player_pos[0]>0 and not self.check('left'): 
                self.player_pos[0] -= self.player_speed
            if key[pygame.K_RIGHT] and self.player_pos[0]<WIDTH-TILE_SIZE and not self.check('right'): 
                self.player_pos[0] += self.player_speed
            if key[pygame.K_UP] and self.player_pos[1]>0 and not self.check('up'):
                self.player_pos[1] -= self.player_speed
            if key[pygame.K_DOWN] and self.player_pos[1]<HEIGHT-TILE_SIZE and not self.check('down'):
                self.player_pos[1] += self.player_speed
            self.player.rect.x = int(self.player_pos[0])
            self.player.rect.y = int(self.player_pos[1])
            #print(self.player.rect)
            #print(self.tiles.colliders)
            #for i in self.tiles.colliders:
            #    print(i.name)
            self.screen.fill((0,0,0))
            self.entities.blitGroups("tile",self.screen)
            self.entities.blitGroups("player",self.screen)
            pygame.display.flip()
        pygame.quit()
        sys.exit()
    
    def check(self,dir):
        future_rect = pygame.Rect(self.player.rect.x,self.player.rect.y,self.player.rect.w,self.player.rect.h)
        if dir == 'left':
            future_rect.x = int(self.player_pos[0] - self.player_speed)
        elif dir == 'right':
            future_rect.x = int(self.player_pos[0] + self.player_speed)
        elif dir == 'up':
            future_rect.y = int(self.player_pos[1] - self.player_speed)
        else:
            future_rect.y = int(self.player_pos[1] + self.player_speed)
        k = False
        for i in self.tiles.colliders:
            if future_rect.colliderect(i.rect):
                k = True
                break
        return k
        
    
if __name__ == "__main__":
    game = Game()
    game.runGame()
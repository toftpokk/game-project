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
        self.MAP = self.assets.loadMap("test2")
        self.MAP_W = self.assets.map_w
        self.MAP_H = self.assets.map_h

        # Player Values
        self.player_pos = [0,0]
        self.player_size = [TILE_SIZE/2,TILE_SIZE/2]
        self.player_speed = 1

        # Entities
        self.entities = EntityManager(self.assets)
        self.player = self.entities.makeCreature("player",group="player",hasTexture=True,size=self.player_size)
        self.entities.makeCreature("enemy",group="enemy")

        # Tiles
        self.tiles = TileManager(self.entities)
        self.tiles.loadTiles()
        self.tiles.setMap(self.MAP,self.MAP_W,self.MAP_H)

        # Camera
        self.camera = [0,0,WIDTH,HEIGHT]
        
        
        # Start Game
        self.in_game = True

    def runGame(self):
        while self.in_game:
            for event in pygame.event.get():
                # quit
                if event.type == pygame.QUIT:
                    self.in_game = False
            self.player_pos[0] = self.check_key('x')
            self.player_pos[1] = self.check_key('y')
            
            self.player.rect.x = int(self.player_pos[0])
            self.player.rect.y = int(self.player_pos[1])

            self.camera[0] = self.check_camera('x')
            self.camera[1] = self.check_camera('y')
            
            for e in self.entities.entities:
                E = self.entities.entities[e]
                E.render_rect.x = E.rect.x - self.camera[0]
                E.render_rect.y = E.rect.y - self.camera[1]
            self.screen.fill((0,0,0))
            self.entities.blitGroups("tile",self.screen)
            self.entities.blitGroups("player",self.screen)
            pygame.display.flip()
        pygame.quit()
        sys.exit()
    def check_key(self,dir):
        key = pygame.key.get_pressed()
        if dir == 'x':
            if key[pygame.K_LEFT] and self.player_pos[0]>self.camera[0] and not self.check_player('left'): 
                return self.player_pos[0] - self.player_speed
            if key[pygame.K_RIGHT] and self.player_pos[0]+self.player_size[0]<self.camera[0]+self.camera[2] and not self.check_player('right'): 
                return self.player_pos[0] + self.player_speed
            return self.player_pos[0]
        else:
            if key[pygame.K_UP] and self.player_pos[1]>self.camera[1] and not self.check_player('up'):
                return self.player_pos[1] - self.player_speed
            if key[pygame.K_DOWN] and self.player_pos[1]+self.player_size[1]<self.camera[1]+self.camera[3] and not self.check_player('down'):
                return self.player_pos[1] + self.player_speed
            return self.player_pos[1]
            
    
    def check_camera(self, dir):
        camera_move = [self.player.rect.x - self.camera[2]/2,self.player.rect.y - self.camera[3]/2]
        if dir == 'x':
            if camera_move[0]<0:
                return 0
            elif camera_move[0]+self.camera[2]>self.MAP_W*TILE_SIZE:
                return (self.MAP_W*TILE_SIZE)-self.camera[2]
            else:
                return camera_move[0]
        else:
            if camera_move[1]<0:
                return 0
            elif camera_move[1]+self.camera[3]>self.MAP_H*TILE_SIZE:
                return (self.MAP_H*TILE_SIZE)-self.camera[3]
            else:
                return camera_move[1]
            
            
    
    def check_player(self,dir):
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
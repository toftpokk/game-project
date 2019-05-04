import pygame

# Entity Manager
class EntityManager():
    def __init__(self, assetman):
        self.entities = {}
        self.AssetManager = assetman
        self.groups = {
            'general':{},
            'player':{},
            'enemy':{},
            'tile': {}
            }

    # Entity Creation
    def getTexture(self,name):
        return self.AssetManager.texture_dict.get(name,self.AssetManager.texture_dict['notexture'])
    
    def manageEntity(self, name, group,e):
        self.entities[name] = e
        self.groups[group][name] = e

    def makeEntity(self, name, pos = [0,0], size = [0,0], group = 'general', hasTexture = False, texturename = None):
        entitytexture = None
        if hasTexture:
            if not texturename:
                texturename = name
            if hasTexture:
                entitytexture = self.getTexture(texturename)
        else:
            texturename = None
        e = Entity(name,pos,size,group,entitytexture,texturename)
        self.manageEntity(name,group,e)
        return e

    def killEntity(self,name=None, entity=None):
        if not name:
            name = entity.name
        group = self.entities[name].group
        self.entities[name].kill()
        del self.groups[group][name]
        self.entities[name]
    
    def blitEntity(self, screen, name=None, entity=None):
        # input only entity
        if not name:
            name = entity.name
            texturename = entity.texturename
        # input only name
        if not texturename:
            texturename = name
        if not self.entities[name].texture == None:
            screen.blit(self.entities[name].texture, self.entities[name].rect)
    
    def blitGroups(self, group, screen):
        for e in self.groups[group].values():
            self.blitEntity(screen, entity=e)

    # TODO make creature
    def makeCreature(self, name, pos = [0,0], size = [0,0], group='general', hasTexture = False, texturename = None):
        e = self.makeEntity(name,pos=pos,size=size,group=group,hasTexture=hasTexture,texturename=texturename)
        return e
    
    def makeTile(self, name, isCollidable = False, pos = [0,0], size = [0,0], group = 'tile', hasTexture = False, texturename = None):
        entitytexture = None
        if hasTexture:
            if not texturename:
                texturename = name
            if hasTexture:
                entitytexture = self.getTexture(texturename)
        else:
            texturename = None
        e = TileEntity(name,isCollidable, pos,size,group,entitytexture,texturename)
        self.manageEntity(name,group,e)
        return e

    
# Entity
class Entity():
    def __init__(self,name, pos, size, group, texture, texturename):
        # pos in pixels
        self.name = name
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.texturename = texturename
        self.texture = texture
        self.group = group
    
    def kill(self):
        #TODO Kill self
        return

class TileEntity(Entity):
    def __init__(self, name, isCollidable, pos, size, group, texture, texturename):
        self.isCollidable = isCollidable
        Entity.__init__(self,name, pos, size, group, texture, texturename)

    
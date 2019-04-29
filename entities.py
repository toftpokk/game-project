import pygame

# Entity Manager
class EntityManager():
    def __init__(self, assetman):
        self.entities = {}
        self.AssetManager = assetman
        self.groups = {
            'general':{},
            'tile': {}
            }

    # Entity Creation
    def getTexture(self,name):
        return self.AssetManager.texture_dict[name]
    
    def manageEntity(self, name, group,e):
        self.entities[name] = e
        self.groups[group][name] = e

    def makeEntity(self, name, pos = [0,0], size = [0,0], group = 'general', hasTexture = False, texturename = None):
        entitytexture = None
        if not texturename:
            texturename = name
        if hasTexture:
            entitytexture = self.getTexture(texturename)
        e = Entity(name,pos,size,group,entitytexture,texturename)
        self.entities[name] = e
        self.groups[group][name] = e
        return e

    def killEntity(self,name=None, entity=None):
        if not name:
            name = entity.name
        group = self.entities[name].group
        self.entities[name].kill()
        del self.groups[group][name]
        self.entities[name]
    
    def blitEntity(self, screen, name=None, entity=None):
        if not name:
            name = entity.name
            texturename = entity.texturename
        if not texturename:
            texturename = name
        screen.blit(self.entities[name].texture, self.entities[name].rect)
    
    def blitGroups(self, group, screen):
        for e in self.groups[group].values():
            self.blitEntity(screen, entity=e)

    def moveToDest(self, dest, name=None, entity=None):
        if not name:
            name = entity.name
        while (self.entities[name].rect.x,self.entities[name].rect.y) != dest :
            if self.entities[name].rect.x < dest[0]:
                self.entities[name].rect.x +=1
            elif self.entities[name].rect.x > dest[0]:
                self.entities[name].rect.x -=1

            if self.entities[name].rect.y < dest[1]:
                self.entities[name].rect.y +=1
            elif self.entities[name].rect.y > dest[1]:
                self.entities[name].rect.y -=1
    
    def switchEntities(self, entityA, entityB):
        coordB = (entityB.rect.x, entityB.rect.y)
        while (entityA.rect.x != coordB[0]) or (entityA.rect.y != coordB[1]):
            if entityA.rect.x < coordB[0]:
                entityA.rect.x +=1
                entityB.rect.x -=1
            elif entityA.rect.x > coordB[0]:
                entityA.rect.x -=1
                entityB.rect.x +=1

            if entityA.rect.y < coordB[1]:
                entityA.rect.y +=1
                entityB.rect.y -=1
            elif entityA.rect.y > coordB[1]:
                entityA.rect.y -=1
                entityB.rect.y +=1
    
# Entity
class Entity:
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
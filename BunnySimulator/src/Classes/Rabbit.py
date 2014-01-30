'''
Created on Jan 30, 2014

@author: alxcoh
'''
from commonPygame import *

class Coords:
    def __init__(self, x, y):
        self.x=x
        self.y=y

class Biome:
    
    def __init__(self, color, tag):
        self.color=color
        self.tag=tag
    

class ImageWithCoords:
    def __init__(self, imagePath, coords):
        self.coord=coords
        self.image=pygame.image.load(imagePath)

class Enemy:
    
    def __init__(self, imagePath, startCoords, tag):
        self.image=ImageWithCoords(imagePath, startCoords)
        self.tag=tag
    
class Food:
    
    def __init__(self, imagePath, startCoords, tag):
        self.image=ImageWithCoords(imagePath, startCoords)
        self.coords=startCoords
        self.tag=tag
    
class Disease:
    
    def __init__(self, tag):
        self.tag==tag

class Trait:
    
    def __init__(self, imagePath, relativePosition, identifier, biomeFitness, enemiesFitness, foodFitness, diseaseFitness, genericFitness):
        self.image=ImageWithCoords(imagePath, relativePosition)
        self.tag=identifier
        #all helpful/harmful stuff is a 2D list. First dimension is an object of that type, second dimension is a rating form -1
        self.biomeFitness=biomeFitness
        self.enemiesFitness=enemiesFitness
        self.foodFitness=foodFitness
        self.diseaseFitness=diseaseFitness
        self.genericFitness=genericFitness
        
        
        


class Rabbit:
    
    def __init__(self, traits, diseases, currentBiome, baseImagePath, headImagePath, headImageRelativeCoords, teethImagePath, teethImageRelativeCoords, tailImagePath, tailImageRelativeCoords, earsImagePath, earsImageRelativeCoords, startCoords):
        self.traits=traits
        self.diseases=diseases
        self.biome=currentBiome
        self.baseImage=ImageWithCoords(baseImagePath, Coords(0, 0))
        self.headImage=ImageWithCoords(headImagePath, headImageRelativeCoords)
        self.teethImage=ImageWithCoords(teethImagePath, teethImageRelativeCoords)
        self.tailImage=ImageWithCoords(tailImagePath, tailImageRelativeCoords)
        self.earsImage=ImageWithCoords(earsImagePath, earsImageRelativeCoords)
        self.coords=startCoords
        self.images=[self.baseImage, self.headImage, self.teethImage, self.tailImage, self.earsImage] #now when we iterate through images and easily add them
        
        
    def checkIfHasTrait(self, theTrait):
        for i in self.traits:
            if i.tag==theTrait.tag:
                return True
            
        return False
    
    def addTrait(self, theTrait):
        if not self.checkIfHasTrait(theTrait):
            self.traits.append(theTrait)
            self.images.append(theTrait.image)
        

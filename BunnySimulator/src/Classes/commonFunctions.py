'''
Created on Dec 22, 2013

@author: alxcoh
'''
from decimal import *
from commonPygame import *
import math
import random
import time
def twoDimensionArray(sizeX, sizeY):
    myList=[[0 for i in range(sizeY)] for j in range(sizeX)]
    return myList

def print2DArray(array): #a readable print of a 2d array, actually in 2 dimensions
    for i in range(len(array)):
        print array[i]
        
def rollDice(num,sides):
    total=0
    for i in range(num):
        total+=random.randrange(sides)+1
    return total 

def chanceOfHappen(a, b):
    if a>b:
        print 'Must be first parameter less then second parameter for chance of something happening'
        return None
    randy=random.randrange(b)
    if randy<a:
        return 1 #event did happen
    else: 
        return 0 #event did not happen
    
def percentChange(a, b): #percentage increase or decrease from a to b
    changy=Decimal(b)/Decimal(a)
    return (changy-1)*100

from random import randint
from npcObjects import *

class Room:
    def __init__(self):
        self.furniture=[]
        self.enemies=[]
        for i in range(0,10):
            number=randint(0,3)
            if number>0:
                self.furniture.append(npcObjects())

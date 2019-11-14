import random
import npcObjects

class Room:
    furniture=[]
    enemies=[]
    def __init__(self):
        for i in range(0,10):
            number=random.randint(0,3)
            if number>0:
                furniture.append(npcObjects())

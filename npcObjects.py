from nameChooser import chooseName
from poiChooser import choosePointsOfInterest
from dialogChooser import chooseDialog 


class npcObjects:

    def __init__(self):
        self.name=chooseName()
        print("name is ..."+self.name)
        self.pointsOfInterest=choosePointsOfInterest(self.name)
        self.dialog=chooseDialog(self.name)
        self.picking=definePickability(name)
        self.otherObjects=chooseInsideObjects(name)



    def definePickability(name):
        return False

    def chooseInsideObjects(name):
        return []



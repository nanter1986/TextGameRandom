from nameChooser import chooseName
from poiChooser import choosePointsOfInterest
from dialogChooser import chooseDialog 
from pickabilityDefiner import definePickability
from insideObjectChooser import chooseInsideObjects


class npcObjects:

    def __init__(self):
        self.name=chooseName()
        print("name is ..."+self.name)
        self.pointsOfInterest=choosePointsOfInterest(self.name)
        self.dialog=chooseDialog(self.name)
        self.picking=definePickability(self.name)
        self.otherObjects=chooseInsideObjects(self.name)





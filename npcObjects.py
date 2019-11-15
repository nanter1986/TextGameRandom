from nameChooser import chooseName
from poiChooser import choosePointsOfInterest


class npcObjects:

    def __init__(self):
        self.name=chooseName()
        print("name is ..."+self.name)
        self.pointsOfInterest=choosePointsOfInterest(self.name)
        self.dialog=chooseDialog(name)
        self.picking=definePickability(name)
        self.otherObjects=chooseInsideObjects(name)


    def chooseDialog(name):
        return []

    def definePickability(name):
        return False

    def chooseInsideObjects(name):
        return []



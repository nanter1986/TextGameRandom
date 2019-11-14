from nameChooser import chooseName


class npcObjects:

    def __init__(self):
        self.name=chooseName()
        self.pointsOfInterest=choosePointsOfInterest(name)
        self.dialog=chooseDialog(name)
        self.picking=definePickability(name)
        self.otherObjects=chooseInsideObjects(name)

    def choosePointsOfInterest(name):
        return []

    def chooseDialog(name):
        return []

    def definePickability(name):
        return False

    def chooseInsideObjects(name):
        return []



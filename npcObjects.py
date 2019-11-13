class npcObjects:
    def chooseName():
        pass

    def choosePointsOfInterest(name):
        pass

    def chooseDialog(name):
        pass

    def definePickability(name):
        pass

    def chooseInsideObjects(name):
        pass

    def __init__(self):
        name=chooseName()
        pointsOfInterest=choosePointsOfInterest(name)
        dialog=chooseDialog(name)
        picking=definePickability(name)
        otherObjects=chooseInsideObjects(name)

class npcObjects:
    def chooseName():
        return "Object" 

    def choosePointsOfInterest(name):
        return []

    def chooseDialog(name):
        return []

    def definePickability(name):
        return False

    def chooseInsideObjects(name):
        return []

    def __init__(self):
        name=chooseName()
        pointsOfInterest=choosePointsOfInterest(name)
        dialog=chooseDialog(name)
        picking=definePickability(name)
        otherObjects=chooseInsideObjects(name)

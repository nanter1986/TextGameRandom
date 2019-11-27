from secrets import randbelow

def getTablePois():
    randonNumber=randbelow(len(options))

def getChairPois():
    pass

def choosePointsOfInterest(name):
    pois=None
    if name=="table":
        pois=getTablePois()
    elif name=="chair":
        pois=getChairPois()
    return pois

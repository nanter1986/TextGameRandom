from secrets import randbelow

def getTablePois():
    options=["drawer","book","gem"]
    randonNumber=randbelow(len(options))

def getChairPois():
    options=["pillow","wood"]
    randonNumber=randbelow(len(options))

def choosePointsOfInterest(name):
    pois=None
    if name=="table":
        pois=getTablePois()
    elif name=="chair":
        pois=getChairPois()
    return pois

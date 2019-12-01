from secrets import randbelow

def probabilisticChooserOfPois(options,probability):
    pass

def getTablePois():
    container=[]
    options=["drawer","book","gem"]
    randomNumber=randbelow(len(options))
    for op in options:
        randomNumber=randbelow(3)
        if randonNumber==0:
            container.append(op)
    return container

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

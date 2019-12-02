from secrets import randbelow

def probabilisticChooserOfPois(options,probability):
    container=[]
    randomNumber=randbelow(len(options))
    for op in options:
        randomNumber=randbelow(probability)
        if randonNumber==0:
            container.append(op)
    return container

def getTablePois():
    options=["drawer","book","gem"]
    probability=3
    probabilisticChooserOfPois(options,probability)
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

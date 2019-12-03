from secrets import randbelow

def probabilisticChooserOfPois(options,probability):
    container=[]
    randomNumber=randbelow(len(options))
    for op in options:
        randomNumber=randbelow(probability)
        if randomNumber==0:
            container.append(op)
            print("probChooser chose "+str(op))
    return container

def getTablePois():
    cont=None
    options=["drawer","book","gem"]
    probability=3
    cont=probabilisticChooserOfPois(options,probability)
    return cont

def getChairPois():
    options=["pillow","wood"]
    cont=None
    probability=3
    cont=probabilisticChooserOfPois(options,probability)
    return cont

def choosePointsOfInterest(name):
    pois=None
    if name=="table":
        pois=getTablePois()
    elif name=="chair":
        pois=getChairPois()
    return pois

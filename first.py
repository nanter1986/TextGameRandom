import roomGenerator

def pInventory():
    print("You have:")
    print("1 key")
    print("1 stone")

def pLocation():
    print("You are here")

print("What do you want to do")

def directionInput():
    direction=input("l for left,r for right")
    return direction

def handleDirectionInput(direction):
    if direction=="l":
        print("You went left")
    elif direction=="r":
        print("You went right")
    else:
        print("uknown command")

pInventory()
pLocation()
directionNow=directionInput()
handleDirectionInput(directionNow)

print("END OF PROGRAM")

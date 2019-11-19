from roomGenerator import *
from inventoryHandler import *
from moneyManager import *
from dbEditor import *

inventory=createInventory()
money=106

def pInventory():
    displayInventory(inventory)

def pLocation():
    room=Room()
    for i in room.furniture:
        print("name:"+i.name)
        print("contains:")
        for point in i.pointsOfInterest:
            print(point)

def pMoney():
    displayMoney(money)


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

mainDb()
pInventory()
pLocation()
pMoney()
directionNow=directionInput()
handleDirectionInput(directionNow)

print("END OF PROGRAM")

from nameChooser import *
from roomGenerator import *
from inventoryHandler import *
from moneyManager import *
from dbEditor import *
from npcObjects import npcObjects

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



def directionInput():
    print("What do you want to explore?")
    selection=chooseName()
    npc=npcObjects(selection)
    print(npc.name)
    print("points of interest:")
    print(npc.pointsOfInterest)

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
#handleDirectionInput(directionNow)
print("will try to update")
replacer=input("replacer?")
update_value_of_name("name",str(replacer))
print("past update")
print("access")

access_db_vaulues_by_name("name")

print("END OF PROGRAM")

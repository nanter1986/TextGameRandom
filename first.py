from nameChooser import *
from roomGenerator import *
from inventoryHandler import *
from moneyManager import *
from dbEditor import *
from secrets import randbelow
from npcObjects import npcObjects

MAX_NUMBER_OF_OBJECTS=5
inventory=createInventory()
money=106

def seeIfUserInputIsWithinListRange(choice,the_list):
    length_of_list=len(the_list)

def handle_choice(npc_list):
    print("What is your choice?")
    choice=input("Choose")
    seeIfUserInputIsWithinListRange(choice,npc_list)
    if choice=="1":
        pass
    else:
        pass

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


def createRandomNumberOfObjects():
    npc=[]
    randomNumber=randbelow(MAX_NUMBER_OF_OBJECTS)
    for i in range(randomNumber):
        npcNew=npcObjects()
        npc.append(npcNew)
        print(str(i+1)+"."+npcNew.name)
        print("points of interest:")
        print(npcNew.pointsOfInterest)
    return npc

def directionInput():
    print("What do you want to explore?")
    npc=createRandomNumberOfObjects()
    npc_chosen=handle_choice(npc)
    

def handleDirectionInput(direction):
    if direction=="l":
        print("You went left")
    elif direction=="r":
        print("You went right")
    else:
        print("uknown command")


#new phone
mainDb()
pInventory()
#pLocation()
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

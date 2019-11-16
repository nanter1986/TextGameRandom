def createInventory():
    inventory=[]
    inventory.append("stone")
    inventory.append("key")
    inventory.append("coin")
    return inventory

def addItemToInventory():
    pass

def removeItemFromInventory():
    pass

def displayInventory(inventory):
    for i in inventory:
        print("You have a "+i)
    print("End of inventory")

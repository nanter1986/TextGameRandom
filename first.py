def pInventory():
    print("You have:")
    print("1 key")
    print("1 stone")

print("You are here")
print("What do you want to do")
direction=input("l for left,r for right")
if direction=="l":
    print("You went left")
elif direction=="r":
    print("You went right")
else:
    print("uknown command")

pInventory()

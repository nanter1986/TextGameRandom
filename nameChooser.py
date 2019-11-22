from secrets import randbelow

def chooseName():
    options=["table","chair"]
    randonNumber=randbelow(len(options))
    selection=options[randonNumber]
    return selection

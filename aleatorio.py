import random

def success():
    rand = random.randrange(0,100) 
    if rand > 30:
        return True
    else:
        return False
    
def more_success():
    rand = random.randrange(0,100) 
    if rand > 20:
        return True
    else:
        return False
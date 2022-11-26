import math

class HumanMannager:
    def __init__(self):
        self.activeHumans = []
        self.deactiveHumans = []
        self.count = 0

    def addHuman(self, x, y):
        # validate if the human is already in the list
        for human in self.activeHumans:
            activeHuman = human.amI(x,y)
            if activeHuman:
                activeHuman.update(x,y)
                return activeHuman.id
        
        # if the human is not in the list, add it
        self.activeHumans.append(Human(self.count,x,y))
        self.count += 1
        return self.count - 1
             
    def removeHuman(self, human):
        self.deactiveHumans.append(human)
        self.activeHumans.remove(human)
    
    def cleanHumans(self):
        for human in self.activeHumans:
            if human.isDead():
                self.removeHuman(human)

class Human:
    def __init__(self, id, x, y ):
        self.id = id
        self.x = x
        self.y = y
        self.cntUsed = 0
        self.cntNoUsed = 0
        self.used = True
    
    def update(self, x, y):
        self.x = x
        self.y = y
        self.used = True
    
    def isUsed(self):
        if self.used:
            self.used = False
            self.cntUsed += 1
            return True
        else:
            self.cntNoUsed += 1
            return False

    def isDead(self):
        if self.isUsed():
            return False
        else:
            if self.cntNoUsed > 5:
                return True
            else:
                return False

    def amI (self, x, y):
        # calculate distance
        distance = math.sqrt((self.x - x)**2 + (self.y - y)**2)
        print("self.x: ", self.x, "self.y: ", self.y, "x: ", x, "y: ", y, "distance: ", distance)
        if distance < 30:
            return self
        else:
            return None
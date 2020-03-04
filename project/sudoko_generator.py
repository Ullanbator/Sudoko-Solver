import random


class cell():

    def __init__(self, position):
        self.possibleAnswers = [1,2,3,4,5,6,7,8,9]
        self.answer = None
        self.position = position
        self.solved = False

    def removeAnswer(self, guess):
        if self.solved is False:
            self.possibleAnswers.remove(guess)

    def getPosition(self):
        return self.position

def emptySudoko():
    sudoko = []

    for x in range(1,10):
        if x in [1,2,3]:
            boxNum = 1
        if x in [4,5,6]:
            boxNum = 4
        if x in [7,8,9]:
            boxNum = 7
    
        for y in range (1,10):
            if y in [1,2,3]:
                boxNum = boxNum
            if y in [4,5,6]:
                boxNum += 1
            if y in [7,8,9]:
                boxNum +=2

        c = cell((x,y,boxNum))
        sudoko.append(c)

    return sudoko

def generateSudoko():
    suduko = emptySudoko()

    cells = list(range(81))

    for c in suduko:
        position = c.getPosition()

        x = position[1]
        y = position[2]
        boxNum = position[3]

        for x in suduko:
            position = x.getPosition()

            if x == position[1]:
                x.removeAnswer
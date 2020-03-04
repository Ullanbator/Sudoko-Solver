import random

"""
Initiate the cell object
"""
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

    def getAnswer(self):
        return self.answer

    def checkSolved(self):
        if len(self.possibleAnswers) == 1:
            self.solved = True
        
        return self.solved

def emptySudoko():
    sudoko = []

    for x in range(1,10):
        if x in [1,2,3]:
            z = 1
            boxNum = 1
        if x in [4,5,6]:
            z = 4
            boxNum = 4
        if x in [7,8,9]:
            z = 7
            boxNum = 7
    
        for y in range (1,10):
            boxNum = z
            if y in [1,2,3]:
                boxNum += 0
            if y in [4,5,6]:
                boxNum += 1
            if y in [7,8,9]:
                boxNum +=2

            c = cell((x,y,boxNum))
            sudoko.append(c)

    return sudoko

"""
Function for print the sudoko in a readable way
@sudoko the sudoko object to print
"""
def printSudoko(sudoko):
    
    sudoko = sudoko

    for c in sudoko:
        print(c.getAnswer())

"""
Generating a sudoko puzzle
"""

def generateSudoko():
    suduko = emptySudoko()

    cells = list(range(81))

    for c in suduko:
        position = c.getPosition()

        x = position[0]
        y = position[1]
        boxNum = position[2]

        for x in suduko:
            position = x.getPosition()

            if x == position[0] and x.checkSolved() == True:
                c.removeAnswer(x.getAnswer())
            if y == position[1] and x.checkSolved() == True:
                c.removeAnswer(x.getAnswer())
            if boxNum == position[2] and x.checkSolved() == True:
                c.removeAnswer(x.getAnswer())

printSudoko(emptySudoko())
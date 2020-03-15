import random
import numpy as np

"""
Initiate the cell object
"""
class cell():

    def __init__(self, position):
        self.possibleAnswers = [1,2,3,4,5,6,7,8,9]
        self.answer = "X"
        self.position = position
        self.solved = False

    def removeAnswer(self, guess):
        if self.solved is False:
            self.possibleAnswers.remove(guess)

    def getPosition(self):
        return self.position

    def getAnswer(self):
        return self.answer
    
    def getPossibleAnswers(self):
        return self.possibleAnswers

    def setAnswer(self, answer):
        self.answer = answer
        return True

    def setSolved(self, solved):
        self.solved = solved
        return True

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

    printList = []

    for c in sudoko:
        printList.append(c.getAnswer())

    splitList = np.array_split(printList, 9)

    #Initialising a counter to know when to put in the horizontal bar
    j = 1

    for l in splitList:
        for i in range(3):
            print(str(l[3*i]) + " " + str(l[3*i+1]) + " " + str(l[3*i+2]), end = '')
            if i < 2:
                print(" | ", end = '')
            else:
                print()

        if j == 3 or j == 6:
            print(21*"-")

        j += 1

        


"""
Generating a sudoko puzzle
"""

def generateSudoko():
    suduko = emptySudoko()

    for c in suduko:
        position = c.getPosition()

        x = position[0]
        y = position[1]
        boxNum = position[2]

        c.setAnswer(random.choice(c.getPossibleAnswers()))

        for cx in suduko:
            position = cx.getPosition()

            if x == position[0] and cx.checkSolved() == True:
                c.removeAnswer(cx.getAnswer())
                c.setAnswer(random.choice(c.getPossibleAnswers()))
            if y == position[1] and cx.checkSolved() == True:
                c.removeAnswer(cx.getAnswer())
                c.setAnswer(random.choice(c.getPossibleAnswers()))
            if boxNum == position[2] and cx.checkSolved() == True:
                c.removeAnswer(cx.getAnswer())
                c.setAnswer(random.choice(c.getPossibleAnswers()))

        c.setSolved(True)

        printSudoko(suduko)
    

#printSudoko(emptySudoko())
generateSudoko()
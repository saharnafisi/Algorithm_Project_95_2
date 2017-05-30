import copy
#Global Variables:
solvedPuzzle=[
    ['1','2','3','4'],
    ['5','6','7','8'],
    ['9','10','11','12'],
    ['13','14','15','*'],
]

def readFromFile(file_name):
    array=[]
    textFile=open(file_name)
    string=textFile.read()
    lines=string.split("\n")
    for line in lines:
        array.append(line.split("\t"))
    return array

def findStar(puzzle,starLocation):
    for row in range(0,4):
        for column in range(0,4):
            if puzzle[row][column]=='*':
                starLocation["row"]=row
                starLocation["col"]=column

def printPuzzle(puzzle):
    if puzzle==None:
        return print("None")
    for line in puzzle:
        print("%s\t%s\t%s\t%s"%(line[0],line[1],line[2],line[3]))
        print("\n")
    print("---------------------------")

def moveUp(puzzle, starLocation):
    if(starLocation["row"]>0):
        retPuzzle=copy.deepcopy(puzzle)
        temp=puzzle[starLocation["row"]-1][starLocation["col"]]
        starLocation["row"]=starLocation["row"]-1
        retPuzzle[starLocation["row"]][starLocation["col"]]='*'
        retPuzzle[starLocation["row"]+1][starLocation["col"]]=temp
        return retPuzzle
    else:
        return None

def moveDown(puzzle, starLocation):
    if(starLocation["row"]<3):
        retPuzzle=copy.deepcopy(puzzle)
        temp=puzzle[starLocation["row"]+1][starLocation["col"]]
        starLocation["row"]=starLocation["row"]+1
        retPuzzle[starLocation["row"]][starLocation["col"]]='*'
        retPuzzle[starLocation["row"]-1][starLocation["col"]]=temp
        return retPuzzle
    else:
        return None

def moveRight(puzzle, starLocation):
    if(starLocation["col"]<3):
        retPuzzle=copy.deepcopy(puzzle)
        temp=puzzle[starLocation["row"]][starLocation["col"]+1]
        starLocation["col"]=starLocation["col"]+1
        retPuzzle[starLocation["row"]][starLocation["col"]]='*'
        retPuzzle[starLocation["row"]][starLocation["col"]-1]=temp
        return retPuzzle
    else:
        return None

def moveLeft(puzzle, starLocation):
    if(starLocation["col"]>0):
        retPuzzle=copy.deepcopy(puzzle)
        temp=puzzle[starLocation["row"]][starLocation["col"]-1]
        starLocation["col"]=starLocation["col"]-1
        retPuzzle[starLocation["row"]][starLocation["col"]]='*'
        retPuzzle[starLocation["row"]][starLocation["col"]+1]=temp
        return retPuzzle
    else:
        return None

def IsSolved(puzzle):
    if(puzzle==solvedPuzzle):
        return True
    else:
        return False

class Node:
    def __init__(self,nodeDepth,nodeData,nodeParent):
        self.depth=nodeDepth
        self.data=nodeData
        self.parent=nodeParent

    def expandNode(self):
        expandedNodes=[]
        
        expandedNodes[0]=Node(self.depth+1,self.data.moveRight(),self)
        expandedNodes[1]=Node(self.depth+1,self.data.moveLeft(),self)
        expandedNodes[2]=Node(self.depth+1,self.data.moveUp(),self)
        expandedNodes[3]=Node(self.depth+1,self.data.moveDown(),self)
        return expandedNodes

if __name__ == '__main__':
    starLocation={"row":0,"col":0}
    currentPuzzle=readFromFile("test.txt")
    findStar(currentPuzzle,starLocation)
    printPuzzle(currentPuzzle)
    while True:
        if(IsSolved(currentPuzzle)):
            print("HoooOOOOOraaAA")
            break
        a=input()
        if(a=="u"):
            b=moveUp(currentPuzzle,starLocation)
            if b!=None:
                currentPuzzle=b
            printPuzzle(b)
        elif(a=="d"):
            b=moveDown(currentPuzzle,starLocation)
            if b!=None:
                currentPuzzle=b
            printPuzzle(b)
        elif(a=="l"):
            b=moveLeft(currentPuzzle,starLocation)
            if b!=None:
                currentPuzzle=b
            printPuzzle(b)
        elif(a=="r"):
            b=moveRight(currentPuzzle,starLocation)
            if b!=None:
                currentPuzzle=b
            printPuzzle(b)
        
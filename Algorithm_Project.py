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

class Puzzle:

    def findStar(self):
        for row in range(0,4):
            for column in range(0,4):
                if self.matrix[row][column]=='*':
                    self.currentSpaceRow=row
                    self.currentSpaceCol=column

    def __init__(self,file_name):
        self.matrix=readFromFile(file_name)
        self.findStar()

    def printPuzzle(self):
        for line in self.matrix:
            print("%s\t%s\t%s\t%s"%(line[0],line[1],line[2],line[3]))
            print("\n")
        print("---------------------------")

    def moveUp(self):
        if(self.currentSpaceRow>0):
            temp=self.matrix[self.currentSpaceRow-1][self.currentSpaceCol]
            self.currentSpaceRow=self.currentSpaceRow-1
            self.matrix[self.currentSpaceRow][self.currentSpaceCol]='*'
            self.matrix[self.currentSpaceRow+1][self.currentSpaceCol]=temp
            return True
        else:
            return False

    def moveDown(self):
        if(self.currentSpaceRow<3):
            temp=self.matrix[self.currentSpaceRow+1][self.currentSpaceCol]
            self.currentSpaceRow=self.currentSpaceRow+1
            self.matrix[self.currentSpaceRow][self.currentSpaceCol]='*'
            self.matrix[self.currentSpaceRow-1][self.currentSpaceCol]=temp
            return True
        else:
            return  False

    def moveRight(self):
        if(self.currentSpaceCol<3):
            temp=self.matrix[self.currentSpaceRow][self.currentSpaceCol+1]
            self.currentSpaceCol=self.currentSpaceCol+1
            self.matrix[self.currentSpaceRow][self.currentSpaceCol]='*'
            self.matrix[self.currentSpaceRow][self.currentSpaceCol-1]=temp
            return True
        else:
            return False

    def moveLeft(self):
        if(self.currentSpaceCol>0):
            temp=self.matrix[self.currentSpaceRow][self.currentSpaceCol-1]
            self.currentSpaceCol=self.currentSpaceCol-1
            self.matrix[self.currentSpaceRow][self.currentSpaceCol]='*'
            self.matrix[self.currentSpaceRow][self.currentSpaceCol+1]=temp
            return True
        else:
            return False

    def IsSolved(self):
        if(self.matrix==solvedPuzzle):
            return True
        else:
            return False

if __name__ == '__main__':
    puz=Puzzle("test.txt")
    puz.printPuzzle()
    while True:
        a=input()
        if a=='u':
            puz.moveUp()
        elif a=='d':
            puz.moveDown()
        elif a=='r':
            puz.moveRight()
        elif a=='l':
            puz.moveLeft()
        else:
            print("invalid input!")
        puz.printPuzzle()
        if puz.IsSolved():
            print("HoooOOOOOOooooraa")
            break
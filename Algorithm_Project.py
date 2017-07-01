import copy
# Global Variables:
solvedPuzzle = [
    ['1', '2', '3', '4'],
    ['5', '6', '7', '8'],
    ['9', '10', '11', '12'],
    ['13', '14', '15', '*'],
]


def readFromFile(file_name):
    array = []
    textFile = open(file_name)
    string = textFile.read()
    lines = string.split("\n")
    for line in lines:
        array.append(line.split("\t"))
    return array


def findStar(puzzle, starLocation):
    for row in range(0, 4):
        for column in range(0, 4):
            if puzzle[row][column] == '*':
                starLocation["row"] = row
                starLocation["col"] = column


def findLocation(puzzle, number, location):
    for row in range(0, 4):
        for column in range(0, 4):
            if puzzle[row][column] == number:
                location["row"] = row
                location["col"] = column


def printPuzzle(puzzle):
    if puzzle == None:
        return print("None")
    for line in puzzle:
        print("%s\t%s\t%s\t%s" % (line[0], line[1], line[2], line[3]))
        print("\n")
    print("---------------------------")


def moveUp(puzzle):
    starLocation = {"row": 0, "col": 0}
    findStar(puzzle, starLocation)
    if(starLocation["row"] > 0):
        retPuzzle = copy.deepcopy(puzzle)
        temp = puzzle[starLocation["row"] - 1][starLocation["col"]]
        starLocation["row"] = starLocation["row"] - 1
        retPuzzle[starLocation["row"]][starLocation["col"]] = '*'
        retPuzzle[starLocation["row"] + 1][starLocation["col"]] = temp
        return retPuzzle
    else:
        return None


def moveDown(puzzle):
    starLocation = {"row": 0, "col": 0}
    findStar(puzzle, starLocation)
    if(starLocation["row"] < 3):
        retPuzzle = copy.deepcopy(puzzle)
        temp = puzzle[starLocation["row"] + 1][starLocation["col"]]
        starLocation["row"] = starLocation["row"] + 1
        retPuzzle[starLocation["row"]][starLocation["col"]] = '*'
        retPuzzle[starLocation["row"] - 1][starLocation["col"]] = temp
        return retPuzzle
    else:
        return None


def moveRight(puzzle):
    starLocation = {"row": 0, "col": 0}
    findStar(puzzle, starLocation)
    if(starLocation["col"] < 3):
        retPuzzle = copy.deepcopy(puzzle)
        temp = puzzle[starLocation["row"]][starLocation["col"] + 1]
        starLocation["col"] = starLocation["col"] + 1
        retPuzzle[starLocation["row"]][starLocation["col"]] = '*'
        retPuzzle[starLocation["row"]][starLocation["col"] - 1] = temp
        return retPuzzle
    else:
        return None


def moveLeft(puzzle):
    starLocation = {"row": 0, "col": 0}
    findStar(puzzle, starLocation)
    if(starLocation["col"] > 0):
        retPuzzle = copy.deepcopy(puzzle)
        temp = puzzle[starLocation["row"]][starLocation["col"] - 1]
        starLocation["col"] = starLocation["col"] - 1
        retPuzzle[starLocation["row"]][starLocation["col"]] = '*'
        retPuzzle[starLocation["row"]][starLocation["col"] + 1] = temp
        return retPuzzle
    else:
        return None


def IsSolved(puzzle):
    if(puzzle == solvedPuzzle):
        return True
    else:
        return False


class Node:
    def __init__(self, nodeDepth, nodeData, nodeParent):
        self.depth = nodeDepth
        self.data = nodeData
        self.parent = nodeParent

    def printPuzzle(self):
        if self.data == None:
            return print("None")
        for line in self.data:
            print("%s\t%s\t%s\t%s" % (line[0], line[1], line[2], line[3]))
            print("\n")
        print("---------------------------")

    def manhattanDistance(self):
        location = {"row": 0, "col": 0}
        correctLocation = {"row": 0, "col": 0}
        totalManhattanDistance = 0
        for i in range(0, 4):
            for j in range(0, 4):
                findLocation(self.data, self.data[i][j], location)
                findLocation(solvedPuzzle, self.data[i][j], correctLocation)
                totalManhattanDistance += abs(location["row"] - correctLocation["row"]) + abs(
                    location["col"] - correctLocation["col"])
                print("%d %d %d" % (i, j, totalManhattanDistance))
        return totalManhattanDistance

    def gt(self, other):
        return (self.manhattanDistance>other.manhattanDistance)

    def ge(self, other):
        return(self.manhattanDistance >= other.manhattanDistance)

    def lt(self, other):
        return(self.manhattanDistance < other.manhattanDistance)

    def le(self, other):
        return(self.manhattanDistance <= other.manhattanDistance)


def expandNode(node):
    expandedNodes = []
    retList = []
    expandedNodes.append(Node(node.depth + 1, moveRight(node.data), node))
    expandedNodes.append(Node(node.depth + 1, moveLeft(node.data), node))
    expandedNodes.append(Node(node.depth + 1, moveUp(node.data), node))
    expandedNodes.append(Node(node.depth + 1, moveDown(node.data), node))
    for node in expandedNodes:
        if node.data != None:
            retList.append(node)
    return retList


def branchAndBound(puzzle):
    nodesQueue = []

    # create a root node
    nodesQueue.append(Node(0, puzzle, None))

    while True:
        # no solution
        if len(nodesQueue) == 0:
            return None

        # take the node from front of queue
        node = nodesQueue.pop(0)

        # if node is goal,return moves
        if node.data == solvedPuzzle:
            moves = []
            while node.parent != None:
                moves.append(node)
                node = node.parent
            return moves

        # if node is not goal,expand node
        else:
            nodesQueue.extend(expandNode(node))


if __name__ == '__main__':
    currentPuzzle = readFromFile("test.txt")
    # manhattanDistance(currentPuzzle)
    # printPuzzle(currentPuzzle)
    node=Node(0,currentPuzzle,0)
    node.printPuzzle();
    node2=Node(0,solvedPuzzle,0)
    printPuzzle(node>node2)

    """while True:
        choice = int(input("enter 1 for greedy and 2 for branch and bound: "))
        if (choice == 1):
            print("manhattan distances: ")
            node = Node(0, currentPuzzle, 0)
            # manhattanDistance(currentPuzzle)
            node.manhattanDistance()
            break

        elif choice == 2:
            moves = branchAndBound(currentPuzzle)
            for state in reversed(moves):
                printPuzzle(state.data)
            break
        else:
            print("invalid choice...try again ")"""

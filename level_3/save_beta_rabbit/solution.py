def answer (food, grid):
    """
    And this version gives me a memory error instead of a time error. How the
    hell do I pare this down?
    Notes:
        Rabbit can only move left or down, and grid is top-to-bottom,
        left-to-right. First element will always be 0 because rabbit starts in
        top-left room. (Although, we could simplify the input, since top-left
        is always the starting point, by instead making grid[0][0] the food
        value, but that's not really important here.) So, to move, rabbit will
        always move from (x,y) to (x+1,y) or (x,y+1).

        Rabbit starts with food, and every time it moves to (x,y),
        food -= grid[x][y]

        Return smallest possible nonnegative food value AFTER arriving at
        (len(grid),len(grid[0])). If no nonnegative value is possible, return
        -1

        I think it's easiest, actually, to find total food expenditures over
        the path, then compare expenditure to food.

    Brute-force messed up again. Looks like this time I'm gonna be walking a
    linked list, like with zombits.
    """

    class Grid:
        def __init__ (self, grid, maxVal):
            self.grid = grid
            self.maxVal = maxVal
            self.maxY = len (grid) - 1
            self.maxX = len (grid[0]) - 1
            self.finalVal = self.search (self.grid, self.maxVal)

        def search (self, grid, maxVal):
            start = GridNode (grid, 0, 0, maxVal, self.maxY, self.maxX)
            if not GridNode.instances:
                return -1
            else:
                total = 201
                for i in GridNode.finalVals:
                    if i < total:
                        total = i
                return total


    class GridNode:
        instances = []
        finalVals = []
        def __init__ (self, grid, x, y, currVal, maxY, maxX):
            self.grid = grid
            self.x = x
            self.y = y
            self.maxX = maxX
            self.maxY = maxY
            self.currVal = currVal - grid[y][x]
            GridNode.instances.append(self)
            self.checkSelf()

        def __str__ (self):
            return "GridNode (" + str (self.x) + "," + str (self.y) + ")"
        def checkSelf (self):
            if self.currVal < 0:
                del GridNode.instances[-1]
                return
            else:
                if self.x < self.maxX:
                    rightChild = GridNode (self.grid, self.x + 1,
                            self.y, self.currVal, self.maxY, self.maxX)
                    #if GridNode.instances:
                        #if GridNode.instances[-1] == rightChild:
                            #return
                if self.y < self.maxY:
                    downChild = GridNode (self.grid, self.x, self.y + 1,
                            self.currVal, self.maxY, self.maxX)
                    #return
            if (self.x == self.maxX) and (self.y == self.maxY):
                self.finalVals.append (self.currVal)

    path = Grid (grid, food)
    return path.finalVal

    """

#Time limit exceeded my ass. Does that mean I took too much time to come up
# with a solution, or that my solution takes too much server time?
    Brute-force method. This works for the examples and would probably work for
    verify if I could run it, but foobar returns a "time limit exceeded" error.
    Server time is expensive, and this version begins by calculating every
    possible path, so I can see why it doesn't work.
    from itertools import permutations

    basePath = ''
    paths = []

    # Generate a path that goes all right, then all left, just to get a base
    # case.
    for i in range (len (grid)):
        basePath += 'd'
    for i in range (len (grid[0])):
        basePath += 'r'

    # All possible paths in this scenario have the same number of moves (width
    # + length - 2). That means that all paths are just permutations of each
    # other. Let itertools take care of making the permutations...
    for i in permutations(basePath):
        if not i in paths:
            paths.append(i)

    x, y, z = 0, 0, 0
    pathTotals = [0]

    # Get the amount of food expended in each path.
    for i in paths:
        for j in i:
            if j == 'd' and y < len (grid) - 1:
                y += 1
            elif j == 'r' and x < len (grid[0]) - 1:
                x += 1
            pathTotals[z] += grid[y][x]
            # Quick fix to reduce computation time a little. Not enough,
            # apparently.
            if pathTotals[z] > food:
                pathTotals[z], x, y = 0, 0, 0
                break
        z += 1
        pathTotals.append (0)
        x, y = 0, 0

    # Find 1: Whether or not a solution where food expended < food carried
    # exists, then 2: the largest amount of food that can be expended within
    # those paths
    solution = False
    currentMax = 0
    for i in range (0, len(pathTotals)):
        if pathTotals[i] <= food:
            solution = True
            if pathTotals[i] > currentMax:
                currentMax = pathTotals[i]
    # And, finally, return -1 if no solution exists, or food remaining if a
    # solution does exist.
    if not solution:
        return -1
    else:
        return food - currentMax
    """

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
    """

    def maxValue (grid, maxPoss):
        r = len (grid)
        c = len (grid[0])
        maxVals = [[0 for i in range(c)] for j in range (r)]
        for i in range (0, r):
            for j in range (0, c):
                if i == 0 and j == 0:
                    maxVals[i][j] = grid[i][j]
                elif i == 0:
                    maxVals[i][j] = maxVals[i][j-1] + grid[i][j]
                elif j == 0:
                    maxVals[i][j] = maxVals[i-1][j] + grid[i][j]
                else:
                    greater = max(maxVals[i][j-1], maxVals[i-1][j])
                    maxVals[i][j] = greater + grid[i][j]
        ret = -1
        for i in range(r):
            for j in range(c):
                if maxVals[i][j] > 0 and maxVals[i][j] <= maxPoss and maxVals[i][j] > ret:
                    ret = maxVals[i][j]
        return ret

    ret = maxValue(grid, food)
    if ret == -1:
        return -1
    else:
        return food - ret



    """
    def search (grid, currVal, x, y):
        global finalVal
        currVal -= grid[y][x]
        if currVal < 0:
            return
        if (x == maxX) and (y == maxY) and ((finalVal == 0) or (finalVal == 1)):
            return


        if x < maxX:
            search (grid, currVal, x + 1, y)
        if y < maxY:
            search (grid, currVal, x, y + 1)

        if (x == maxX) and (y == maxY):
            if (currVal < finalVal) or (finalVal == -1):
                    finalVal = currVal

    search (grid, food, 0, 0)
    """

import time
start_time = time.time()

row_size = 6
coln_size = row_size + 2


def make_row():
    global row_size, coln_sizeq
    grid = []
    for i in range(row_size):
        temp = []
        for j in range(coln_size):
            if i == 0 or i == row_size-1:
                temp.append(1)
            else:
                temp.append(0)
        grid.append(temp)
    return (grid)


grid = make_row()


def possibleConnect(grid):
    count =0
    for i in range(row_size):
        for j in range(row_size):
            ConnectionWithOrWithoutCount = False
            innerCountList = []
            if j>i:
                if j-i == row_size-1:
                    break
                for k in range(coln_size):
                    initial = False
                    diff = j - i - 1
                    if grid[i][k] == 1 and grid[j][k] == 1:
                        initial = True
                    if not(initial):
                        if k == coln_size-1 and ConnectionWithOrWithoutCount == False:
                            return 30
                        continue
                    if initial:
                        ConnectionWithOrWithoutCount = True
                        if diff == 0:
                            break
                        if diff ==1:
                            if grid[i+1][k] == 0:
                                innerCountList.append(0)
                                break
                            if k == coln_size-1:
                                break
                            else:
                                innerCountList.append(1)
                        if diff > 1:
                            innerBool = True
                            DownRow = i
                            innerCount = 0
                            while DownRow < j-1:
                                DownRow +=1
                                if grid[DownRow][k] == 0 and innerBool:
                                    innerBool = True
                                else:
                                    if grid[DownRow][k] == 1:
                                        innerCount +=1
                                    innerBool = False
                            if innerBool:
                                innerCountList.append(0)
                                break
                            else:
                                innerCountList.append(innerCount)
            if len(innerCountList)>0:
                count += min(innerCountList)
    return count


def generate_numbers(grid, start, stop):
    for i in range(coln_size):
        if i < start:
            grid[i] = 0
        if i >= start:
            if i <stop:
                grid[i] = 1
        if i >= stop:
            grid[i] = 0


def SsList():
    SSlist = []
    for i in range(coln_size):
        start = 0
        stop = i+1
        SSlist.append([start, stop])
        for j in range(coln_size):
            if stop < coln_size:
                start +=1
                stop += 1
                SSlist.append([start,stop])
    return SSlist


SSlist = SsList()
countList = []

def makeRowCombinations(grid, SSlist, row):
    global countList
    for i in SSlist:
        start = i[0]
        stop = i[1]

        generate_numbers(grid[row+1], start, stop)
        temp = possibleConnect(grid)
        if temp < 20:
            countList.append(temp)
        if row < len(grid)-3:
            makeRowCombinations(grid, SSlist, row+1)

makeRowCombinations(grid,SSlist, 0)

print(min(countList))


print(time.time()-start_time)
from queue import Queue

kaart1 = [
    "      **               **      ",
    "     ***     D        ***      ",
    "     ***                       ",
    "                      *****    ",
    "           ****      ********  ",
    "           ***          *******",
    " **                      ******",
    "*****             ****     *** ",
    "*****              **          ",
    "***                            ",
    "              **         ******",
    "**            ***       *******",
    "***                      ***** ",
    "                               ",
    "                s              ",
]

kaart2 = [
    "     **********************    ",
    "   *******   D    **********   ",
    "   *******                     ",
    " ****************    **********",
    "***********          ********  ",
    "            *******************",
    " ********    ******************",
    "********                   ****",
    "*****       ************       ",
    "***               *********    ",
    "*      ******      ************",
    "*****************       *******",
    "***      ****            ***** ",
    "                               ",
    "                s              ",
]

wall = "*"

start_row = 14
start_col = 16

start = (start_row, start_col)
visited = [start]

parents = {start: None}
queue = Queue()


def getMapSize(map):
    return len(map[0]) - 1, len(map) - 1


def workWithDirection(currentPoint, x, y):
    newPoint = (currentPoint[0] + x, currentPoint[1] + y)
    visited.append(newPoint)
    queue.put(newPoint)
    parents[newPoint] = currentPoint


def makeMovement(map, currentPoint):
    height = getMapSize(map)[0]
    wight = getMapSize(map)[1]

    if currentPoint[0] + 1 < wight and \
            (currentPoint[0] + 1, currentPoint[1]) not in visited and \
            map[currentPoint[0] + 1][currentPoint[1]] != wall:
        workWithDirection(currentPoint, 1, 0)

    if currentPoint[0] - 1 > 0 and \
            (currentPoint[0] - 1, currentPoint[1]) not in visited and \
            map[currentPoint[0] - 1][currentPoint[1]] != wall:
        workWithDirection(currentPoint, -1, 0)

    if currentPoint[1] + 1 < height and \
            (currentPoint[0], currentPoint[1] + 1) not in visited and \
            map[currentPoint[0]][currentPoint[1] + 1] != wall:
        workWithDirection(currentPoint, 0, +1)

    if currentPoint[1] - 1 > 0 and \
            (currentPoint[0], currentPoint[1] - 1) not in visited and \
            map[currentPoint[0]][currentPoint[1] - 1] != wall:
        workWithDirection(currentPoint, 0, -1)


def exploreMap(map):
    currentPoint = start

    while map[currentPoint[0]][currentPoint[1]] != "D":
        makeMovement(map, currentPoint)
        currentPoint = queue.get()
    return parents, currentPoint


def getPath(map, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = map.get(current)

    return path


def getSolvedMap(path, map):
    path.pop(0)
    print(path)
    for el in path:
        map[el[0]] = map[el[0]][:el[1]] + "O" + map[el[0]][el[1] + 1:]
    return map


def solve(map):

    exploredMap, goal = exploreMap(map)

    path = getPath(exploredMap, goal)
    getSolvedMap(path, map)
    map = "\n".join(map)
    return map


# run here
print(solve(kaart2))




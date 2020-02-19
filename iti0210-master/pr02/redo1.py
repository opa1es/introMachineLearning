from queue import Queue

mapFileName = "cave300x300"
wall = "*"
start = (13, 16)


def generateMap():
    # return [l.strip() for l in f.readlines() if len(l) > 1]
    return [
        "*******************************",
        "*    ***     D        ***     *",
        "*    ***                      *",
        "*                     *****   *",
        "*          ****      ******** *",
        "*          ***          *******",
        "***                      ******",
        "*****             ****     ****",
        "*****              **         *",
        "***                           *",
        "*             **         ******",
        "**            ***       *******",
        "***                      ******",
        "*               s             *",
        "*******************************",
    ]


def getNeighbors(map, current):
    neighbors = []

    if map[current[0] + 1][current[1]] != wall:
        neighbors.append((current[0] + 1, current[1]))
    if map[current[0] - 1][current[1]] != wall:
        neighbors.append((current[0] - 1, current[1]))
    if map[current[0]][current[1] + 1] != wall:
        neighbors.append((current[0], current[1] + 1))
    if map[current[0]][current[1] - 1] != wall:
        neighbors.append((current[0], current[1] - 1))
    # print(str(current) + "  " + str(neighbors))
    return neighbors


def exploreBFS():
    card = generateMap()

    frontier = Queue()
    frontier.put(start)
    parents = {start: None}
    currentPoint = start
    while card[currentPoint[0]][currentPoint[1]] != "D":
        for newPosition in getNeighbors(card, currentPoint):
            if newPosition not in parents:
                frontier.put(newPosition)
                parents[newPosition] = currentPoint
        currentPoint = frontier.get()
    return parents, currentPoint


def getPath(map, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = map.get(current)
    print(len(path))
    return path


def getSolvedMap(path, map):
    path.pop(0)
    print(path)
    for el in path:
        map[el[0]] = map[el[0]][:el[1]] + "O" + map[el[0]][el[1] + 1:]
    return map


def solveBFS(map):
    exploredMap, goal = exploreBFS()
    path = getPath(exploredMap, goal)
    getSolvedMap(path, map)
    map = "\n".join(map)
    return map


print(solveBFS(generateMap()))

from queue import Queue, PriorityQueue

mapFileName = "cave300x300"
wall = "*"
start = (2, 2)


def setFinish():
    if mapFileName == "cave300x300": return 295, 257
    if mapFileName == "cave600x600": return 598, 595
    if mapFileName == "cave900x900": return 898, 895


finish = setFinish()


def h(currentPosition, end):
    return abs(end[0] - currentPosition[0]) + abs(end[1] - currentPosition[1])


def generateMap():
    with open(mapFileName) as f:
        return [l.strip() for l in f.readlines() if len(l) > 1]


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
    return neighbors


# -----------------------BFS-------------------------------------

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


def solveBFS(map):
    exploredMap, goal = exploreBFS()
    path = getPath(exploredMap, goal)
    getSolvedMap(path, map)
    map = "\n".join(map)
    return map


# -----------------------GREEDY-------------------------------------


def exploreGreedy():
    card = generateMap()

    frontier = PriorityQueue()
    frontier.put((0, start))
    parents = {start: None}
    currentPoint = start
    while card[currentPoint[0]][currentPoint[1]] != "D":
        for newPosition in getNeighbors(card, currentPoint):
            if newPosition not in parents:
                priority = h(currentPoint, finish)
                frontier.put((priority, newPosition))
                parents[newPosition] = currentPoint
        _, currentPoint = frontier.get()
    return parents, currentPoint


def solveGreedy(map):
    exploredMap, goal = exploreGreedy()
    path = getPath(exploredMap, goal)
    getSolvedMap(path, map)
    map = "\n".join(map)
    return map


# -----------------------A* algorithm-------------------------------------


def exploreAStar():
    card = generateMap()
    cost_so_far = {start: 0}
    frontier = PriorityQueue()
    frontier.put((0, start))
    parents = {start: None}
    currentPoint = start
    while card[currentPoint[0]][currentPoint[1]] != "D":
        for newPosition in getNeighbors(card, currentPoint):
            if newPosition not in parents:

                new_cost = cost_so_far[currentPoint] + 1

                if newPosition not in cost_so_far or new_cost < cost_so_far[newPosition]:
                    cost_so_far[newPosition] = new_cost
                    priority = new_cost + h(newPosition, finish)
                    frontier.put((priority, newPosition))
                    parents[newPosition] = currentPoint

        _, currentPoint = frontier.get()
    return parents, currentPoint


def solveAStar(map):
    setFinish()
    exploredMap, goal = exploreAStar()
    path = getPath(exploredMap, goal)
    getSolvedMap(path, map)
    map = "\n".join(map)
    return map


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


# print(solveBFS(generateMap())) #takes too much time
print(solveAStar(generateMap()))
# print(solveGreedy(generateMap()))

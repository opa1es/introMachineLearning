from queue import Queue, PriorityQueue


def generateMap(name):
    with open(name) as f:
        return [l.strip() for l in f.readlines() if len(l) > 1]


def getFinish(name):
    if name == "cave300x300": return 295, 257
    if name == "cave600x600": return 598, 595
    if name == "cave900x900": return 898, 895


wall = "*"
start = (2, 2)

parents = {start: None}


def workWithDirection(currentPoint, queue, visited, x, y):
    newPoint = (currentPoint[0] + x, currentPoint[1] + y)
    visited.append(newPoint)
    queue.put(newPoint)
    parents[newPoint] = currentPoint


def exploreMap(map, queue, visited):
    currentPoint = start
    # ctr = 0
    while map[currentPoint[0]][currentPoint[1]] != "D":

        if (currentPoint[0] + 1, currentPoint[1]) not in visited and \
                map[currentPoint[0] + 1][currentPoint[1]] != wall:
            workWithDirection(currentPoint, queue, visited, 1, 0)

        if (currentPoint[0] - 1, currentPoint[1]) not in visited and \
                map[currentPoint[0] - 1][currentPoint[1]] != wall:
            workWithDirection(currentPoint, queue, visited, -1, 0)

        if (currentPoint[0], currentPoint[1] + 1) not in visited and \
                map[currentPoint[0]][currentPoint[1] + 1] != wall:
            workWithDirection(currentPoint, queue, visited, 0, +1)

        if (currentPoint[0], currentPoint[1] - 1) not in visited and \
                map[currentPoint[0]][currentPoint[1] - 1] != wall:
            workWithDirection(currentPoint, queue, visited, 0, -1)
        # ctr+=1
        # print(ctr)
        currentPoint = queue.get()

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
    visited = [start]
    queue = Queue()
    exploredMap, goal = exploreMap(map, queue, visited)

    path = getPath(exploredMap, goal)
    getSolvedMap(path, map)
    map = "\n".join(map)
    return map


# run here
print(solveBFS(generateMap("cave300x300")))

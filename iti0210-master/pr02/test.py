from queue import Queue, PriorityQueue

mapFileName = "cave600x600"


wall = "*"

start = (2, 2)
parents = {start: None}


def generateMap():
    with open(mapFileName) as f:
        return [l.strip() for l in f.readlines() if len(l) > 1]


def h(currentPosition, end):
    return abs(end[0] - currentPosition[0]) + abs(end[1] - currentPosition[1])



def getFinish(name):
    if name == "cave300x300": return 295, 257
    if name == "cave600x600": return 598, 595
    if name == "cave900x900": return 898, 895




def workWithDirectionGreedy(currentPoint, queue, visited, x, y):
    newPoint = (currentPoint[0] + x, currentPoint[1] + y)
    visited.append(newPoint)
    priority = h(currentPoint, getFinish(mapFileName))
    queue.put((priority, newPoint))
    parents[newPoint] = currentPoint


def exploreMapGreedy(map, queue, visited):
    currentPoint = start

    while map[currentPoint[0]][currentPoint[1]] != "D":
        if (currentPoint[0] + 1, currentPoint[1]) not in visited and \
                map[currentPoint[0] + 1][currentPoint[1]] != wall:
            workWithDirectionGreedy(currentPoint, queue, visited, 1, 0)

        if (currentPoint[0] - 1, currentPoint[1]) not in visited and \
                map[currentPoint[0] - 1][currentPoint[1]] != wall:
            workWithDirectionGreedy(currentPoint, queue, visited, -1, 0)

        if (currentPoint[0], currentPoint[1] + 1) not in visited and \
                map[currentPoint[0]][currentPoint[1] + 1] != wall:
            workWithDirectionGreedy(currentPoint, queue, visited, 0, +1)

        if (currentPoint[0], currentPoint[1] - 1) not in visited and \
                map[currentPoint[0]][currentPoint[1] - 1] != wall:
            workWithDirectionGreedy(currentPoint, queue, visited, 0, -1)

        _, currentPoint = queue.get()
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


def solveGreedy(map):
    queue = PriorityQueue()
    visited = [start]
    exploredMap, goal = exploreMapGreedy(map, queue, visited)

    path = getPath(exploredMap, goal)
    getSolvedMap(path, map)
    map = "\n".join(map)
    return map


# run here
print(solveGreedy(generateMap()))

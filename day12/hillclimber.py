from dataclasses import dataclass

def constructMap(path):
    with open(path) as f:
        lines = f.read().splitlines()
    map = []
    for line in lines:
        row = []
        for c in line:
            if c.isupper():
                row.append(c)
                continue
            height = ord(c)-ord("a")
            row.append(height)
        map.append(row)
    return map

def findPosition(char, map):
    locations = []
    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c] == char:
                locations.append((r, c))
    return locations

def makeAdjList(map):
    adj = {}
    height = len(map)
    width = len(map[0])
    for r in range(len(map)):
        for c in range(len(map[0])):
            pos = (r, c)
            h1 = map[r][c]
            if h1 == "S":
                h1 = 0
            elif h1 == "E":
                h1 = 25
            adj[pos] = []
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            for i in directions:
                new_pos = (pos[0]+i[0], pos[1]+i[1])
                if new_pos[0] < 0 or new_pos[0] >= height or new_pos[1] < 0 or new_pos[1] >= width:
                    continue
                h2 = map[new_pos[0]][new_pos[1]]
                if h2 == "S": 
                    h2 = 0
                if h2 == "E": 
                    h2 = 25
                if abs(h2 - h1) > 1:
                    continue
                adj[pos].append(new_pos)
    return adj

def Djikstras(adjDict, startCoord):
    @dataclass
    class Path:
        path: list
        dist: int

    def smallestUnvisitedPath(distances, unvisitedNodes):
        smallestKey = None
        for key in unvisitedNodes:
            if distances[key].dist == -1:
                continue
            if smallestKey == None:
                smallestKey = key
            if distances[key].dist < distances[smallestKey].dist:
                smallestKey = key
        return smallestKey

    unvisitedNodes = list(adjDict.keys())
    current = startCoord
    unvisitedNodes.remove(current)
    distances = {startCoord: Path([], 0)}
    for key in unvisitedNodes:
        distances[key] = Path([], -1)

    while len(unvisitedNodes) != 0:
        neighbors = adjDict[current]
        currentPath = distances[current]
        for i in neighbors:
            distance = currentPath.dist + 1
            newPath = currentPath.path + [i]
            if distance < distances[i].dist or distances[i].dist == -1:
                distances[i] = Path(newPath, distance)
        current = smallestUnvisitedPath(distances, unvisitedNodes)
        if current == None:
            print(f"{len(unvisitedNodes)} nodes are unreachable")
            break
        unvisitedNodes.remove(current)
    
    return distances

def findAllofHeight(height, dictionary, map):
    new_dict = {}
    for key in dictionary.keys():
        if map[key[0]][key[1]] == height:
            new_dict[key] = dictionary[key]
    return new_dict

def findLowestDist(dict):
    lowest = None
    for key in dict.keys():
        if dict[key].dist == -1:
            continue
        if lowest == None:
            lowest = dict[key]
            continue
        if dict[key].dist < lowest.dist:
            lowest = dict[key]
    return lowest

def main():
    map = constructMap("input.txt")
    start_pos = findPosition("S", map)[0]
    end_pos = findPosition("E", map)[0]
    adjList = makeAdjList(map)
    #distances = Djikstras(adjList, start_pos)
    #print(distances[end_pos].dist)
    distances = Djikstras(adjList, end_pos)
    a_paths = findAllofHeight(0, distances, map)
    validPaths = []
    for i in distances.values():
        if len(i.path) == 0:
            continue
        validPaths.append(i)
    print(len(validPaths))
    print(findLowestDist(a_paths).dist)

if __name__ == "__main__":
    main()
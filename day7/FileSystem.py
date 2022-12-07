import re
from numpy import Inf

def navigateToPath(dictionary, path):
    for i in range(len(path)):
        dictionary = dictionary[path[i]]
    return dictionary

def addDirectory(dictionary, path, newDirectory):
    folder = navigateToPath(dictionary, path)
    folder[newDirectory] = {}

def addFile(dictionary, directory, file):
    size = file[0]
    name = file[1]
    folder = navigateToPath(dictionary, directory)
    folder[name] = int(size)

def constructDictionary():
    x = {"/": {}}
    path = []
    with open("input.txt") as f:
        instructions = f.read().splitlines()
    for i in instructions:
        components = i.split(" ")
        if components[0] == "$":
            if components[1] == "cd":
                if components[2] == "..":
                    path.pop()
                    continue
                if components[2] == "/":
                    path = []
                path.append(components[2])
        elif components[0] == "dir":
            addDirectory(x, path, components[1])
        elif re.search("[0-9]+", components[0]):
            addFile(x, path, [components[0], components[1]])
    return x

def count(totals, dictionary, key):
    total = 0
    for i in dictionary.keys():
        if type(dictionary[i]) == dict:
            result = count(totals, dictionary[i], i)
            total += result
        else:
            total += dictionary[i]
    totals.append([key, total])
    return total

def getPreCounts(dictionary):
    counts = []
    count(counts, dictionary, "/")
    return counts

def sumLessThan100000(dictionary):
    running_total = 0
    preCounts = getPreCounts(dictionary)
    print(preCounts)
    for i in preCounts:
        if i[1] <= 100000:
            running_total += i[1]
    return running_total

def findSmallest(values, minimum):
    smallest = Inf
    for i in values:
        if minimum < i[1] < smallest:
            smallest = i[1]
    return smallest

def findFirstOccurence(dirName, values):
    for i in values:
        if i[0] == dirName:
            return i[1]


def main():
    dictionary = constructDictionary()
    #print(sumLessThan100000(dictionary))
    values = getPreCounts(dictionary)
    freeSpace = 70000000-findFirstOccurence("/", values)
    required_space = 30000000-freeSpace
    print(findSmallest(values, required_space))

if __name__ == "__main__":
    main()
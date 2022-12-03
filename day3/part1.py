def getRuckascks():
    rucksacks = [] # (compartment 1, compartment 2)
    while True:
        rucksack = input()
        if rucksack == "":
            break
        rucksack = (rucksack[0:int((len(rucksack)/2))],rucksack[int((len(rucksack)/2)):len(rucksack)])
        rucksacks.append(rucksack)
    return rucksacks

def findRepeatedItems(rucksacks):
    print(rucksacks)
    repeatedItems = []
    for rucksack in rucksacks:
        comparisons = []
        for i in rucksack[0]:
            for j in rucksack[1]:
                if (i, j) in comparisons:
                    continue
                if i == j:
                    comparisons.append((i, j))
                    repeatedItems.append(i)
    print(repeatedItems)
    return repeatedItems

def getItempriority(char):
    priority = -96
    if char.isupper():
        priority += 58
    priority += ord(char)
    return priority

def priorityCount(repeatedItems):
    total = 0
    for i in repeatedItems:
        total += getItempriority(i)
    return total

if __name__ == "__main__":
    print(priorityCount(findRepeatedItems(getRuckascks())))

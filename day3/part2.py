from part1 import getItempriority

def findGroups():
    groups = [] #(elf1, elf2, elf3)
    current_group = []
    count = 0
    while True:
        x = input()
        if x == "":
            break
        current_group.append(x)
        count += 1
        if count == 3:
            groups.append(current_group)
            count = 0
            current_group = []
    return groups

def getCommon(group):
    commonItem = ""
    for i in group[0]:
        for j in group[1]:
            for k in group[2]:
                if i == j and j == k:
                    commonItem = i
                    break
    return commonItem

def Count(groups):
    total = 0
    for group in groups:
        commonItem = getCommon(group)
        print(commonItem)
        priority = getItempriority(commonItem)
        total += priority
    return total

                


print(Count(findGroups()))

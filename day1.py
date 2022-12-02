def elfCount():
    elves = []
    running = True
    current_total = 0
    while running:
        x = input()
        if x == "":
            elves.append(current_total)
            current_total = 0
            continue
        
        if int(x) < 0:
            running = False
        current_total += int(x)
    return elves

def sort(l):
    for i in range(len(l), 0, -1):
        noSwaps = True
        for j in range(i-1):
            if l[j] > l[j+1]:
                temp = l[j+1]
                l[j+1] = l[j]
                l[j] = temp
                noSwaps = False
        if noSwaps:
            break
    return l

def reverse(l):
    new_list = []
    for i in range(len(l)-1, 0, -1):
        new_list.append(l[i])
    return new_list

def findTop(l, n):
    sorted = reverse(sort(l))
    return sorted[0:n]

def sumList(l:list):
    total = 0
    for i in l:
        total += i
    return total


print(sumList(findTop(elfCount(), 3)))


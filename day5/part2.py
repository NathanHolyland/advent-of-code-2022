from part1 import getStacks, printEachElement

def performInstructionsFor9001(s, instructions):
    for i in instructions:
        numberOfCrates = int(i[0])
        initial = int(i[1])-1
        final = int(i[2])-1
        block = []

        # take off from the top
        for i in range(numberOfCrates):
            if len(s[initial]) == 0:
                continue
            block.append(s[initial].pop())
        

        # add in reverse order
        for i in range(len(block)-1, -1, -1):
            s[final].append(block[i])
        
    return s

printEachElement(performInstructionsFor9001(*getStacks()))
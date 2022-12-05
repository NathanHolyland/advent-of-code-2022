import re

def getStacks():
    columns = []
    while True:
        x = input()
        if x == "":
            columns.pop()
            break
        splitLine = re.findall('    |\[.\]', x)
        columns.append(splitLine)
    
    stacks = [[] for i in range(len(columns)+1)]
    for r in range(len(columns)-1, -1, -1):
        for c in range(len(columns[r])):
            if columns[r][c] == "    ":
                continue
            stacks[c].append(columns[r][c][1])
    
    instructions = []
    while True:
        instruction = input()
        if instruction == "":
            break
        components = re.findall('[0-9]+', instruction)
        instructions.append(components)
    
    return stacks, instructions

def printEachElement(x):
    for i in x:
        print(i)

#crate mover 9000 can only do it one at a time
def performInstructionsFor9000(stacks, instructions):
    for i in instructions:
        repeats = int(i[0])
        initial = int(i[1])-1
        final = int(i[2])-1
        print(f'performing instruction {initial+1} -> {final+1} {repeats} times')
        for i in range(repeats):
            if len(stacks[initial]) == 0:
                continue
            stacks[final].append(stacks[initial].pop())
    return stacks

if __name__ == "__main__":
    printEachElement(performInstructionsFor9000(*getStacks()))

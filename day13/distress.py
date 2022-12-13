def textToList(line):
    x = []
    currentStr = ""
    skipVals = 0
    for c in range(1, len(line)):
        if skipVals > 0:
            skipVals -= 1
            continue
        char = line[c]
        if char == "," and currentStr != "":
            x.append(currentStr)
            currentStr = ""
        elif char == "[": # recursively construct a new list
            depth = 1
            passed = "["
            for i in range(1, len(line)-c):
                passed += (line[c+i])
                if line[c+i] == "[":
                    depth += 1
                elif line[c+i] == "]":
                    depth -= 1
                if depth == 0:
                    skipVals = i #skip past this point when finding new values
                    break
            returnedVal = textToList(passed)
            x.append(returnedVal)
        elif char == "]":
            if currentStr != "":
                x.append(currentStr)
        else:
            if char == ",":
                continue
            currentStr += char
    return x

def createPairs(lines):
    pairs = []
    pair = []
    for line in lines:
        if line == "":
            pairs.append(pair)
            pair = []
            continue
        pair.append(textToList(line))
    pairs.append(pair)
    return pairs

def testValidity(left, right):
    if type(left) == str and type(right) == str:
        if int(left) == int(right):
            return -1
        if int(left) < int(right):
            return True
        return False

    if type(left) == list and type(right) == list:
        for i in range(min(len(left), len(right))):
            pairValidity = testValidity(left[i], right[i])
            if pairValidity == -1:
                continue
            else:
                return pairValidity
        if len(right) == len(left):
            return -1
        elif len(left) < len(right):
            return True
        return False
    
    if type(left) == str and type(right) == list:
        return testValidity([left], right)
    if type(right) == str and type(left) == list:
        return testValidity(left, [right])
    
def part1():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    pairs = createPairs(lines)
    sum = 0
    for i in range(len(pairs)):
        left = pairs[i][0]
        right = pairs[i][1]
        if testValidity(left, right):
            sum += i+1
    print(sum)

def part2():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    packets = []
    for line in lines:
        if line == "":
            continue
        packets.append(textToList(line))
    
    n = len(packets)

    for i in range(n):
        for j in range(n-i-1):
            if not testValidity(packets[j], packets[j+1]):
                packets[j], packets[j+1] = packets[j+1], packets[j]
    print((packets.index([['2']])+1) * (packets.index([['6']])+1))

def main():
    #part1()
    part2()

if __name__ == "__main__":
    main()
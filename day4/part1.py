def getPairs():
    pairs = []
    while True:
        x = input()
        if x == "":
            break
        split = x.split(",")
        hiloOfPair = [split[0].split("-"), split[1].split("-")]
        pairs.append(hiloOfPair)
    return pairs

def checkIfFullOverlap(pair):
    min0 = int(pair[0][0])
    max0 = int(pair[0][1])
    min1 = int(pair[1][0])
    max1 = int(pair[1][1])

    if (min0 <= min1) and (max0 >= max1):
        return True
    elif (min1 <= min0) and (max1 >= max0):
        return True
    return False

def countOverlaps(pairs):
    count = 0
    for pair in pairs:
        if checkIfFullOverlap(pair):
            count +=1
    return count

if __name__ == "__main__":
    print(countOverlaps(getPairs()))
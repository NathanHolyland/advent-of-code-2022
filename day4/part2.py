from part1 import getPairs

def checkCollision(pair):
    min0 = int(pair[0][0])
    max0 = int(pair[0][1])
    min1 = int(pair[1][0])
    max1 = int(pair[1][1])

    if min1 <= min0 <= max1:
        return True
    elif min0 <= min1 <= max0:
        return True
    return False

def countCollisions(pairs):
    count = 0
    for pair in pairs:
        if checkCollision(pair):
            count += 1
    return count

if __name__ == "__main__":
    print(countCollisions(getPairs()))
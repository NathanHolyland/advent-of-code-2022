def reduceToOnes(vec):
    if vec.x != 0:
        x = vec.x
        reducedX = x/abs(x) # maintains direction
    else:
        reducedX = 0
    if vec.y != 0:
        y = vec.y
        reducedY = y/abs(y)
    else:
        reducedY = 0
    return Vector(reducedX, reducedY)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, v):
        return Vector(self.x+v.x, self.y+v.y)

    def sub(self, v):
        return Vector(self.x-v.x, self.y-v.y)
    
    def magnitude(self):
        return (self.x**2 + self.y**2)**0.5
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

def moveRopePart(leader, follower):
    vec = leader.sub(follower)
    if abs(vec.x) > 1 or abs(vec.y) > 1:
        movementVec = reduceToOnes(vec)
        follower = follower.add(movementVec)
    return follower

def main():
    with open("input.txt") as f:
        movements = f.read().splitlines()
    directions = []
    for movement in movements:
        directions.append(movement.split(" "))
    rope_parts = [Vector(0,0) for i in range(10)]

    toVector = {
        "U": Vector(0,1),
        "D": Vector(0,-1),
        "L": Vector(-1, 0),
        "R": Vector(1, 0)
    }

    unique_end_squares = set()

    for d in directions:
        vector = toVector[d[0]]
        for i in range(int(d[1])):
            rope_parts[0] = rope_parts[0].add(vector)
            for j in range(len(rope_parts)):
                if j == 0:
                    continue
                rope_parts[j] = moveRopePart(rope_parts[j-1], rope_parts[j])
                if j == len(rope_parts)-1:
                    unique_end_squares.add((rope_parts[j].x, rope_parts[j].y))
    
    print(len(unique_end_squares))

if __name__ == "__main__":
    main()
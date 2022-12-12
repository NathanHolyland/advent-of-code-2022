from re import L


def constructMap(path):
    with open(path) as f:
        lines = f.read().splitlines()
    map = []
    for line in lines:
        row = []
        for c in line:
            if c.isupper():
                row.append(c)
                continue
            row.append(ord(c)-ord("a"))
        map.append(row)
    return map

def main():
    map = constructMap("input.txt")
    for row in map:
        for c in row:
            print(c, end="")
        print()
    

if __name__ == "__main__":
    main()
import re

def nicePrint(List2d):
    for r in List2d:
        for c in r:
            print(c, end="")
        print()

def tick(cycle, x, screen):
    pixel = ((cycle-1)%40,(cycle-1)//40)
    try:
        if pixel[0] in [x-1,x,x+1]:
            screen[pixel[1]][pixel[0]] = "#"
        else:
            screen[pixel[1]][pixel[0]] = "."
    except:
        pass

    if cycle%40 == 20:
        print(f"cycle {cycle}: x = {x}: signal strength = {x*cycle}")
        return x*(cycle)
    return 0

def main():
    with open("input.txt") as f:
        commands = f.read().splitlines()
    signalSum = 0
    cycle = 0
    x=1
    screen = [["." for i in range(40)] for i in range(6)]
    print(f"x: {len(screen[0])}, y: {len(screen)}")
    for i in range(len(commands)):
        val = 0
        if commands[i] == "noop":
            cycle += 1
            signalSum += tick(cycle, x, screen)
        elif re.search("addx", commands[i]):
            cycle += 1
            signalSum += tick(cycle, x, screen)
            cycle += 1
            signalSum += tick(cycle, x, screen)
            x += (int(re.findall("-?[0-9]+", commands[i])[0]))
        x += val
    return signalSum, screen

if __name__ == "__main__":
    signalSum, screen = main()
    nicePrint(screen)
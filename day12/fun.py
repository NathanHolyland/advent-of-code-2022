import pygame
import hillclimber
import colorsys

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

def drawMap(List2d,screen,s):
    for r in range(len(List2d)):
        for c in range(len(List2d[r])):
            height = List2d[r][c]
            if type(height) == int:
                x = height/9
                color = hsv2rgb((x*120)/360, 1, 1)
            print(x)
            print(color)
            pygame.draw.rect(screen, color, [s*c,s*r,s,s], 0)

running = True 
map = hillclimber.constructMap("input.txt")
s=7
resolution = [s*len(map[0]),s*len(map)]
print(resolution)
screen = pygame.display.set_mode(resolution)
while running:
    screen.fill((255, 255, 255))
    drawMap(map, screen, s)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
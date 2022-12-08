def findVisibleTrees(table):
    visible_trees = []
    table_height = len(table)
    table_width = len(table[0])
    for r in range(len(table)):
        for c in range(len(table[r])):
            if r%(len(table)-1) == 0 or c%(len(table[r])-1) == 0: #edge trees
                visible_trees.append((r, c))
                continue

            directions = [(-1,0, r+1),(0,-1, c+1),(0,1, table_height-c),(1,0, table_width-r)]
            tree_height = table[r][c]
            visible = False

            #print(f"Looking at ({r}, {c}):")
            for i in directions:
                directionVisible = True
                for x in range(1, i[2]):
                    #print(f"testing: ({r+i[0]*x}, {c+i[1]*x})")
                    if table[r+i[0]*x][c+i[1]*x] >= tree_height:
                        directionVisible = False
                if directionVisible:
                    visible = True
                        
            #print(f"tree: {table[r][c]}\nvisible = {visible}\n")
            if visible:
                visible_trees.append((r, c))
    return visible_trees

def calculateScenicScores(table):
    score_table = {}
    table_height = len(table)
    table_width = len(table[0])
    for r in range(len(table)):
        for c in range(len(table[r])):
            directions = [(-1,0, r+1),(0,-1, c+1),(0,1, table_height-c),(1,0, table_width-r)]
            tree_height = table[r][c]

            #print(f"Looking at ({r}, {c}):")
            score = 1
            for i in range(len(directions)):
                vec = directions[i]
                viewDistance = 0
                for x in range(1, directions[i][2]):
                    #print(f"testing: ({r+i[0]*x}, {c+i[1]*x})")
                    viewDistance += 1
                    if table[r+vec[0]*x][c+vec[1]*x] >= tree_height:
                        break
                    
                score = score * viewDistance
            score_table[(r, c)] = score
    return score_table

def main():
    with open("input.txt") as f:
        rows = f.read().splitlines()
    table = []
    for row in rows:
        new_row = []
        for char in row:
            new_row.append(int(char))
        table.append(new_row)
    #print(len(findVisibleTrees(table)))
    scores = calculateScenicScores(table)
    print(scores)
    bestScore = 0
    for tree in scores.keys():
        if scores[tree] > bestScore:
            bestScore = scores[tree]
    print(bestScore)


if __name__ == "__main__":
    main()
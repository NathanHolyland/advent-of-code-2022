def findVisibleTrees(table):
    visible_trees = []
    table_height = len(table)
    table_width = len(table[0])
    for r in range(len(table)):
        for c in range(len(table[r])):
            if r%(len(table)-1) == 0 or c%(len(table[r])-1) == 0: #edge trees
                visible_trees.append((r, c))
                continue

            directions = [(-1,0, r),(0,-1, c),(0,1, table_height-c),(1,0, table_width-r)]
            tree_height = table[r][c]
            visible = False

            print(f"Looking at ({r}, {c}):")
            for i in directions:
                directionVisible = True
                for x in range(i[2]):
                    if table[r+i[0]*x][c+i[1]*x] > tree_height:
                        directionVisible = False
                if directionVisible:
                    visible = True
                        
            print(f"visible = {visible}\n")
            if visible:
                visible_trees.append((r, c))
    return visible_trees

def main():
    with open("test.txt") as f:
        rows = f.read().splitlines()
    table = []
    for row in rows:
        new_row = []
        for char in row:
            new_row.append(int(char))
        table.append(new_row)
    print(len(findVisibleTrees(table)))

if __name__ == "__main__":
    main()
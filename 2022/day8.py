with open('2022/data/day8.txt') as f:
    raw_input = [line.strip() for line in f.readlines()]

def printsummary(array):

    for i in range(3):
        print(array[i][:3], '...', array[i][-3:])
    for i in range(3):
        print(' .       .')
    for i in range(3):
        print(array[i-3][:3], '...', array[i-3][-3:])

class Tree:
    def __init__(self, height):
        self.height = int(height)
        self.isvisible = False

    def __repr__(self):
        return str(1 if self.isvisible else 0)

#printsummary(raw_input)
# for row in raw_input:
#     print(row)

gridsize = len(raw_input)

treearray = [[Tree(char) for char in row] for row in raw_input]

# array   indexing 
#  [0,0],  [0,1], ...,  [0,98]
#  [1,0],  [1,1], ...,  [1,98]
#   ...     ...          ...
# [98,0], [98,1], ..., [98,98]

#set boundary conditions
edges = treearray[0] + treearray[-1] + [row[0] for row in treearray] + [row[-1] for row in treearray]
for tree in edges:
    tree.isvisible = True

for r, row in enumerate(treearray):
    if r == 0 or r == gridsize-1:
        continue
    else:
        for c, tree in enumerate(row):
            if c == 0 or c == gridsize-1:
                continue
            else:
                # trees are visible if max height in ONE of 4 directions
                # left
                left = treearray[r][:c]
                right = treearray[r][c+1:]
                above = [tree for tree in [treearray[i][c] for i in range(r)]]
                below = [tree for tree in [treearray[i][c] for i in range(r+1, gridsize)]]
                max_out = [max([out.height for out in direction]) for direction in [left,right,above,below]]
                tree.isvisible = any([tree.height > max for max in max_out])

#print(treearray[1])
visiblecount = 0 
for row in treearray:
    rowsum = sum([tree.isvisible for tree in row])
    visiblecount += rowsum

visiblecount = sum([sum([tree.isvisible for tree in row]) for row in treearray])
print('part1 ans:')
print(visiblecount)



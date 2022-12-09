with open('2022/data/day8.txt') as f:
    raw_input = [line.strip() for line in f.readlines()]

def printsummary(array):

    for i in range(3):
        print(array[i][:3], '...', array[i][-3:])
    for i in range(3):
        print(' .       .')
    for i in range(3):
        print(array[i-3][:3], '...', array[i-3][-3:])

def multiplylist(list):
    prod = 1
    for obj in list:
        prod = prod * obj
    return prod

class Tree:
    def __init__(self, height):
        self.height = int(height)
        self.isvisible = False
        self.scenicscore = 0

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
                left.reverse()
                right = treearray[r][c+1:]
                above = [tree for tree in [treearray[i][c] for i in range(r)]]
                above.reverse()
                below = [tree for tree in [treearray[i][c] for i in range(r+1, gridsize)]]
                directions = [above, left,right, below]
                # print(tree.height, [[tree.height for tree in direction] for direction in directions])
                viewing_distances = []
                for direction in directions:
                    visibles = [comparetree.height < tree.height for comparetree in direction]
                    if False not in visibles:
                        viewing_distances.append(len(visibles))
                    else:
                        viewing_distances.append(visibles.index(False)+1)
                    #print(visibles, viewing_distances[-1])
                #print(r,c,tree.height,multiplylist(viewing_distances))
                tree.scenicscore = multiplylist(viewing_distances)
                max_out = [max([out.height for out in direction]) for direction in directions]
                tree.isvisible = any([tree.height > max for max in max_out])

#print(treearray[1])
visiblecount = 0 
for row in treearray:
    rowsum = sum([tree.isvisible for tree in row])
    visiblecount += rowsum

visiblecount = sum([sum([tree.isvisible for tree in row]) for row in treearray])
print('part1 ans:')
print(visiblecount)

print()

max_score = max([max([tree.scenicscore for tree in row]) for row in treearray])
print('part2 ans:')
print(max_score)



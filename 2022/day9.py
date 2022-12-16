from math import sqrt


class Knot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.history = [[self.x,self.y]]

    def move(self,direction):
        if direction == 'L':
            self.x += -1
        if direction == 'R':
            self.x += 1
        if direction == 'U':
            self.y += 1
        if direction == 'D':
            self.y += -1

        self.history.append([self.x, self.y])

    def move_vec(self, v):
        self.x += v[0]
        self.y += v[1]
        self.history.append([self.x, self.y])

    def __repr__(self):
        return f"({self.x}, {self.y})"

def displacement(head: Knot, tail: Knot):
    return [head.x - tail.x, head.y - tail.y]

def norm(vector):
    return sqrt(vector[0]**2+vector[1]**2)

def calculate_tail_reaction(delta):
    if delta in [[-2,1],[-2,2],[-1,2]]:
        return [-1, 1]
    elif delta == [0,2]:
        return [0,1]
    elif delta in [[1,2],[2,2],[2,1]]:
        return [1,1]
    elif delta == [2,0]:
        return [1,0]
    elif delta in [[2,-1],[2,-2],[1,-2]]:
        return [1,-1]
    elif delta == [0,-2]:
        return [0,-1]
    elif delta in [[-1,-2],[-2,-2],[-2,-1]]:
        return [-1,-1]
    elif delta == [-2,0]:
        return [-1,0]

head = Knot()
tail = Knot()

moves = []
with open('2022/data/day9.txt') as f:
    for line in f.readlines():
        direction, distance = line.strip().split(' ')
        moves.append([direction, int(distance)])

for move in moves:
    for i in range(move[1]):
        head.move(move[0])
        d = displacement(head,tail)
        if norm(d)>sqrt(2):
            tail.move_vec(calculate_tail_reaction(d))

unique_history = []
for pos in tail.history:
    if pos not in unique_history:
        unique_history.append(pos)

print(len(unique_history))
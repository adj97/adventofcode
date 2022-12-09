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

    def __repr__(self):
        return f"({self.x}, {self.y})"

def displacement(head: Knot, tail: Knot):
    return [head.x - tail.x, head.y - tail.y]

def norm(vector):
    return sqrt(vector[0]**2+vector[1]**2)

head = Knot()
tail = Knot()

moves = []
with open('2022/data/day9_.txt') as f:
    for line in f.readlines():
        direction, distance = line.strip().split(' ')
        moves.append([direction, int(distance)])

for move in moves:
    for i in range(move[1]):
        head.move(move[0])
        d = displacement(head,tail)
        print(head, tail, norm(d))
        if norm(d)>sqrt(2):
            print('tail moves')
        break
    break

# print(head.history)
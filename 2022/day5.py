with open('2022/data/day5.txt') as f:
    lines = f.readlines()
    data = [lines[0].replace('\n', '')] + [line.strip() for line in lines[1:]]

class Move:
    def __init__(self, raw):
        raw_split = raw.split(' ')
        self.amount = raw_split[1]
        self.fromm = int(raw_split[3])-1
        self.to = int(raw_split[5])-1

    def __repr__(self):
        return f"{self.amount}, {self.fromm}, {self.to}"

i = data.index('')
formation = data[:i]
moves = [Move(d) for d in data[i+1:]]

# 1, 5, 9, ...
cols = []
for i in range(len(formation)-1):
    line = formation[i]
    cols.append([line[4*i+1] for i in range(8)])

stacks = [[],[],[],[],[],[],[],[]]
for i, stack in enumerate(stacks):
    stacks[i] = [cols[7-j][i] for j in range(8)]

for stack in stacks:
    print(stack)

for move in moves:
    print(move)
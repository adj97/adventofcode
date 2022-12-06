with open('2022/data/day5.txt') as f:
    lines = f.readlines()
    data = [lines[i].replace('\n', '') for i in range(9)] + [line.strip() for line in lines[9:]]

class Move:
    def __init__(self, raw):
        raw_split = raw.split(' ')
        self.amount = int(raw_split[1])
        self.fromm = int(raw_split[3])-1
        self.to = int(raw_split[5])-1

    def __repr__(self):
        return f"{self.amount}, {self.fromm}, {self.to}"

i = data.index('')
formation = data[:i]

moves = [Move(d) for d in data[i+1:]]

cols = []
for i in range(len(formation)-1):
    line = formation[i]
    cols.append([line[4*i+1] for i in range(9)])


stacks = [[],[],[],[],[],[],[],[],[]]
for i, stack in enumerate(stacks):
    stacks[i] = [cols[7-j][i] for j in range(8)]

stacks = [[s for s in stack if s != ' '] for stack in stacks]

# for i, stack in enumerate(stacks):
#     print(i, stack)

for move in moves:
    # print()
    # print(move)
    # print()
    to_keep = stacks[move.fromm][:len(stacks[move.fromm])-move.amount]
    to_move = stacks[move.fromm][-move.amount:]
    stacks[move.fromm] = to_keep
    stacks[move.to] += to_move
    # for i, stack in enumerate(stacks):
    #     print(i, stack)
    # print()



print('part1 ans:')
for stack in stacks:
    print(stack[-1],end="")
print()
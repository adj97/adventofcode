with open('2022/data/day1.txt') as f:
    data = [s.strip() for s in f.readlines()]

elves = [[]]
for i in data:
    if not i:
        elves.append([])
    else:
        elves[-1].append(int(i))

totals = [sum(cals) for cals in elves]

print(max(totals))
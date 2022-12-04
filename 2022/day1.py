with open('2022/data/day1.txt') as f:
    data = [s.strip() for s in f.readlines()]

elves = [[]]
for i in data:
    if not i:
        elves.append([])
    else:
        elves[-1].append(int(i))

totals = [sum(cals) for cals in elves]

print('part 1:', max(totals))

totals.sort()

top3 = totals[-1] + totals[-2] + totals[-3]

print('part 2:', top3)
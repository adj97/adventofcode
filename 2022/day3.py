from typing import List
from string import ascii_lowercase, ascii_uppercase

with open('2022/data/day3.txt') as f:
    data = [s.strip() for s in f.readlines()]

priorities = ' ' + ascii_lowercase + ascii_uppercase

class Rucksack():
    def __init__(self, raw, compartment1, compartment2, common):
        self.raw = raw
        self.compartment1 = compartment1
        self.compartment2 = compartment2
        self.common = common
        self.calculate_common_priority()
        return

    def calculate_common_priority(self):
        self.common_priority = priorities.index(self.common[0])
        return

class Group():
    def __init__(self, members):
        self.members = members
        self.find_badge()

    def find_badge(self):
        common = list(set(self.members[0].raw).intersection(self.members[1].raw).intersection(self.members[2].raw))
        self.badge = common[0]
        self.badge_effort = priorities.index(self.badge)
        return

rucksacks: List[Rucksack] = []
for d in data:
    i_half = int(len(d)/2)
    c1 = d[:i_half]
    c2 = d[i_half:]
    common = list(set(c1).intersection(c2))
    rucksacks.append(Rucksack(d, c1, c2, common))

priority_sum = sum([r.common_priority for r in rucksacks])
print('part1:', priority_sum)

groups: List[Group] = []
for j in range(int(len(rucksacks)/3)):
    indexes = [j*3+1, j*3+2, j*3+3]
    groups.append(
        Group([r for r in [rucksacks[i-1] for i in indexes]])
    )

group_badge_effort_priority_sum = sum([group.badge_effort for group in groups])
print('part2:', group_badge_effort_priority_sum)
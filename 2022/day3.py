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
        self.common_priority = None
        return

    def calculate_common_priority(self):
        self.common_priority = priorities.index(self.common[0])
        return

rucksacks: List[Rucksack] = []
for d in data:
    i_half = int(len(d)/2)
    c1 = d[:i_half]
    c2 = d[i_half:]
    common = list(set(c1).intersection(c2))
    r = Rucksack(d, c1, c2, common)
    r.calculate_common_priority()
    rucksacks.append(r)

priority_sum = sum([r.common_priority for r in rucksacks])
print('part1:', priority_sum)
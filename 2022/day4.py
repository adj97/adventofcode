with open('2022/data/day4.txt') as f:
    data = [s.strip().split(',') for s in f.readlines()]

class Elf():
    def __init__(self, elf):
        self.start = int(elf[0])
        self.end = int(elf[1])

    def __repr__(self):
        return ' '*self.start + str(self.start) + '-'*(self.end-self.start) + str(self.end) + ' '*5


class Pair():
    def __init__(self, elf1, elf2):
        self.elf1 = Elf(elf1)
        self.elf2 = Elf(elf2)
        self.fully_contained = None
        self.overlap = None

    def __repr__(self):
        output = self.elf1.__repr__() + '\n' + self.elf2.__repr__() + str(self.overlap) + '\n\n'
        return output

    def calculate_overlap(self):
        self.overlap = self.elf2.start <= self.elf1.end and self.elf2.end >= self.elf1.start
        return


pairs = [Pair(d[0].split('-'), d[1].split('-')) for d in data]

for pair in pairs:
    big_top = (pair.elf1.start <= pair.elf2.start) and (pair.elf1.end >= pair.elf2.end)
    big_bottom = (pair.elf1.start >= pair.elf2.start) and (pair.elf1.end <= pair.elf2.end)
    pair.fully_contained = big_top or big_bottom
    pair.calculate_overlap()

contained_count = sum([pair.fully_contained for pair in pairs])
print('part1:', contained_count)

overlap_count = sum([pair.overlap for pair in pairs])
print('part2:', overlap_count)
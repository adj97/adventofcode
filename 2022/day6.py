with open('2022/data/day6.txt') as f:
    stream = f.read()

def get_min_chars_processed(marker_length):

    for i in range(len(stream)-(marker_length-1)):
        this_marker = stream[i:i+marker_length]
        if (len(this_marker) == len(set(this_marker))):
            return i+marker_length

print('part1 ans:')
print(get_min_chars_processed(4))

print('part2 ans:')
print(get_min_chars_processed(14))
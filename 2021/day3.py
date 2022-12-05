import numpy as np

# process instructions
file1 = open('day3data.txt', 'r')
lines = file1.readlines()

obits = [[],[],[],[],[],[],[],[],[],[],[],[]]

for line in lines:
    for j,char in enumerate(line.strip()):
        obits[j].append(int(char))

counts = [[sum([b==x for b in bit]) for x in [0,1]] for bit in obits]
gamma_bin = ''.join([str(count.index(max(count))) for count in counts])
epsilon_bin = ''.join([str(1-count.index(max(count))) for count in counts])
gamma_dec = int(gamma_bin,2)
epsilon_dec = int(epsilon_bin,2)

# part 1
#print(gamma_dec * epsilon_dec)

# part 2

# oxygen

numbers = [''.join([str(n[x]) for n in obits]) for x in range(0,len(obits[0]))] # numbers from bits
bits = [''.join([str(n[x]) for n in numbers]) for x in range(0,len(numbers[0]))] # bits from numbers

for i in range(0,len(bits[0])):
    numbers = [''.join([str(b[x]) for b in bits]) for x in range(0,len(bits[0]))]
    count = [sum([b==x for b in bits[i]]) for x in ["0","1"]]
    maxval = str(count.index(max(count)))
    numbers = [n for n in numbers if n[i] == str(maxval)]

    if len(numbers)==1: 
        print(numbers)
        break

    bits = [''.join([str(n[x]) for n in numbers]) for x in range(0,len(numbers[0]))]

oxygen = int(numbers[0],2)


#co2

numbers = [''.join([str(n[x]) for n in obits]) for x in range(0,len(obits[0]))] # numbers from bits
bits = [''.join([str(n[x]) for n in numbers]) for x in range(0,len(numbers[0]))] # bits from numbers


for i in range(0,len(bits[0])):
    numbers = [''.join([str(b[x]) for b in bits]) for x in range(0,len(bits[0]))]

    count = [sum([b==x for b in bits[i]]) for x in ["0","1"]]
    minval = str(count.index(min(count)))
    
    numbers = [n for n in numbers if n[i] == minval]

    if len(numbers)==1:
        print(numbers)
        break

    bits = [''.join([str(n[x]) for n in numbers]) for x in range(0,len(numbers[0]))]

co2 = int(numbers[0],2)

print(oxygen,"x",co2,"=",oxygen*co2)

# process instructions
file1 = open('day2data.txt', 'r')
lines = file1.readlines()

for i,s in enumerate(lines):
    lines[i] = s.strip()

# # init co-ords
# h,d = 0,0

# for line in lines:
#     action = line.split()[0]
#     amount = int(line.split()[1])

#     if action == "forward":
#         h += amount
#     elif action == "down":
#         d += amount
#     elif action == "up":
#         d -= amount

# # part 1
# print(h*d)

# init co-ords
h,d, a = 0, 0, 0

for line in lines:
    action = line.split()[0]
    amount = int(line.split()[1])

    if action == "forward":
        h += amount
        d += a*amount
    elif action == "down":
        a += amount
    elif action == "up":
        a -= amount

# part 2
print(h*d)
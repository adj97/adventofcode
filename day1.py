import csv

with open('day1data.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

data[0][0] = data[0][0][3:]

data = [int(d) for d in data[0]]

goes_up = 0
for d in range(1,len(data)):
    if data[d]>data[d-1]:
        goes_up += 1

# day 1
#print(goes_up)

sliding_windows = []
for i in range(0,len(data)-2):
    sliding_windows.append(data[i]+data[i+1]+data[i+2])

sw_goes_up = 0
for i in range(1,len(sliding_windows)):
    if sliding_windows[i]>sliding_windows[i-1]:
        sw_goes_up += 1

# day 2
print(sw_goes_up)
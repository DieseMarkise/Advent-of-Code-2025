x = []
voltage = 0
input = "Puzzle 5/input.csv"

with open(input) as f:
    for line in f:
        x.append(line.rstrip('\n'))

for line in x:
    temp = 0
    i = 0
    j = 1
    while j < len(line):
        while i < j:
            if int(line[i] + line[j]) > temp: temp = int(line[i] + line[j])
            i += 1
        j += 1
        i = 0
    voltage += temp

print(voltage)
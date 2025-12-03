x = []
voltage = 0
lengthVoltage = 12
input = "Puzzle 6/input.csv"

with open(input) as f:
    for line in f:
        x.append(line.rstrip('\n'))

for line in x:
    number = []
    temp = '0'
    j = 0
    k = 0
    for i in range(lengthVoltage - 1, -1, -1):
        while (j < len(line) - i):
            if line[j] > temp:
                temp = line[j]
                k = j + 1
            if temp == '9':
                break
            j += 1
        number.append(temp)
        temp = '0'
        j = k
    voltage += int(''.join(map(str,number)))

print(voltage)
list = []

number = 50

count = 0

with open ('Puzzle 2/input.csv') as file:
    for line in file:
        match line[0]:
            case 'R':
                i = 0
                while (i < int(line[1:])):
                    number += 1
                    if number == 100:
                        number = 0
                    if number == 0:
                        count +=1
                    i += 1
            case 'L':
                i = 0
                while (i < int(line[1:])):
                    number = (number - 1) % 100
                    if number == 0:
                        count +=1
                    i += 1
            case _:
                print("Kein R oder L erkannt")

print(count)
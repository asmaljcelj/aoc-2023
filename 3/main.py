import re

filename = 'input.txt'

file1 = open(filename, 'r')
lines = file1.readlines()

sum = 0
gears = 0
potential_gear_positions = dict()
for row, line in enumerate(lines):
    line = line.strip()
    for match in re.finditer(r'[0-9]+', line):
        start = match.start()
        end = match.end()
        number = int(match.group())
        # PART 1
        # check left
        # if start > 0 and line[start - 1] != '.' and not line[start - 1].isdigit():
        #     sum += number
        #     print('including', number)
        #     continue
        # # check right
        # if end < len(line) and line[end] != '.' and not line[end].isdigit():
        #     sum += number
        #     print('including', number)
        #     continue
        # for index in range(start - 1, end + 1):
        #     if index < 0 or index >= len(line):
        #         continue
        #     # check up
        #     if row > 0 and lines[row - 1][index] != '.' and not lines[row - 1][index].isdigit():
        #         sum += number
        #         print('including', number)
        #         break
        #     # check down
        #     if row != len(lines) - 1 and lines[row + 1][index] != '.' and not lines[row + 1][index].isdigit():
        #         sum += number
        #         print('including', number)
        #         break
        #     if index == end:
        #         print('-------- not including', number)
        # PART 2
        if start > 0 and line[start - 1] == '*':
            if (row, start - 1) not in potential_gear_positions.keys():
                potential_gear_positions[(row, start - 1)] = []
            potential_gear_positions[(row, start - 1)].append(number)
            continue
        # check right
        if end < len(line) and line[end] == '*':
            if (row, end) not in potential_gear_positions.keys():
                potential_gear_positions[(row, end)] = []
            potential_gear_positions[(row, end)].append(number)
            continue
        for index in range(start - 1, end + 1):
            if index < 0 or index >= len(line):
                continue
            # check up
            if row > 0 and lines[row - 1][index] == '*':
                # sum += number
                # print('including', number)
                if (row - 1, index) not in potential_gear_positions.keys():
                    potential_gear_positions[(row - 1, index)] = []
                potential_gear_positions[(row - 1, index)].append(number)
                break
            # check down
            if row != len(lines) - 1 and lines[row + 1][index] == '*':
                if (row + 1, index) not in potential_gear_positions.keys():
                    potential_gear_positions[(row + 1, index)] = []
                potential_gear_positions[(row + 1, index)].append(number)
                break

for gear in potential_gear_positions:
    if len(potential_gear_positions[gear]) == 2:
        num1 = potential_gear_positions[gear][0]
        num2 = potential_gear_positions[gear][1]
        sum += (num1 * num2)
print('sum of OK numbers/gears:', sum)

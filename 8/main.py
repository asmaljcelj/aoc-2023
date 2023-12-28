import math

filename = 'input.txt'

file1 = open(filename, 'r')
lines = file1.readlines()
start_string = 'AAA'
end_string = 'ZZZ'
command = ''
map_plan = []
starts = []
order_strings = []

# read map
for row, line in enumerate(lines):
    line = line.strip()
    if row == 0:
        command = line
    elif len(line) > 0:
        split = line.split(' = ')
        # append only rows with nodes
        order_strings.append(split[0])
        if split[0].endswith('A'):
            starts.append(row - 2)
        map_split = split[1].split(',')
        directions = []
        for s in map_split:
            string = ''
            for a in s:
                if a.isalpha() or a.isdigit():
                    string += a
            directions.append(string)
        map_plan.append([split[0], directions])


# handle directions
steps = 0
print(starts)
continue_search = [True for _ in range(len(starts))]
# continue_search = True
new_indexes = []
steps_for_each = [0 for _ in range(len(starts))]
while any(continue_search):
    for c in command:
        for i, start in enumerate(starts):
            if map_plan[start][0].endswith('Z'):
                continue_search[i] = False
                new_indexes.append(start)
                continue
            steps_for_each[i] += 1
            if c == 'L':
                new = order_strings.index(map_plan[start][1][0])
                new_indexes.append(new)
            elif c == 'R':
                new = order_strings.index(map_plan[start][1][1])
                new_indexes.append(new)
        starts = new_indexes
        new_indexes = []

print('steps=', steps_for_each)


def find_lcm_of_list(numbers):
    lcm_result = 1
    for number in numbers:
        lcm_result = math.lcm(lcm_result, number)
    return lcm_result


result = find_lcm_of_list(steps_for_each)
print(result)
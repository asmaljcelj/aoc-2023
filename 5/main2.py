filename = 'input.txt'

file1 = open(filename, 'r')
lines = file1.readlines()
values = []
modified = []
new_values = []

for line in lines:
    line = line.strip()
    if line.startswith('seeds'):
        split = line.split(' ')
        start_and_length = []
        for s in split:
            if s.isnumeric():
                start_and_length.append(int(s))
                if len(start_and_length) == 2:
                    values.append(start_and_length)
                    start_and_length = []
        modified = [False for _ in range(len(values))]
    if len(line) == 0:
        if len(new_values) > 0:
            for i, changed in enumerate(modified):
                # if block is unchanged add it to new values
                if not changed:
                    new_values.append(values[i])
            values = new_values
            new_values = []
        print('current values after segment:', values)
        modified = [False for _ in range(len(values))]
        continue
    # handle all rows that starts with digits (actual maps)
    if line[0].isdigit():
        split = line.split(' ')
        destination_range_start = int(split[0])
        source_range_start = int(split[1])
        length = int(split[2])
        for i, start_length in enumerate(values):
            old_start = start_length[0]
            old_length = start_length[1]
            # check if map start and end is between mentioned start
            if source_range_start <= old_start < source_range_start + length and not modified[i]:
                modified[i] = True
                # old max is higher, divide into 2 parts
                if old_start + old_length - (source_range_start + length) > 0:
                    # first part
                    new_start = destination_range_start + (old_start - source_range_start)
                    new_length = source_range_start + length - old_start
                    new_values.append([new_start, new_length])
                    # second part
                    new_start2 = source_range_start + length
                    new_length2 = old_length - new_length
                    new_values.append([new_start2, new_length2])
                # only move start, preserve length
                else:
                    new_start = destination_range_start + (old_start - source_range_start)
                    new_values.append([new_start, old_length])
            # destination starts after old_start
            elif old_start < source_range_start <= old_start + old_length and not modified[i]:
                modified[i] = True
                new_length = old_length - (source_range_start - old_start)
                new_values.append([destination_range_start, new_length])
                new_values.append([old_start, old_length - new_length])

if len(new_values) > 0:
    for i, changed in enumerate(modified):
        # if block is unchanged add it to new values
        if not changed:
            new_values.append(values[i])
    values = new_values
    new_values = []

print('final values:', values)
print('min=', min(values))

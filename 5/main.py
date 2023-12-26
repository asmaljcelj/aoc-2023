filename = 'input.txt'

file1 = open(filename, 'r')
lines = file1.readlines()
values = []
modified = []

for line in lines:
    line = line.strip()
    if line.startswith('seeds'):
        split = line.split(' ')
        for s in split:
            # append all numbers as seeds
            if s.isnumeric():
                values.append(int(s))
        print('initial values:', values)
        modified = [False for _ in range(len(values))]
    if len(line) == 0:
        print('current values:', values)
        modified = [False for _ in range(len(values))]
        continue
    # handle all rows that starts with digits (actual maps)
    if line[0].isdigit():
        split = line.split(' ')
        destination_range_start = int(split[0])
        source_range_start = int(split[1])
        length = int(split[2])
        for i, value in enumerate(values):
            # check if in range
            if source_range_start + length > value >= source_range_start and not modified[i]:
                # change value
                print('changed', values[i], 'to', destination_range_start + (value - source_range_start))
                values[i] = destination_range_start + (value - source_range_start)
                modified[i] = True
    else:
        print('now processing:', line)
print('final values:', values)
print('min is', min(values))

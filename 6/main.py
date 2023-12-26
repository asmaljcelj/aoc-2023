filename = 'input.txt'

file1 = open(filename, 'r')
lines = file1.readlines()
times = []
distances = []
races = []
result = 1

for line in lines:
    line = line.strip()
    split = line.split(' ')
    # read the time
    if split[0] == 'Time:':
        # PART 1
        # for number in split:
        #     if number.isdigit():
        #         times.append(int(number))
        # PART 2
        total_num = 0
        for number in split:
            if number.isdigit():
                for place in range(len(number)):
                    total_num *= 10
                    total_num += int(number[place])
        times.append(total_num)
    else:
        # PART 1
        # for number in split:
        #     if number.isdigit():
        #         distances.append(int(number))
        # PART 2
        total_num = 0
        for number in split:
            if number.isdigit():
                for place in range(len(number)):
                    total_num *= 10
                    total_num += int(number[place])
        distances.append(total_num)
# combine times and distances
for i in range(len(times)):
    races.append([times[i], distances[i]])
# calculate for each race
for i, race in enumerate(races):
    possibilities = 0
    record_time = race[0]
    record_distance = race[1]
    for holding_time in range(1, record_time):
        distance = holding_time * (record_time - holding_time)
        if distance > record_distance:
            possibilities = possibilities + 1
    print('possibilities for race', i, '=', possibilities)
    if possibilities > 0:
        result = result * possibilities
print('result = ', result)


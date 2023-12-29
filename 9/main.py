filename = 'input.txt'
file = open(filename, 'r')
lines = file.readlines()
total_sum = 0

# read history
for row, line in enumerate(lines):
    line = line.strip()
    # read history
    history = []
    split = line.split(' ')
    for value in split:
        history.append(int(value))
    # construct sequences
    sequences = [history]
    length = len(sequences)
    while not all(v == 0 for v in sequences[length - 1]):
        new_sequence = []
        for i, value in enumerate(sequences[length - 1]):
            if i == len(sequences[length - 1]) - 1:
                # don't compare last number with next one, out of bounds
                continue
            new_sequence.append(sequences[length - 1][i + 1] - value)
        sequences.append(new_sequence)
        length += 1
    print('before extrapolation forwards/backwards')
    print(sequences)
    # extrapolate
    # sequences[length - 1].append(0)
    sequences[length - 1].insert(0, 0)
    # for i in range(length - 2, -1, -1):
    for i in range(length - 2, -1, -1):
        length_of_current_sequence = len(sequences[i])
        # get increment from higher level
        # increment = sequences[i + 1][length_of_current_sequence - 1]
        increment = sequences[i + 1][0]
        # calculate new value
        # result = sequences[i][length_of_current_sequence - 1] + increment
        result = sequences[i][0] - increment
        # sequences[i].append(result)
        sequences[i].insert(0, result)
        # if we are in the uppermost row, add the result
        if i == 0:
            total_sum += result
    print('after extrapolation forwards/backwards')
    print(sequences)
print('result =', total_sum)



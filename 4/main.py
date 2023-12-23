filename = 'input.txt'

file1 = open(filename, 'r')
lines = file1.readlines()
total = 0
copies = [1 for _ in range(len(lines))]
for row, line in enumerate(lines):
    line = line.strip()
    split = line.split(' ')
    winning = []
    winning_ended = False
    # points = 0
    ocurrences_count = 0
    for word in split:
        if word.isdigit():
            number = int(word)
            if winning_ended and number in winning:
                # PART 1
                # if points == 0:
                #     points = 1
                # else:
                #     points *= 2
                # PART 2
                ocurrences_count += 1
            else:
                winning.append(number)
        if word == '|':
            winning_ended = True
    for i in range(ocurrences_count):
        copies[row + 1 + i] += copies[row]
    # print(points)
    # total += points
# print('total=', total)
print(sum(copies))

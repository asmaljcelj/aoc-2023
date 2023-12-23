filename = 'input.txt'

file1 = open(filename, 'r')
Lines = file1.readlines()

# PART 1
# max_red = 12
# max_green = 13
# max_blue = 14
# sum_ids = 0
# PART 2
value = 0
for line in Lines:
    split_by_column = line.split(':')
    game_id = split_by_column[0].split()[1]
    pulls = split_by_column[1].strip().split(';')
    valid = True
    min_red = -1
    min_green = -1
    min_blue = -1
    for pull in pulls:
        attempt = pull.split(',')
        for at in attempt:
            at = at.strip()
            number_color = at.split()
            number = int(number_color[0])
            color = number_color[1]
            # PART 1
            # if color == 'blue' and number > max_blue:
            #   valid = False
            #  break
            # if color == 'red' and number > max_red:
            #   valid = False
            #  break
            # if color == 'green' and number > max_green:
            #    valid = False
            #   break
    #   if not valid:
    #      break
    # if valid:
    #    sum_ids += int(game_id)
    # PART 2
            if color == 'blue' and (number > min_blue or min_blue == -1):
                min_blue = number
            if color == 'green' and (number > min_green or min_green == -1):
                min_green = number
            if color == 'red' and (number > min_red or min_red == -1):
                min_red = number
    value += min_red * min_blue * min_green

#print(sum_ids)
print(value)
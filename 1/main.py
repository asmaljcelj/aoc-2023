filename = 'input.txt'

file1 = open(filename, 'r')
Lines = file1.readlines()

sum = 0
# Strips the newline character
for line in Lines:
    first = -1
    last = -1
    for letter in line:
        if letter.isdigit():
            if first == -1:
                first = int(letter)
            last = int(letter)
    num = first * 10 + last
    #print(num)
    sum += num
print(sum)
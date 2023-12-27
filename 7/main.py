filename = 'input.txt'


def get_score(e):
    return e[0]


def get_hand(e):
    return e[1][0]


file1 = open(filename, 'r')
lines = file1.readlines()
cards_and_bids = []
order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
order_2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
alphabet = 'AKQJT98765432'
alphabet_2 = 'AKQT98765432J'


def compare_strings(string1, string2):
    for i in range(len(string1)):
        index1 = alphabet_2.find(string1[i])
        index2 = alphabet_2.find(string2[i])
        if index1 > index2:
            return 1
        elif index2 > index1:
            return -1
    return 0


def sort_same_scores(same_scores):
    for i in range(len(same_scores) - 1):
        for j in range(len(same_scores) - i - 1):
            if compare_strings(same_scores[j][1][0], same_scores[j + 1][1][0]) < 0:
                temp = same_scores[j]
                same_scores[j] = same_scores[j + 1]
                same_scores[j + 1] = temp
    return same_scores


# read hands and bids
for line in lines:
    line = line.strip()
    split = line.split(' ')
    cards_and_bids.append([split[0], int(split[1])])

# scores: 7 = five of a kind, 1 = high card
scores = []
# analyze each hand
for player in cards_and_bids:
    cards = player[0]
    bid = player[1]
    # figure out their total score
    occurrences = [0 for _ in range(len(order_2))]
    for card in cards:
        index = order_2.index(card)
        occurrences[index] = occurrences[index] + 1
    jokers = occurrences[12]
    # get maximum value without jokers
    no_jokers_occurrences = occurrences[:-1]
    max_index = no_jokers_occurrences.index(max(no_jokers_occurrences))
    occurrences[max_index] += jokers
    occurrences[12] = 0
    if not any(o > 1 for o in occurrences):
        # only 1 and zeros -> high card
        scores.append([1, player])
        continue
    for occurrence in occurrences:
        if occurrence == 5:
            # five of a kind
            scores.append([7, player])
            break
        if occurrence == 4:
            # four of a kind
            scores.append([6, player])
            break
        if occurrence == 3:
            if any(o == 2 for o in occurrences):
                # full house
                scores.append([5, player])
                break
            else:
                # three of a kind
                scores.append([4, player])
                break
        if occurrence == 2:
            if any(o == 2 for o in occurrences) and len([i for i in occurrences if i == 2]) > 1:
                # two pair
                scores.append([3, player])
                break
            elif any(o == 3 for o in occurrences):
                # full house
                scores.append([5, player])
                break
            else:
                # one pair
                scores.append([2, player])
                break
# sort
scores.sort(key=get_score)
print(scores)

current_value = 1
same_scores = []
final_standings = []
for score in scores:
    if score[0] != current_value and len(same_scores) > 0:
        # different score, sort them
        same_scores = sort_same_scores(same_scores)
        print(same_scores)
        final_standings = final_standings + same_scores
        current_value = score[0]
        same_scores = [score]
    else:
        current_value = score[0]
        same_scores.append(score)
same_scores = sort_same_scores(same_scores)
print(same_scores)
final_standings = final_standings + same_scores
print('final:', final_standings)

result = 0
for i, player in enumerate(final_standings):
    result += ((i + 1) * player[1][1])
print(result)

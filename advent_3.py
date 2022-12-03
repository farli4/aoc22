import string

# for task 1 and 2: creating a map to with characters - priority pairs --> lookup table
def set_priorities():
    prio_keys = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    prio_values = list(range(1, 53))
    priorities = dict(zip(prio_keys, prio_values))
    return priorities

# for both tasks : create priority dict
prios = set_priorities()

# 1st Task:
# read file into list containing lists of two sets that contain the characters of the first and second compartment each
with open('3_input.txt', mode='r') as f:
    rucksacks_divided = [[set(line.rstrip()[0: int(len(line.rstrip())/2)]), 
                          set(line.rstrip()[int(len(line.rstrip())/2):len(line.rstrip())])] for line in f]

score_misplaced_items = 0
for i in range(len(rucksacks_divided)):
    common_item = rucksacks_divided[i][0] & rucksacks_divided[i][1]
    score_misplaced_items += prios[common_item.pop()]

print(f'total priority score of misplaced items: {score_misplaced_items}')

# 2nd Task:
# use the rucksacks_divided from the first task and rejoin the two sets representing the two compartments
rucksacks_undivided = [item[0].union(item[1])
                       for item in rucksacks_divided]

score_badge_items = 0
for i in range(0, len(rucksacks_undivided), 3):
    common_item = rucksacks_undivided[i] & rucksacks_undivided[i +
                                                               1] & rucksacks_undivided[i+2]
    score_badge_items += prios[common_item.pop()]

print(f'total priority score of team badges: {score_badge_items}')

# below: another solution with more functions (but also longer code)

""" import string

# for task 1 and 2: creating a map to with characters - priority pairs --> lookup table
def set_priorities():
    prio_keys = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    prio_values = list(range(1, 53))
    priorities = dict(zip(prio_keys, prio_values))
    return priorities


# for task 1: function to produce a list with the single characters that are to be found in both the first and second compartment
def common_items_within_rucksack(rs):
    common_items = []
    for i in range(len(rs)):
        common_item = rs[i][0] & rs[i][1]
        common_items.append(common_item.pop())
    return common_items

# for task 2: return the list of characters that are to be found in both the first and second compartment
def common_items_within_group(rs):
    common_items = []
    for i in range(0, len(rs), 3):
        common_item = rs[i] & rs[i+1] & rs[i+2]
        common_items.append(common_item.pop())
    return common_items


# for task 1 and 2: find the matching priority values for each common item in the rucksacks_divided' two compartments and sum these values
# if third param is true, we call the appropriate func for task 1, if false, we call the appr. func for task 2
def get_sum_priorities(rs, prios, within_rucksack):
    sum_of_prios = 0
    if within_rucksack:
        for item in common_items_within_rucksack(rs):
            sum_of_prios += prios[item]
    else:
        for item in common_items_within_group(rs):
            sum_of_prios += prios[item]
    return sum_of_prios


if __name__ == '__main__':

    priorities = set_priorities()
    
    # 1st Task:
    # read file into list containing lists of two sets that contain the characters of the first and second compartment each
    with open('3_input.txt', mode='r') as f:
        rucksacks_divided = [[set(line.rstrip()[0: int(len(line.rstrip())/2)]), set(line.rstrip()
                                                                                    [int(len(line.rstrip())/2):len(line.rstrip())])] for line in f]
    score_misplaced_items = get_sum_priorities(
        rucksacks_divided, priorities, True)
    print(f'total priority score of misplaced items: {score_misplaced_items}')


    # 2nd Task:
    # use the rucksacks_divided from the first task and rejoin the two sets representing the two compartments
    rucksacks_undivided = [item[0].union(item[1])
                           for item in rucksacks_divided]
    score_badge_items = get_sum_priorities(
        rucksacks_undivided, priorities, False)
    print(f'total priority score of team badges: {score_badge_items}') """




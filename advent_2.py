import pandas as pd


def categorize_winlosedraw(row, task):
    p1 = row['Player_1']
    p2 = row['Player_2_info']
    if task == 'A':
        if p1 == p2:
            return 3
        elif p1 == 'A' and p2 == 'B':
            return 6
        elif p1 == 'B' and p2 == 'C':
            return 6
        elif p1 == 'C' and p2 == 'A':
            return 6
        else:
            return 0
    if task == 'B':
        if p2 == 'A':
            return 0
        elif p2 == 'B':
            return 3
        else:
            return 6


def categorize_weapon(row, task):
    p1 = row['Player_1']
    p2 = row['Player_2_info']
    if task == 'A':
        if p2 == 'A':
            return 1
        elif p2 == 'B':
            return 2
        else:
            return 3
    if task == 'B':
        if p2 == 'A' == p1 or (p2 != 'A' != p1 and p1 != p2):
            return 3
        elif p2 == 'B' == p1 or (p2 != 'B' != p1 and p1 != p2):
            return 2
        else:
            return 1


# load data from file into pandas dataframe (wih 2 columns initially)
all_rounds = pd.read_csv("2_1_input.txt", sep=" ", header=None)
all_rounds.columns = ['Player_1', 'Player_2_info']

# switch X, Y, Z to A,B,C respectively:
# doesnt make a big difference but a bit easier to compare values and also less confusing for me
# BUT: note, that the letters in first column don't have the same meaning as in the second column in case of TASK B
all_rounds.loc[(all_rounds['Player_2_info'] == 'X'), "Player_2_info"] = 'A'
all_rounds.loc[(all_rounds['Player_2_info'] == 'Y'), "Player_2_info"] = 'B'
all_rounds.loc[(all_rounds['Player_2_info'] == 'Z'), "Player_2_info"] = 'C'

# Task 1 (Task A)
all_rounds['Points_from_result_A'] = all_rounds.apply(
    lambda row: categorize_winlosedraw(row, 'A'), axis=1)
all_rounds['Points_from_weapon_choice_A'] = all_rounds.apply(
    lambda row: categorize_weapon(row, 'A'), axis=1)
all_rounds['Points_combined_A'] = all_rounds['Points_from_result_A'] + \
    all_rounds['Points_from_weapon_choice_A']

final_score_A = all_rounds['Points_combined_A'].sum()


# Task 2 (Task B)
all_rounds['Points_from_result_B'] = all_rounds.apply(
    lambda row: categorize_winlosedraw(row, 'B'), axis=1)
all_rounds['Points_from_weapon_choice_B'] = all_rounds.apply(
    lambda row: categorize_weapon(row, 'B'), axis=1)
all_rounds['Points_combined_B'] = all_rounds['Points_from_result_B'] + \
    all_rounds['Points_from_weapon_choice_B']
final_score_B = all_rounds['Points_combined_B'].sum()

# results:
# print(all_rounds)
print(final_score_A)
print(final_score_B)

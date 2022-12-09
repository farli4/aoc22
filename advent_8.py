import numpy as np


def check_visibility(arr, current_height):
    visible = True
    for x in arr:
        if x >= current_height:
            visible = False
    if visible:
        return True
    else:
        return False


def visible(i, j, forest):
    current_height = forest[i, j]
    is_visible = True
    if current_height == 0:
        return False
    if check_visibility(forest[i, 0:j], current_height):
        return True
    elif check_visibility(forest[0:i, j], current_height):
        return True
    elif check_visibility(
            forest[i, j+1:len(forest)], current_height):
        return True
    elif check_visibility(
            forest[i+1:len(forest), j], current_height):
        return True
    else:
        return False


def calculate_score(arr, current_height):
    score = 0
    for x in arr:
        score += 1
        if x < current_height:
            continue
        else:
            break
    return score


def visual_scoring(i, j, forest):
    current_height = forest[i, j]
    score_left = calculate_score(np.flip(forest[i, 0:j]), current_height)
    score_upper = calculate_score(np.flip(forest[0:i, j]), current_height)
    score_right = calculate_score(forest[i, j+1:len(forest)], current_height)
    score_bottom = calculate_score(forest[i+1:len(forest), j], current_height)
    return score_left * score_upper * score_right * score_bottom


def load_data(fname):
    forest = []
    with open('8_input.txt') as f:
        i = 0
        for line in f:
            forest.append([])
            row = line.strip()
            for c in row:
                forest[i].append(int(c))
            i += 1
    forest = np.array(forest)
    return forest


if __name__ == '__main__':
    forest = load_data('8_input.txt')
    counter = 0
    visual_scores = []
    for i in range(1, len(forest)-1):
        for j in range(1, len(forest[0])-1):

            # 2nd task: visual scores
            visual_scores.append(visual_scoring(i, j, forest))

            # 1st task: count visible trees
            if visible(i, j, forest):
                counter += 1

    sum_visible = len(forest)*4 - 4 + counter
    max_visual_score = max(visual_scores)

    print(
        f'sum of visible trees of the forest viewed from outside: {sum_visible}')
    print(
        f'max visual score for a tree in the given forest: {max_visual_score}')

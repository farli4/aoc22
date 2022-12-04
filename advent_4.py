with open('4_input.txt') as f:
    
    sum_fully_containing_pairs = 0
    sum_overlapping_pairs = 0

    for line in f:
        area_limits = line.rstrip().replace('-', ',').split(',')
        
        # the line above coud be: area_limits = list(map(int, area_limits)), but I'm not sure which is better performing
        a, b, c, d = int(area_limits[0]), int(area_limits[1]), int(area_limits[2]), int(area_limits[3])

        if (a <= c and c <= b) or (a <= d and d <= b) or (c <= a and a <= d) or (c <= b and b <= d):
            sum_overlapping_pairs += 1
            if (a >= c and b <= d) or (c >= a and d <= b):
                sum_fully_containing_pairs += 1

# results:
print(f'num of pairs that fully contain each other: {sum_fully_containing_pairs}')
print(f'num of pairs that overlap: {sum_overlapping_pairs}')








"""


with open('4_input.txt') as f:
    sum_fully_containing_pairs = 0
    for line in f:
        area_limits = line.rstrip().replace('-', ',').split(',')
        area_limits = list(map(int, area_limits))
        if (area_limits[0] >= area_limits[2] and area_limits[1] <= area_limits[3]) or (area_limits[2] >= area_limits[0] and area_limits[3] <= area_limits[1]):
            sum_fully_containing_pairs += 1
        print(f'{line} : {sum_fully_containing_pairs}') """

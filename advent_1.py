with open('1_1_input.txt') as f:
    # read file and make a list containing lists of the numbers(in str format) that belong to one elf each
    calories_list = [k.split('\n') for k in [c_per_elf_str.strip()
                                             for c_per_elf_str in f.read().split('\n\n')]]

# convert str numbers to integers
for i in range(len(calories_list)):
    calories_list[i] = [int(item) for item in calories_list[i]]

# we need the summed calories for each elf, and then to sum the first three (so we have to order this list first)
calories_per_elf = [sum(cals_list_per_elf)
                    for cals_list_per_elf in calories_list]
sorted_calories_per_elf = sorted(calories_per_elf, reverse=True)
most_cals_per_elf = sorted_calories_per_elf[0]
top_3_cals_summed = sum(sorted_calories_per_elf[0:3])

print(most_cals_per_elf)
print(top_3_cals_summed)


# this code is only suitable for cases when only a few first calorie sums have to be selected
# it gets very repetitive and complicated for cases where n>3
""" with open('1_1_input.txt', mode='r') as my_file:
    #elf_with_most_calories = -1
    most_calories = 0
    second_most = 0
    third_most = 0
    calories = 0
    for line in my_file.readlines():
        if line.strip():
            calories += int(line)
            
        else:
            if calories > most_calories:
                third_most = second_most
                second_most = most_calories
                most_calories = calories
                
            elif calories > second_most:
                third_most = second_most
                second_most = calories
            elif calories > third_most:
                third_most = calories
            calories = 0
    print(most_calories)
    print(second_most)
    print(third_most)
    print(most_calories+second_most+third_most) """

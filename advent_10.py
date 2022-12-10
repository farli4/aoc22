
# only store numbers : 1 row in command list = the num to add in the current cycle
# if you have an add command in original file: first add one row with zero value, then the num to add
def read_file(fname):
    command_list = []
    with open(fname) as f:
        for line in f:
            full_command = line.strip()
            command_list.append(0)
            if full_command != 'noop':
                num = full_command.split(" ")[1]
                command_list.append(int(num))
    return command_list


if __name__ == '__main__':
    # each line of this list contains an integer for each clock cycle (0 if don't need to add anything atm)
    commands = read_file('10_input.txt')

    # variables for Task 1
    sum_signal_strength = 0
    value = 1

    # container, variable for Task 2
    drawing = []
    line_of_drawing = ''

    for i, command in enumerate(commands):
        # Task 2:
        sprite_start = value-1
        sprite_end = value + 1
        if sprite_end >= i % 40 >= sprite_start:
            line_of_drawing = line_of_drawing + '#'
        else:
            line_of_drawing = line_of_drawing + '.'
        # Task 2: if we're at the end of the row, start a new row
        if (i + 1) % 40 == 0:
            drawing.append(line_of_drawing)
            line_of_drawing = ''

        # Task 1:
        if (i-19) % 40 == 0:
            sum_signal_strength += value * (i+1)
        value += command

    # Task 1 result:
    print(
        f'Task 1: sum of signal strengths calculated according to instructions: {sum_signal_strength}\n')
    # Task 2 result:
    print(f'Task 2: message on the screen: \n')
    for line in drawing:
        print(line)

import copy


def read_file(filename):
    with open(filename) as f:
        crates_stack = []
        instructions = []
        for i, line in enumerate(f):
            if i < 8:
                crates_stack.append(line.replace(
                    '    ', ' ').replace('\n', '').split(' '))
            if i > 9:
                instructions.append(
                    [int(line.strip().split(' ')[x]) for x in [1, 3, 5]])

        crates_stack = list(map(list, zip(*crates_stack)))
        for i, row in enumerate(crates_stack):
            crates_stack[i] = [x.replace('[', '').replace(']', '') for x in row if x != '']

    return crates_stack, instructions


def reorganize_crates(crates_stack, instructions):
    #print('crates stack 2nd  \n',crates_stack)
    rearranged_crates_0 = copy.deepcopy(crates_stack)
    rearranged_crates_1 = copy.deepcopy(crates_stack)
    
    for i, instruction in enumerate(instructions):
        
        this_many = instruction[0]
        from_stack = instruction[1]-1
        to_stack = instruction[2]-1
        
        # second part solution:
        rearranged_crates_1[to_stack][0:0] = rearranged_crates_1[from_stack][0:this_many]
        del rearranged_crates_1[from_stack][0:this_many]
        
        # first part solution
        for j in range(this_many):
            rearranged_crates_0[to_stack].insert(
                0, rearranged_crates_0[from_stack][0])
            del rearranged_crates_0[from_stack][0]
            
    return rearranged_crates_0, rearranged_crates_1


if __name__ == '__main__':
    
    crates, instr = read_file('5_input.txt')
    crates_reorganized_0, crates_reorganized_1 = reorganize_crates(crates, instr)
    
    final_crates_on_top_0 = ''.join([stack[0] for stack in crates_reorganized_0])
    final_crates_on_top_1 = ''.join([stack[0] for stack in crates_reorganized_1])

    print(final_crates_on_top_0)
    print(final_crates_on_top_1)


from abc import ABCMeta, abstractmethod


def sum_size(l):
    if isinstance(l, int):
        return l

    summed_size = 0
    for item in l:
        summed_size = summed_size + sum_size(item)

    return summed_size


class Component(metaclass=ABCMeta):

    def get_parent(self):
        return self.parent
    
    def is_composite(self) -> bool:
        return False
    
    @abstractmethod
    def calculate_size():
        '''return sumed size of all leaf elements within composite/ return size of leaf element '''
        pass


class File(Component):
    
    def __init__(self,name, size, parent):
        self.size = size
        self.name = name
        self.parent = parent     
        
    def calculate_size(self):
        return self.size
    
    
class Folder(Component):
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []     
    
    def add(self, component: Component) -> None:
        self.children.append(component)
        component.parent = self
        
    def is_composite(self) -> bool:
        return True
    
    def calculate_size(self ):
        results = []
        for child in self.children:
            results.append(child.calculate_size())
        return sum_size(results)
            

with open('7_input.txt') as f:
    data = f.read().strip().split('\n')
    

component_list = []
current_dir = Folder('/', '')
previous_dir = current_dir
component_list.append(current_dir)

for line in data[1:]:
    if line[0:3] == 'dir':
        continue
    
    if line[:4] == '$ cd' and line [5] != '.':
        new_folder = Folder(line[5:], current_dir)
        current_dir.add(new_folder)
        #print(f"folder name: {new_folder.name}, parent name: {previous_dir.name}")
        component_list.append(new_folder)
        previous_dir = current_dir
        current_dir = new_folder  
        
    if line[0].isnumeric():
        file_size, file_name = line.split(" ")
        new_file = File(file_name,int(file_size),current_dir)
        current_dir.add(new_file)
        component_list.append(new_file)

    if line == '$ cd ..':
        current_dir = previous_dir
        try:
            previous_dir = current_dir.parent
        except AttributeError:
            previous_dir = component_list[0]

    if line == '$ ls':
        continue

# task 1:  
summed_size_under_100000 = 0
for line in component_list[1:]:
    if line.is_composite():
        folder_sum = line.calculate_size()
        if folder_sum <= 100000:
            summed_size_under_100000 += folder_sum

print(f'summed size of folder under 100000: {summed_size_under_100000}')

# task 2:
space_needed = 30000000- (70000000 - sum_size(component_list[0].calculate_size()))
big_enough_folders = [folder.calculate_size() for folder in component_list if folder.calculate_size() >= space_needed]

print(f'size of smallest folder that frees up enough storage: {sorted(big_enough_folders)[0]}')
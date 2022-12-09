from json import dumps
from typing import List


with open('2022/data/day7.txt') as f:
    raw_input = f.read()

class Command:
    def __init__(self, cmd, args, outputs):
        self.cmd = cmd
        self.args = args
        self.outputs = outputs

    def __repr__(self):
        return str(self.__dict__)

class Item():
    def __init__(self, type, name, pwd, size = 0):
        self.type = type
        self.name = name
        self.pwd = pwd
        self.children: List[Item] = []
        self.size = int(size)

    def tojson(self):
        return {
            'type': self.type,
            'name': self.name,
            'pwd': self.pwd,
            'children': [child.tojson() for child in self.children],
            'size': self.size
        }

    def walk(self):
        results = []
        for child in self.children:
            if child.type == 'dir':
                results.append([child.name, child.size])
                for res in child.walk():
                    results.append(res)
        return results

    def calculate_size(self):
        sum = 0
        for child in self.children:
            if child.type == 'dir':
                child.calculate_size()
                sum += child.size
            else:
                sum += int(child.size)
        self.size = sum

    def __repr__(self):
        return dumps(self.tojson(), indent=4)

command_split = [c.strip() for c in raw_input.split('$')]
commands = []
for i, ro in enumerate(command_split):
    if i < 2 : continue
    try:
        firstlinebreak = ro.index('\n')
        cmd, *args = ro[:firstlinebreak].split(' ')
        outputs = []
        for o in ro[firstlinebreak:].split('\n')[1:]:
            prefix, name = o.split(' ')
            if prefix == 'dir':
                objtype = prefix
                size = 0
            else:
                objtype = 'file'
                size = prefix
            outputs.append({'name':name, 'type':objtype, 'size':size})
    except ValueError:
        firstlinebreak = None
        cmd, args = ro.split(' ')
        outputs = None
    commands.append(Command(cmd, args if args else None, outputs))

pwd = '/'
tree = Item('dir', 'root', None)
item_to_add_to = tree
for command in commands:
    # print(command)
    if command.cmd == 'ls':
        for output in command.outputs:
            item_to_add_to.children.append(Item(output['type'], output['name'], pwd, output.get('size')))
    if command.cmd == 'cd':
        if command.args == '..':
            pwd_parts = pwd.split('/')[1:-1]
            pwd_parts = pwd_parts[:-1]
            pwd_parts = ['',*pwd_parts,'']
            pwd = '/'.join(pwd_parts)
            if pwd == '':
                pwd = '/'
        else:
            pwd += command.args + '/'
        if pwd == "/":
            item_to_add_to = tree
        else:
            pwd_parts = pwd.split('/')[1:-1]
            item_to_add_to = tree
            for part in pwd_parts:
                item_to_add_to = [child for child in item_to_add_to.children if child.name == part][0]

tree.calculate_size()
walk_results = [[tree.name, tree.size], *tree.walk()]

small_dir_sum = sum([dir[1] for dir in walk_results if dir[1] < 100000])
print('part1 ans:')
print(small_dir_sum)
print()

total_disk_space = 70000000
space_required_to_update = 30000000
max_used_space = 40000000

total_used_space = tree.size #sum([dir[1] for dir in walk_results])
print('total used space', total_used_space)
need_to_delete = total_used_space-max_used_space
print('  need to delete', need_to_delete)

print()

big_enough_to_delete = ['none', 10000000000000000]
for folder in walk_results:
    if folder[1] > need_to_delete:
        if folder[1] < big_enough_to_delete[1]:
            big_enough_to_delete = folder

print(big_enough_to_delete)
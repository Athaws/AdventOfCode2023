with open('input.txt', 'r') as f:
    instructions, blank, *rest = f.read().splitlines()
    
    destinations = {}
    for line in rest:
        line = line.strip().split(' = ')
        destinations[line[0]] = line[1].replace('(', '').replace(')', '').replace(' ', '').split(',')
    
    next, counter = 'AAA', 0
    while next != 'ZZZ':
        counter += 1
        next = destinations[next][0 if instructions[0] == 'L' else 1]
        instructions = instructions[1:] + instructions[0]
    
    print(counter)
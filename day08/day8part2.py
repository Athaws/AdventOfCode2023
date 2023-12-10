from math import gcd

with open('input.txt', 'r') as f:
    instructions, blank, *rest = f.read().splitlines()
    
    destinations = {}
    for line in rest:
        line = line.strip().split(' = ')
        destinations[line[0]] = line[1].replace('(', '').replace(')', '').replace(' ', '').split(',')
    
    startings = [dst for dst in destinations if dst.endswith('A')]
    wins = []
    
    for start in startings:
        instructions_tmp, counter, win = instructions, 0, []
        z_found = None
        
        while True:
            while not start.endswith('Z') or counter == 0:
                counter += 1
                start = destinations[start][0 if instructions_tmp[0] == 'L' else 1]
                instructions_tmp = instructions_tmp[1:] + instructions_tmp[0]
            print(counter)
            wins.append(counter)
            
            if z_found is None:
                z_found = start
                counter = 0
            elif z_found == start:
                break
        if win != []:
            wins.append(win)
    lcm = wins.pop()
    for winner in wins:
        lcm = lcm * winner // gcd(lcm, winner)
    print(lcm)
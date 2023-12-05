with open('input.txt', 'r') as f:
    lines = f.readlines()
    tmp = lines.pop(0).replace('seeds: ', '').strip().split(' ')
    seeds = [int(i) for i in tmp]
    print(seeds)
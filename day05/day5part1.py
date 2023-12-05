with open('input.txt', 'r') as f:
    seeds, *rest = f.read().split('\n\n')
    seeds = [int(i) for i in seeds.replace('seeds:', '').split(' ') if i]
    for part in rest:
        startRanges = []
        for p in part.splitlines()[1:]:
            startRanges.append([int(i) for i in p.split()])
        nextStep = []
        for seed in seeds:
            for x, y, z in startRanges:
                if seed in range(y, y+z):
                    nextStep.append(seed+x-y)
                    break
            else:
                nextStep.append(seed)
        seeds = nextStep
print(min(seeds))
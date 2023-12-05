with open('input.txt', 'r') as f:
    seedRanges, *rest = f.read().split('\n\n')
    seedRanges = [int(i) for i in seedRanges.replace('seeds:', '').split(' ') if i]
    seeds = []
    for i in range(0, len(seedRanges), 2):
        seeds.append((seedRanges[i], seedRanges[i] + seedRanges[i+1]))
    for part in rest:
        startRanges = []
        for p in part.splitlines()[1:]:
            startRanges.append([int(i) for i in p.split()])
        nextStep = []
        while len(seeds) > 0:
            start, stop = seeds.pop(0)
            for x, y, z in startRanges:
                startOver = max(start, y)
                stopOver = min(stop, y+z)
                if startOver < stopOver:
                    nextStep.append((startOver+x-y, stopOver+x-y))
                    if startOver > start:
                        seeds.append((start, startOver))
                    if stop > stopOver:
                        seeds.append((stopOver, stop))
                    break
            else:
                nextStep.append((start, stop))
        seeds = nextStep
print(min(seeds))
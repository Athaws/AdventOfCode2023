def getDiffs(list):
    if all(i == 0 for i in list):
        return 0
    diffs = [b-a for a,b in zip(list, list[1:])]
    diff = getDiffs(diffs)
    return list[0] - diff

with open('input.txt', 'r') as f:
    total = 0
    for line in f.read().splitlines():
        nums = list(int(i) for i in line.split(' '))
        total += getDiffs(nums)
    print(total)
sum = 0
coordinateSet = set()

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    for l, line in enumerate(lines):
        for c, char in enumerate(line):
            if char.isdigit() or char == '.':
                continue
            for lc in [l-1, l, l+1]:
                for cc in [c-1, c, c+1]:
                    if lc < 0 or lc >= len(lines) or cc < 0 or cc >= len(lines[lc]) or not lines[lc][cc].isdigit():
                        continue
                    while cc > 0 and lines[lc][cc-1].isdigit():
                        cc -= 1
                    coordinateSet.add((lc, cc))

for l, c in coordinateSet:
    tmp = ''
    while c < len(lines[l]) and lines[l][c].isdigit():
        tmp += lines[l][c]
        c += 1
    sum += int(tmp)

print(sum)
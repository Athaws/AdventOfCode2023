total = 0
with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    for l, line in enumerate(lines):
        for c, char in enumerate(line):
            if char != '*':
                continue
            coordinateSet = set()
            for lc in [l-1, l, l+1]:
                for cc in [c-1, c, c+1]:
                    if lc < 0 or lc >= len(lines) or cc < 0 or cc >= len(lines[lc]) or not lines[lc][cc].isdigit():
                        continue
                    while cc > 0 and lines[lc][cc-1].isdigit():
                        cc -= 1
                    coordinateSet.add((lc, cc))
            if len(coordinateSet) != 2:
                continue
            nums = []
            for lc, cc in coordinateSet:
                tmp = ''
                while cc < len(lines[lc]) and lines[lc][cc].isdigit():
                    tmp += lines[lc][cc]
                    cc += 1
                nums.append(int(tmp))
            total += nums[0] * nums[1]
print(total)
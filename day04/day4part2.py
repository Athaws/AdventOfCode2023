with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    numCopies = [1] * len(lines)
    for l, line in enumerate(lines):
        tmpline = line.split('|')
        winNums, myNums = tmpline[0].lstrip('Card').replace(':', '').strip().split(' '), tmpline[1].strip().split(' ')
        winNums, myNums = [int(x) for x in winNums if x], [int(x) for x in myNums if x]
        currCard = winNums.pop(0)-1
        cardsToAdd = sum(1 for x in myNums if x in winNums)
        for x in range(l+1, l+cardsToAdd+1):
            numCopies[x] += numCopies[l]
print(sum(numCopies))
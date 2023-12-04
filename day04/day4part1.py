sum = 0
with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    for line in lines:
        line = line.split('|')
        winNums, myNums = line[0].lstrip('Card').strip().split(' ')[1:], line[1].strip().split(' ')
        winNums, myNums = [int(i) for i in winNums if i], [int(i) for i in myNums if i]
        
        found, currCard = False, 0
        for num in myNums:
            if found and num in winNums:
                currCard *= 2 
            elif not found and num in winNums:
                currCard += 1
                found = True
        sum += currCard
print(sum)
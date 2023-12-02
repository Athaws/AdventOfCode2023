sum = 0
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n','').replace('Game ','').replace(',','')
        line = line.split(':')
        impossible, gamenumber = False, int(line[0])
        minRed, minGreen, minBlue = 1, 1, 1
        for parts in line[1].split(';'):
            parts = parts.split(' ')
            for i in range(1, len(parts), 2):
                if int(parts[i]) > minRed and parts[i+1] == 'red':
                    minRed = int(parts[i])
                elif int(parts[i]) > minGreen and parts[i+1] == 'green':
                    minGreen = int(parts[i])
                elif int(parts[i]) > minBlue and parts[i+1] == 'blue':
                    minBlue = int(parts[i])
        sum += minRed * minGreen * minBlue
print(sum)
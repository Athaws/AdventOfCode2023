sum = 0
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n','').replace('Game ','').replace(',','')    # Remove fluff from string
        line = line.split(':')                                              # Split gamenumber from rest
        impossible, gamenumber = False, int(line[0])
        minRed, minGreen, minBlue = 1, 1, 1
        for parts in line[1].split(';'):                                    # Split line by sub-games
            parts = parts.split(' ')                        # Split subgame into respective number and colour
            for i in range(1, len(parts), 2):
                if int(parts[i]) > minRed and parts[i+1] == 'red':  
                    minRed = int(parts[i])      # Min. reds is updated if higher found in current subgame
                elif int(parts[i]) > minGreen and parts[i+1] == 'green':
                    minGreen = int(parts[i])    # Min. greens is updated if higher found in current subgame
                elif int(parts[i]) > minBlue and parts[i+1] == 'blue':
                    minBlue = int(parts[i])     # Min. blues is updated if higher found in current subgame
        sum += minRed * minGreen * minBlue      # Sum of the minumum of all colours added to sum
print(sum)
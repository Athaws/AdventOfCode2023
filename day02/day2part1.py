MAXRED, MAXGREEN, MAXBLUE = 12, 13, 14

sum = 0
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n','').replace('Game ','').replace(',','')    # Remove fluff from line
        line = line.split(':')                                              # Split gamenumber from rest
        impossible, gamenumber = False, int(line[0])
        for parts in line[1].split(';'):                                    # Split line by sub-games
            if impossible:                      # If game is impossible, immediately move to next game
                break
            parts = parts.split(' ')            # Split subgame into respective number and colour
            for i in range(1, len(parts), 2):
                if int(parts[i]) > MAXRED and parts[i+1] == 'red':          # Check first number and colour
                    impossible = True
                    break
                elif int(parts[i]) > MAXGREEN and parts[i+1] == 'green':    # Check second number and colour
                    impossible = True
                    break
                elif int(parts[i]) > MAXBLUE and parts[i+1] == 'blue':      # Check third number and colour
                    impossible = True
                    break
        if not impossible:          # If none of the checks flagged for impossibility, add game-number to sum
            sum += gamenumber
print(sum)
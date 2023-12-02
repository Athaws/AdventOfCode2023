MAXRED, MAXGREEN, MAXBLUE = 12, 13, 14

sum = 0
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n','').replace('Game ','').replace(',','')
        line = line.split(':')
        impossible, gamenumber = False, int(line[0])
        for parts in line[1].split(';'):
            if impossible:
                break
            parts = parts.split(' ')
            for i in range(1, len(parts), 2):
                print(parts[i], parts[i+1])
                if int(parts[i]) > MAXRED and parts[i+1] == 'red':
                    impossible = True
                    break
                elif int(parts[i]) > MAXGREEN and parts[i+1] == 'green':
                    impossible = True
                    break
                elif int(parts[i]) > MAXBLUE and parts[i+1] == 'blue':
                    impossible = True
                    break
        if not impossible:
            sum += gamenumber
print(sum)
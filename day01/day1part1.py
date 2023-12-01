import re
total = 0
with open('input.txt', 'r') as f:
    lines = f.readlines()   # Read the entire contents of the file
    for line in lines:      # Process one line at a time
        line = re.sub(r'[^0-9]', '', line)      # Remove anything that isn't a digit
        line = line[0] + line[0] if len(line) == 1 else line[0] + line[-1]  # If only one digit: duplicate
        total += int(line)  # Add current line's value to the total
print(total)    # Print total
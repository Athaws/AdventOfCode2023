import re
wordToNum = {   'nine':'n9e', 'eight':'e8t', 'seven':'s7n', # Map the words of numbers with actual numbers.
                'six':'s6x', 'five':'f5e', 'four':'f4r',    # Keeping the first and last letter,
                'three':'t3e', 'two':'t2o', 'one':'o1e'     # due to possible overlaps of words/numbers
            }
total = 0
with open('input.txt', 'r') as f:
    lines = f.readlines()   # Read the entire input file
    for line in lines:      # Process each line, one at a time
        for key, value in wordToNum.items():    # Match the words of the numbers to their digit counterparts
            line = line.replace(key, value)     # Replace the words with actual numbers, one at a time
        line = re.sub(r'[^0-9]', '', line)      # Remove anything that isn't a digit
        line = line[0] + line[0] if len(line) == 1 else line[0] + line[-1] # If only one digit: duplicate
        total += int(line)  # Add current line's value to the total
print(total)                # Print the total
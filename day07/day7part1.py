reorderValue = {'T':'A', 'J':'B', 'Q':'C', 'K':'D', 'A':'E',} # Reord cards for alphabetical order

def trueVal(hand):
    cs = [hand.count(c) for c in hand]
    if 5 in cs:
        return 6
    if 4 in cs:
        return 5
    if 3 in cs:
        return 4 if 2 in cs else 3
    if cs.count(2) == 4:
        return 2
    if 2 in cs:
        return 1
    return 0

def handStrength(hand):
    return trueVal(hand), [reorderValue.get(c, c) for c in hand]

with open('input.txt', 'r') as f:
    lines, games = f.read().split('\n'),[]
    for line in lines:
        hand, bid = line.split(' ')
        games.append((hand, int(bid)))
    games.sort(key=lambda game: handStrength(game[0]))
    
    total = 0
    for g, (h, b) in enumerate(games, 1):
        print(g, h, b)
        total += (g * b)
    print(total)
with open('input.txt', 'r') as f:
    lines = f.readlines()
    times, records = [i for i in lines[0].split() if i.isdigit()], [i for i in lines[1].split() if i.isdigit()]
    time, record = int(''.join(times)), int(''.join(records))
    total = 0
    for i in range(time):
        if (time-i) * i > record:
            total += 1
    print(total)
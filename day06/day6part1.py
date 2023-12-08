with open('input.txt', 'r') as f:
    lines = f.readlines()
    times = [int(i) for i in lines[0].split() if i.isdigit()]
    records = [int(i) for i in lines[1].split() if i.isdigit()]
    results, sum = [0, 0, 0, 0], 1
    for i, time in enumerate(times):
        for j in range(time):
            if (time-j) * j > records[i]:
                results[i] += 1
    for i in results:
        sum *= i
    print(sum)
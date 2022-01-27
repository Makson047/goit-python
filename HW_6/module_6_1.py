def total_salary(path):
    tot=0.0
    fh = open(path, 'r')
    while True:
        line = fh.readline()
        if not line:
            break
        print(line)
        tot += float(line.split(',')[1])

    fh.close()
    return tot
def read_employees_from_file(path):
    fh = open(path, 'r')
    res = fh.read().splitlines()
    fh.close()
    return res
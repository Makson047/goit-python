def get_cats_info(path):
    res = []
    with open(path, 'r') as f:
        lines = f.readlines()
        for line1 in lines:
            line = line1.split('\n')[0]
            dic = {"id": line.split(',')[0],
                   "name": line.split(',')[1],
                   "age": line.split(',')[2]}
            res += [dic]
    return res
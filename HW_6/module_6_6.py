def get_recipe(path, search_id):
    res = None
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:

            if line.split(',')[0] == search_id:
                res = {"id": line.split(',')[0],
                       "name": line.split(',')[1],
                       "ingredients": [
                           line.split(',')[2],
                           line.split(',')[3],
                           line.split(',')[4].split('\n')[0],
                       ],
                       }
            else:
                continue
    return res
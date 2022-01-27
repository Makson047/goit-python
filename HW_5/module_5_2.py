articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
    ]



def find_articles(key, letter_case=False):
    lists = []
    for i in articles_dict:
        for k, v in i.items():
            if k == 'title':
                if not letter_case:
                    v_low = v.lower()
                    key = key.lower()
                    res = v.find(key)
                    res_low = v_low.find(key)
                    if res != -1 or res_low != -1:
                        lists.append(i)
                else:
                    res = v.find(key)
                    if res != -1:
                        lists.append(i)

            elif k == 'author':
                if not letter_case:
                    v = v.lower()
                    key = key.lower()
                    res = v.find(key)
                    # res_low = v_low.find(key)
                    if res != -1:  # or res_low != -1:
                        lists.append(i)
                else:
                    res = v.find(key)
                    if res != -1:
                        lists.append(i)
                    else:
                        break
            else:
                continue
    print(lists)
    return lists


find_articles('Silver', True)
find_articles('Ocean')

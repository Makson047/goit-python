import re


def find_word(text, word):
    s = re.search(word, text)
    res = {}
    if s != None:
        res = { 'result': True,
                'first_index': s.span()[0],
                'last_index': s.span()[1],
                'search_string': word,
                'string': text}
    else:
      res = {'result': False,
             'first_index': None,
                'last_index': None,
                'search_string': word,
                'string': text}
    return res

"""
1.Длина строки пароля восемь символов.+
2.Содержит хотя бы одну букву в верхнем регистре.+
3.Содержит хотя бы одну букву в нижнем регистре.+
4.Содержит хотя бы одну цифру.+
"""


def is_valid_password(password):
    numbers = '1234567890'
    numbers_set = set(numbers)
    symbols = set(password)
    alfabet = 'abcdefghijklmnopqrstyvwxyz'
    alfabet_lower = set(alfabet.lower())
    alfabet_upper = set(alfabet.upper())
    if len(password) != 8:
        print('not 8')
        return False
    elif not bool(numbers_set & symbols):
        print('not number')
        return False
    elif not bool(alfabet_lower & symbols):
        print('not lower')
        return False
    elif not bool(alfabet_upper & symbols):
        print('not upper')
        return False
    else:
        return True


print(is_valid_password('Dfdfhgu1'))

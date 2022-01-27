def is_valid_pin_codes(pin_codes):
    for codes in pin_codes:
        for el in codes:
            if not el.isdigit():
                return False
        if len(codes) != 4:
            return False
        elif type(codes) is not str:
            return False
    set_code = set(pin_codes)

    if len(pin_codes) == 0:
        return False
    elif len(set_code) != len(pin_codes):
        return False
    else:
        return True


print(is_valid_pin_codes(['1101', '9034', '001a']))

def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    phone_dict = {}
    phone_dict.fromkeys(["UA", "JP", "TW", "SG"])
    pref_jp = '81'
    pref_sg = '65'
    pref_tw = '886'
    ua = []
    jp = []
    tw = []
    sg = []
    for i in list_phones:
        clear_number = sanitize_phone_number(i)
        if clear_number.removeprefix(pref_jp) != clear_number:
            jp.append(clear_number)
        elif clear_number.removeprefix(pref_sg) != clear_number:
            sg.append(clear_number)
        elif clear_number.removeprefix(pref_tw) != clear_number:
            tw.append(clear_number)
        else:
            ua.append(clear_number)
    phone_dict['JP'] = jp
    phone_dict['SG'] = sg
    phone_dict['TW'] = tw
    phone_dict['UA'] = ua
    return phone_dict














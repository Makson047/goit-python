import re


def find_all_emails(text):
    result = re.findall(r"[a-zA-Z]+[a-zA-Z0-9_.]+@[a-zA-Z]+[.]{1}[a-zA-Z]{1}[a-zA-Z]+", text)
    return result

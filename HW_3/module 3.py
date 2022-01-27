# Task 6
# def format_string(string, length):
#     if len(string) >= length:
#         return string
#     else:
#         res = ' ' * ((length - len(string)) // 2)
#         return f"{res}{string}"
#
#
# c = format_string(length=15, string='abaa')
# print(c)

# Task 7


def first(size, *numb):
    size = size + len(numb)
    return size


print(first(5, "first", "second", "third"))

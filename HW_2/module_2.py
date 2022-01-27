#  Caesar`s code
# "Hello my little friends!", offset = 37,
# "Hello world!", offset = 7
message = "Hello world!"  # input("Введите сообщение: ")
offset = 7  # int(input("Введите сдвиг: "))
encoded_message = ""
for ch in message:
    pos = ord(ch) - ord('a')  # 21
    pos = (pos + offset) % 26  # 2
    new_char = chr(pos + ord("a"))
    encoded_message += new_char
    a=0
print(encoded_message)


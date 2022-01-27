def formatted_numbers():
    formatted_list = []
    title = '|{:^10}|{:^10}|{:^10}|'.format('decimal', 'hex', 'binary')
    formatted_list.append(title)
    for i in range(16):
        row = '|{:<10d}|{:^10x}|{:>10b}|'.format(i,i,i)
        formatted_list.append(row)
    return formatted_list


print(formatted_numbers())


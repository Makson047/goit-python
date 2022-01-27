import re


# file_name = "File.txt"
file_name = input('Please enter your file name:')
data = {}

with open(file_name, 'r') as fh:
    while True:
        line = fh.readline()
        if not line:
            break
        name = re.findall(r"\w+[.][a-zA-Z]{2,4}", line)
        memory_cell = re.findall(r"\(.+\)", line)
        if memory_cell:
            normalized_cell_name = re.findall(r"\dx[a-zA-Z]*[a-zA-Z0-9]+", memory_cell[0])
        if name and normalized_cell_name:
            data[normalized_cell_name[0]] = name[0]

new_file_name = "data_list.txt"
with open(new_file_name, 'w') as new_file:
    for k, v in data.items():
        new_file.write(f'{k}: {v}\n')

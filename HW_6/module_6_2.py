def write_employees_to_file(employee_list, path):
    fh = open(path, 'w')
    for otdlist in employee_list:
        for employee in otdlist:
            fh.write(f'{employee}\n')

    fh.close()
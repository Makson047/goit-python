grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    print(students)
    i = 0
    grades_list = []
    for st, gr in students.items():
        st_list = [str(i + 1).rjust(4), st.ljust(10), gr.center(5), str(grades[gr]).center(5)]
        i += 1
        grades_list += ['|'.join(st_list)]
    print(grades_list)

    return grades_list


formatted_grades({'Nick': 'A', 'Olga': 'B', 'Boris': 'FX', 'Anna': 'C'})




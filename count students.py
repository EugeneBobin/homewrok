def group_by_surname(list_of_students):
    group_counts = [0, 0, 0, 0]

    for student in list_of_students:
        surname = student.split()[1]

        if 'A' <= surname[0] <= 'I':
            group_counts[0] += 1
        elif 'J' <= surname[0] <= 'P':
            group_counts[1] += 1
        elif 'Q' <= surname[0] <= 'T':
            group_counts[2] += 1
        elif 'U' <= surname[0] <= 'Z':
            group_counts[3] += 1

    return tuple(group_counts)
print(group_by_surname({"Will Smith", "Vasya Pupkin", "Irina Avramova", "Jay Z"}))
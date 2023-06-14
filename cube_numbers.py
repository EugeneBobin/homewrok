def generate_cube_numbers(limit):
    num = 2
    while True:
        cube = num ** 3
        if cube < limit:
            yield cube
        else:
            return
        num += 1

print(list(generate_cube_numbers(int(input("enter number :")))))

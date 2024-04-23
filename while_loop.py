def print_pyramid(rows):
    space = rows - 1
    row = 1

    while row <= rows:
        print(" " * space, end="")

        print("*" * (2 * row - 1))

        space -= 1
        row += 1

rows = 5

print_pyramid(rows)

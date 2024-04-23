# print a triangle pattern using for loops
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


# triangle pattern using nested while loops
rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1

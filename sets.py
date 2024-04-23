my_set = {1, 2, 3, 4, 5}

my_set.add(6)
my_set.add(7)

print("Set:", my_set)

my_set.remove(3)
print("Modified Set:", my_set)

print("Is 5 in the set?", 5 in my_set)

print("Iterating over the set:")
for item in my_set:
    print(item)

print("Length of the set:", len(my_set))

copy_of_set = my_set.copy()
print("Copy of the set:", copy_of_set)

my_set.clear()
print("Cleared Set:", my_set)

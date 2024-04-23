import random

num_times = int(input("How many random numbers do you want to generate? "))

for _ in range(num_times):
    random_number = random.randint(1, 100)
    print(random_number)
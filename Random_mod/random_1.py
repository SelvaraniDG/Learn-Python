import random

def generate_random_numbers(num_times):
    random_numbers = []
    for _ in range(num_times):
        random_number = random.randint(1, 100)
        random_numbers.append(random_number)
    return random_numbers
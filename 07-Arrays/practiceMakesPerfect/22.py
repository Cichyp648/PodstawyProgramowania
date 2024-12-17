import random

def rand_elem(array):
    return random.choice(array)

arr = [1, 2, 3, 4, 5, 6]
random_element = rand_elem(arr)

print("Array:", arr)
print("Randomly selected element:", random_element)
import random

# Generate a random integer between 0 and 9 (inclusive)
random_integer = random.randint(0, 9)
print(random_integer)

# Generate a random float between 0 and 1 (exclusive)
random_float = random.random()
print(random_float)

# Generate a random number using a normal distribution with mean 0 and standard deviation 1
random_normal = random.gauss(0, 1)
print(random_normal)

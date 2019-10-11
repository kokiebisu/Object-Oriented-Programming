import math

# Lambdas


def multiple_of_five(x): return x * 5


def squared(x): return x**0.5


numbers = [(lambda x: x ** 0.5)(i) for i in range(0, 10)]

print(multiple_of_five(10))
print(list(numbers))

# Maps
full_names = [
    "Ross Geller",
    "Rachel Green",
    "Phoebe Buffay",
]

first_names = ["ross", "rachel", "pheobe", "chandler", "monica", "joey"]
last_names = ["geller", "green", "buffay", "bing", "geller", "tribbiani"]


first_name_map = map(lambda x: x.split()[0], full_names)
print(type(first_name_map))
print(list(first_name_map))

# Filters
num_list = list(range(1, 10))
even_nums_filter = filter(lambda x: x % 2 == 0, num_list)
print(type(even_nums_filter))
print(list(even_nums_filter))

# Challenge 2: Lambda Functions
string = "Hello World"
vowels = ["a", "e", "i", "o", "u"]
string_filter = filter(lambda x: x not in vowels, string)
print(string_filter)
print(list(string_filter))

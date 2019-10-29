# Multiple arguments, combining two lists
first_names = ["Ross", "Rachel", "Phoebe"]
last_names = ["Galler", "Greem", "Buffay"]
full_names = map(lambda x, y: f"{x} {y}", first_names, last_names)
list(full_names)
print(type(full_names))
print(list(full_names))
print(tuple(full_names))

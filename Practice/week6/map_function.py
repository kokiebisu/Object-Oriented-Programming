full_names = [
    "Ken Henry",
    "Waterloo Geourge",
    "Father boy",
    "mama sails"
]

first_name_map = map(lambda x: x.split()[0], full_names)
print(type(first_name_map))
print(list(first_name_map))
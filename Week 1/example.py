my_dict = {
    'a': 50,
    'b': 20,
    'c': 80,
    'd': 10
}

keys_to_remove = ['a', 'b']

for key in keys_to_remove:
    if key in my_dict:
        del my_dict[key]

print(my_dict)

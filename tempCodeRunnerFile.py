
from numpy import concatenate


def print_dictionary(my_dict):
    for key, value in my_dict.items():
        print(f"{key}: {value}")

    

d = {'foo': 100, 'bar': 200, 'baz': 300}
print_dictionary(d)
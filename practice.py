def print_dictionary(*words,**my_dict):
    for key, value in my_dict.items():
        print(f"{key}: {value}")
    
    for x in words:
        print(x)

d = {'foo': [100,'Aizaz','Abbottabad'], 'bar': [200,'Ali','Lahore'], 'baz': [300,'Shah','Karachi']}
print_dictionary(('foo', 100), ('bar', 200),d, ('baz', 300))
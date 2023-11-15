new_path = {"key": "C:\\Users\\aizaz\\OneDrive\\Desktop"}
s.path.append(new_path['key'])

from module import print_something as ps, name as nm
import sys as s
import sample as sam



ps()
print(nm)
print("User File")

print(sam.first_dict)

print(s.path,"\n\n")
print("Path of sample file is: ",sam.__file__,"\n\n")
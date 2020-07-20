import os
current_dir = os.path.abspath(os.path.dirname(__file__))
print(current_dir)

current_dir1 = os.path.dirname(__file__)
print(current_dir1)

parent_path = os.path.dirname(current_dir1)
print(parent_path)
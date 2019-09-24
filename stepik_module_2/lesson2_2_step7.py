import os

current_dir = os.path.abspath(os.path.dirname(__file__))
# ile_path = os.path.join(current_dir, 'file.txt')
print(current_dir)
print(os.path.abspath(__file__))
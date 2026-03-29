"py"

import os
from constant import BASE_DIR

for items in os.walk(BASE_DIR):
    path_to_file, list_dir, file_extension = items


    for py_file in file_extension:
        if py_file.endswith('.log'):
            print(f'{path_to_file}//{py_file}')



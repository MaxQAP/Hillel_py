#import pathlib
from pathlib import Path


#path_to_file = pathlib.Path(__file__).parent
#path_to_dir_where_file =pathlib.Path().cwd()
#print(path_to_file)
#root_dir = pathlib.Path().cwd().parent
#breakpoint()

from constant import DATA_FOR_TEST_DIR

with open(DATA_FOR_TEST_DIR/'new_file') as file:
    print(file.read())



#parents_dir = DATA_FOR_TEST_DIR/'parents_dir'/ 'parents_dir_1'
#print(parents_dir)
#parents_dir.mkdir(parents=True, exist_ok=True)

new_dir = DATA_FOR_TEST_DIR/'request_model'/ 'pat'
print(new_dir)
new_dir.mkdir(parents=True, exist_ok=True)
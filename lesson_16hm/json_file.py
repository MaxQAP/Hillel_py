import json
from constant import DATA_FOR_TEST_DIR




with open(DATA_FOR_TEST_DIR / 'json_test.json', 'r') as file:
    data = json.load(file)

print(data)
print(type(data))
print(data[1].get('name'))


with open(DATA_FOR_TEST_DIR / 'json_test22.json', 'w') as file:
    json.dump(data, file, indent=4)
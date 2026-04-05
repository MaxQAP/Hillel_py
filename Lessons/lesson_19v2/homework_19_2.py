import requests
import os

base_url = "http://127.0.0.1:8080"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "venus.jpeg")

#POST
with open(file_path, 'rb') as f:
    files = {'image': f}
    response = requests.post(f"{base_url}/upload", files=files)

if response.status_code == 201:
    print("Успішно завантажено!")
    image_url = response.json().get('image_url')
    print(f"URL з сервера: {image_url}")
else:
    print(f"Помилка завантаження: {response.text}")

import os
filename = os.path.basename(file_path)
#GET
print("\n--- Крок 2: Отримання посилання через GET ---")
headers = {'Content-Type': 'text'}
get_response = requests.get(f"{base_url}/image/{filename}", headers=headers)

if get_response.status_code == 200:
    print(f"Сервер підтвердив посилання: {get_response.json().get('image_url')}")
else:
    print(f"Помилка при отриманні: {get_response.text}")
#DELETE
print("\nКрок 3: Видалення файлу")
delete_response = requests.delete(f"{base_url}/delete/{filename}")

if delete_response.status_code == 200:
    print(f"Відповідь сервера: {delete_response.json().get('message')}")
else:
    print(f"Помилка при видаленні: {delete_response.text}")

